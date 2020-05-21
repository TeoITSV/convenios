# -*- coding: utf-8 -*-
from xlrd import open_workbook
from docxtpl import DocxTemplate
from django.conf import settings
from django.utils import six
import json
import sys
reload(sys)
import os
sys.setdefaultencoding('utf-8')

def __init__():
    pass

hojaDeDatos = settings.MEDIA_ROOT + 'hojaDatos.xlsx'
nombrePlantillaConvenioIndividual =  settings.MEDIA_ROOT + 'plantillaIndividuales.docx'
nombrePlantillaConvenioMarco = settings.MEDIA_ROOT + 'plantillaMarco.docx'
nombrePlantillaDiplomas = settings.MEDIA_ROOT + 'plantillaDiplomas.docx'
carpetaConveniosIndividuales = settings.MEDIA_ROOT + '/resultado/ConveniosIndividuales/'
carpetaConveniosMarco = settings.MEDIA_ROOT + '/resultado/ConveniosMarco/'
carpetaDiplomas = settings.MEDIA_ROOT + '/resultado/Diplomas/'
book = ''

def correrAplicacion(documento):
    global book
    book = open_workbook(hojaDeDatos)
    if (documento.count('a')==1):
        individual = crearConveniosIndividuales('individuales')
    else:
        individual = True
    if (documento.count('b')==1):
        marco = crearConveniosMarco()
    else:
        marco = True
    if (documento.count('c')==1):
        diplomas = crearConveniosIndividuales('diplomas')
    else:
        diplomas = True
    if(individual == True and marco == True and diplomas == True):
        return True

def crearConveniosIndividuales(diplomas):
    sheetAlumnos = book.sheet_by_index(0)
    keys = [sheetAlumnos.cell(0, col_index).value for col_index in xrange(sheetAlumnos.ncols)]
    for row_index in xrange(1, sheetAlumnos.nrows):
        dataAlumnos = {keys[col_index]: sheetAlumnos.cell(row_index, col_index).value
             for col_index in xrange(sheetAlumnos.ncols)}
        row_indexAlumnos = row_index
        json_strAlumnos = json.dumps(dataAlumnos)
        resp = json.loads(json_strAlumnos)
        sheetEmpresas = book.sheet_by_index(1)
        keysEmpresas = [sheetEmpresas.cell(0, col_index).value for col_index in xrange(sheetEmpresas.ncols)]
        for row_index in xrange(1, sheetEmpresas.nrows):
            nombreEmpresa = str(sheetEmpresas.cell(row_index,0).value)
            if (nombreEmpresa == resp['empresaElegida']):
                dataEmpresas = {keysEmpresas[col_index]: sheetEmpresas.cell(row_index, col_index).value
                    for col_index in xrange(sheetEmpresas.ncols)}
                dataAlumnos.update(dataEmpresas)
        if (diplomas == 'diplomas'):
            imprimirDiplomas(dataAlumnos)
        else:
            imprimirConvenios(dataAlumnos)
            # print dataAlumnos
        if(sheetAlumnos.nrows - 1 == row_indexAlumnos):
            return True


def crearConveniosMarco():
    sheetEmpresas = book.sheet_by_index(1)
    keysEmpresas = [sheetEmpresas.cell(0, col_index).value for col_index in xrange(sheetEmpresas.ncols)]
    for row_index in xrange(1, sheetEmpresas.nrows):
        dataEmpresas = {keysEmpresas[col_index]: sheetEmpresas.cell(row_index, col_index).value
             for col_index in xrange(sheetEmpresas.ncols)}
        json_strEmpresa = json.dumps(dataEmpresas)
        respEmpresa = json.loads(json_strEmpresa)
        imprimirConveniosMarco(dataEmpresas)
    row_indexEmpresa = row_index
    if(sheetEmpresas.nrows - 1 == row_indexEmpresa):
        return True

def imprimirConvenios(datosJason):
    json_str = json.dumps(datosJason)
    resp = json.loads(json_str)
    context = datosJason
    try:
        datosJason["dniAlumno"] = int(datosJason["dniAlumno"])
        datosJason["dniTutorAlumno"] = int(datosJason["dniTutorAlumno"])
        datosJason["dniTutorEmpresa"] = int(datosJason["dniTutorEmpresa"])
        datosJason['dniTitularEmpresa'] = int(datosJason['dniTitularEmpresa'])
        docIndi = DocxTemplate(nombrePlantillaConvenioIndividual)
        nombreAlumno = resp['nombreAlumno']
        nombreEmpresa = resp['nombreEmpresa']
        docIndi.render(context)
        docIndi.save(carpetaConveniosIndividuales +"Convenio Individual - "+ nombreEmpresa +" - "+ nombreAlumno +".docx")
    except:
        print "Error al convertir a int - convenio individual de: " + resp['nombreAlumno']

def imprimirConveniosMarco(datosJason):
    json_str = json.dumps(datosJason)
    resp = json.loads(json_str)
    context = datosJason
    try:
        datosJason['dniTitularEmpresa'] = int(datosJason['dniTitularEmpresa'])
        docIndi = DocxTemplate(nombrePlantillaConvenioMarco)
        nombreEmpresa = resp['nombreEmpresa']
        docIndi.render(context)
        docIndi.save(carpetaConveniosMarco + "Convenio Marco - "+ nombreEmpresa +" .docx")
    except:
        print "Error al convertir a int - convenio marco de: " + resp['nombreEmpresa']


def imprimirDiplomas(datosJason):
    json_str = json.dumps(datosJason)
    resp = json.loads(json_str)
    context = datosJason
    datosJason["dniAlumno"] = int(datosJason["dniAlumno"])
    datosJason["nombreAlumno"] = datosJason["nombreAlumno"].upper()
    datosJason["nombreEmpresa"] = datosJason["nombreEmpresa"].upper()
    datosJason["especialidad"] = datosJason["especialidad"].upper()
    docIndi = DocxTemplate(nombrePlantillaDiplomas)
    nombreAlumno = resp['nombreAlumno']
    nombreEmpresa = resp['nombreEmpresa']
    datosJason['cantidadHoras'] = int(datosJason['cantidadHoras'])
    docIndi.render(context)
    python_2_unicode_compatible = six.python_2_unicode_compatible
    docIndi.save(carpetaDiplomas+"Diploma - "+ nombreEmpresa +" - "+ nombreAlumno +" .docx")

def limpiarDirectorios():
    directorios = ['','/resultado/ConveniosIndividuales/','/resultado/ConveniosMarco/','/resultado/Diplomas/']
    for direc in directorios:
        folder = os.path.join(settings.MEDIA_ROOT + direc)
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(e)
