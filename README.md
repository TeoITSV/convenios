
# 📜 Generador de Convenios ITSV🖋️✨

  

Estimados usuarios 👥👥,

Este sistema es una herramienta 🛠️ para la confección de convenios⚖ específicos del ITS Villada👨‍🏫. Desarrollado👨‍💻 en el robusto🦾 marco de Django🎶 en python 3.7🐍, permite completar plantillas de convenios de manera automatizada🤖 y generar archivos PDF individuales 📜🖨️ para cada alumno👨‍🎓.

## 🛠️ Proceso de Instalación y Configuración

Vamos a sumergirnos en los detalles de la instalación, paso a paso:

  

1.  **📋Clonar el Repositorio**:

  

Para comenzar, clonen este repositorio en sus entornos locales con el siguiente comando 👇:

```bash
git clone urlDelRepo
```

1.  **💼Configuración del Entorno:**

Es crucial crear un entorno virtual utilizando Python 3.7 (¡sin excepciones!) para luego instalar las dependencias necesarias con pip:

```bash
pip install  -r  requirements.txt
```

3.  **🚀Lanzar el Proyecto:**

Una vez que estén todas las dependencias en su lugar, inicien el proyecto con este comando mágico ✨:

```bash
python manage.py  runserver
```

  

El proyecto se levantará en localhost:8000🌍. Ahora, el próximo paso es cargar las plantillas de convenios en formato 📎DOCX, junto con los archivos 📊Excel que contienen los datos de los estudiantes y las empresas.

## 📂 Utilizando el Generador

 
Ahora, aprendamos cómo generar los convenios con facilidad:

1.  **📑Plantillas y Datos:**

Antes que nada, asegúrense de que las plantillas de convenios contengan las 🗝"keys" de autocompletado en el formato **{{key}}**. Además, el archivo Excel debe tener información de los estudiantes y las empresas, y los nombres de las "keys" deben estar en la primera fila.

  

2.  **📈Generación Individual o Masiva:**

¡Es hora de la acción! El Generador les permite generar convenios de uno en uno o en masa. Los convenios generados se descargarán en un archivo comprimido que seguirá esta estructura de directorios🌳:


```markdown
	.
	└── resultado
		├── ConveniosIndividuales
		├── ConveniosMarco
		└── Diplomas
```
  

## 📎 Archivos Adjuntos para su Comodidad

  
Para facilitarles el proceso, hemos adjuntado en la carpeta 🧱Static las plantillas necesarias y un archivo excel de prueba en este repositorio. Estos recursos les permitirán verificar✍ y asegurarse de que el proyecto funciona sin problemas🥳.

  

## 🌐Referencias Utiles

- Instalacion de virtualENV
	- [Python documentation venv](https://docs.python.org/3/library/venv.html)
	- [Pyenv ](https://github.com/pyenv/pyenv)
		Gestor de versiones de python, util para instalar python 3.7🐍
	- [Cambiar python a 3.7 ](https://tellor.io/blog/how-to-install-python-3-9-and-venv-on-ubuntu/)
		Pueden usar esta opcion si no pueden instalar pyenv/no funciona
	

