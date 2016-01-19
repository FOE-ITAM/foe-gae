from django.conf.urls import *
from views import *
from django.conf import settings

if settings.IS_PROD:
    urlpatterns = patterns(
        '',

        # main site
        url(r'^$', index, name='index'),

        # RegistroOE
        url(r'^registro-oe/$', registro_oe, name='registro_oe'),
        url(r'^registro-comite/$', registro_comite, name='registro_comite'),
        url(r'^registro-miembro/$', miembros_oe, name='registro_miembro'),
        url(r'^registro-bancario/$', datos_bancarios, name='registro_bancario'),
        url(r'^directorio/$', directorio, name='directorio'),
        url(r'^directorio/(?P<oe_slug>[\w-]+)/$', perfil_oe, name='perfil_oe'),
        url(r'^view_file/([^/]+)?', ViewFileHandler, name='view_file'),
    )

else:
    urlpatterns = patterns(
        '',

        # main site
        url(r'^$', index, name='index'),

        # RegistroOE
        url(r'^registro-oe/$', registro_oe, name='registro_oe'),
        url(r'^registro-comite/$', registro_comite, name='registro_comite'),
        url(r'^registro-miembro/$', miembros_oe, name='registro_miembro'),
        url(r'^registro-bancario/$', datos_bancarios, name='registro_bancario'),
        url(r'^directorio/$', directorio, name='directorio'),
        url(r'^directorio/(?P<oe_slug>[\w-]+)/$', perfil_oe, name='perfil_oe'),
    )
