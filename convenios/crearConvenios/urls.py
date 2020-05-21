from django.conf.urls import url
from . import views

app_name="crearConvenios"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^generar', views.generar, name='generar'),
    url(r'^ayuda', views.ayuda, name='ayuda'),
    url(r'^descargar/(?P<plantilla>[\w-]+)', views.descargarPlanillas, name='descargar'),
]