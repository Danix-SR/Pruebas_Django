from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse

def Index (request):
    return render(request,"Index.html")