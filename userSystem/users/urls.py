from django.urls import path
from . import views


# path( direccion solitada,  accion de views, nombre para la aplicacion)
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('users', views.users, name='users'),
    path('users/create', views.createUser, name='createUser'),
    path('users/edit', views.editUser, name='editUser'),
]

