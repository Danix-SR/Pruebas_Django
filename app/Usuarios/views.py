from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse

class Usuario(object):
    def __init__(self,Id,Nombre,Apellido):
        self.Id = Id
        self.Nombre = Nombre
        self.Apellido = Apellido
Lista_User = []
for cnt in range(0, 5):
    Lista_User.append(Usuario(str(cnt),"Nombre"+str(cnt),"Apellido"+str(cnt)))

def Index (request):
    return render(request,"Usuarios/Index.html",{"Lista_User":Lista_User})

def CrearUsuario (request):
    #Sin comillas 
    Llegada =("Id=%s  Nombre=%s  Apellido=%s ") %(request.GET["Id"],request.GET["Nombre"],request.GET["Apellido"])
    
    #Con comillas porque es string %r porque es una variable tipo render 
    #Llegada =("Id=%r  Nombre=%r  Apellido=%r ") %(request.GET["Id"],request.GET["Nombre"],request.GET["Apellido"])
    
    #Como llega del render 
    #Llegada = request.GET["Id"]+request.GET["Nombre"]+request.GET["Apellido"]
    return HttpResponse (Llegada)