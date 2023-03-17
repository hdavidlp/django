from django.shortcuts import render
from django.http import HttpResponse
from .models import User
# Create your views here.


def inicio(request):
    return render(request, 'paginas/inicio.html' )

def nosotros(request):
    return render(request, 'paginas/nosotros.html' )

def users(request):
    all_users  = User.objects.all()
    return render(request, 'users/index.html', {
        'users': all_users}
    )

def createUser(request):
    return render(request, 'users/create.html')

def editUser(request):
    return render(request, 'users/edit.html')
    

