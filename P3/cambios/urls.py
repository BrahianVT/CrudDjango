from django.conf.urls import url
from .views import( Actualiza,Agregar,Lista,Detalle,Borrar)
# urls de vista genericas

urlpatterns = [
    url(r'^$', Lista.as_view(), name='lista'),
    url(r'^(?P<pk>\d+)$' , Detalle.as_view(), name='detalle'),
    url(r'^modificar/(?P<pk>\d+)$', Actualiza.as_view() , name='modificar'),
    url(r'^borrar/(?P<pk>\d+)$' , Borrar.as_view(), name='borrar'),
    url(r'^agregar$' , Agregar.as_view(), name='agregar'),
]