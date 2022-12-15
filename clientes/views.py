from django.shortcuts import render
from django.http import HttpResponse

def clientes(request):
    if request.method == "GET":
       return render(request,  'clientes.html')
    elif request.method == "POST":
        nome = request.POST.get()
