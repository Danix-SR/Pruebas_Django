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
    return render(request,"layout.html",{"Lista_User":Lista_User})