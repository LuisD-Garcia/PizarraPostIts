from django.urls import path
from . import views


urlpatterns = [

    path(
        'login/',
        views.login_view,
        name='login'
    ),

    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),

    path(
        'perfil/',
        views.perfil,
        name='perfil'
    ),

    path(
        '',
        views.pizarra,
        name='pizarra'
    ),

    path(
        'completados/',
        views.completados,
        name='completados'
    ),

    path(
        'crear/',
        views.crear,
        name='crear'
    ),

    path(
        'detalle/<int:id>/',
        views.detalle,
        name='detalle'
    ),

    path(
        'editar/<int:id>/',
        views.editar,
        name='editar'
    ),

    path(
        'completar/<int:id>/',
        views.completar,
        name='completar'
    ),

    path(
        'eliminar/<int:id>/',
        views.eliminar,
        name='eliminar'
    ),

]