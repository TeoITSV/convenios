# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import StreamingHttpResponse, Http404
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from wsgiref.util import FileWrapper
from .static.code.codigo import correrAplicacion, limpiarDirectorios
import mimetypes
import os, shutil


def index(request):
    try:
        return render(request, 'index.html')
    except Exception as e:
        raise Http404("No se encuentra index: " + e)

def generar(request):  #si no paso todos los documentos da error!
    try:
        if request.method == 'POST':
            limpiarDirectorios()
            documentos = ''
            if(request.POST.get('hojaDatosText')!=''):
                hojaDatos = request.FILES['hojaDatos']
                path = default_storage.save('hojaDatos.xlsx', ContentFile(hojaDatos.read()))
                tmp_file = os.path.join(settings.MEDIA_ROOT,path)
            if(request.POST.get('plantillaIndividualesText')!=''):
                plantillaIndividuales = request.FILES['plantillaIndividuales']
                path = default_storage.save('plantillaIndividuales.docx', ContentFile(plantillaIndividuales.read()))
                tmp_file = os.path.join(settings.MEDIA_ROOT,path)
                documentos = documentos + 'a'
            if(request.POST.get('plantillaMarcoText')!=''):
                plantillaMarco = request.FILES['plantillaMarco']
                path = default_storage.save('plantillaMarco.docx', ContentFile(plantillaMarco.read()))
                tmp_file = os.path.join(settings.MEDIA_ROOT,path)
                documentos = documentos + 'b'
            if(request.POST.get('plantillaDiplomasText')!=''):
                plantillaDiplomas = request.FILES['plantillaDiplomas']
                path = default_storage.save('plantillaDiplomas.docx', ContentFile(plantillaDiplomas.read()))
                tmp_file = os.path.join(settings.MEDIA_ROOT,path)
                documentos = documentos + 'c'
        generarConvenios = False
        if(correrAplicacion(documentos) == True):
            shutil.make_archive(settings.MEDIA_ROOT + 'resultado', 'zip', settings.MEDIA_ROOT +'/resultado/')
            generarConvenios = True
        the_file = settings.BASE_DIR + '/crearConvenios/media/resultado.zip'
        filename = os.path.basename(the_file)
        response = StreamingHttpResponse(FileWrapper(open(the_file, 'rb')),
                           content_type=mimetypes.guess_type(the_file)[0])
        response['Content-Length'] = os.path.getsize(the_file)
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        limpiarDirectorios()
        return response
    except Exception as e:  
        if (generarConvenios == False):
            generarConvenios = "La planilla que contiene los datos es erronea."
        return render(request, 'error.html',{'error':e,'generarConvenios':generarConvenios})

def ayuda(request):
    return render(request, 'ayuda.html')


def descargarPlanillas(request,plantilla):
    if(plantilla == 'datos'):
        the_file = settings.BASE_DIR + '/crearConvenios/static/plantillas/Datos.xlsx'
    elif(plantilla == 'diplomas'):
        the_file = settings.BASE_DIR + '/crearConvenios/static/plantillas/PlantillaDiplomas.docx'
    elif(plantilla == 'individual'):
        the_file = settings.BASE_DIR + '/crearConvenios/static/plantillas/PlantillaIndividual.docx'
    elif(plantilla=='marco'):
        the_file = settings.BASE_DIR + '/crearConvenios/static/plantillas/PlantillaMarco.docx'
    filename = os.path.basename(the_file)
    response = StreamingHttpResponse(FileWrapper(open(the_file, 'rb')),
                       content_type=mimetypes.guess_type(the_file)[0])
    response['Content-Length'] = os.path.getsize(the_file)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
