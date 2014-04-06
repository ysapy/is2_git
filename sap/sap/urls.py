from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sap.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    #autenticacion
    url(r'^', include('aplicaciones.autenticacion.urls')), #incluimos la urls.py de la aplicacion autenticacion
	#url(r'^usuario', include('aplicaciones.usuarios.urls')), #
)
