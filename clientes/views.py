from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente, Tratamento
import re

def clientes(request):
    if request.method == "GET":
       return render(request,  'clientes.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        tratamentos =request.POST.getlist('tratamento')
        triagens =request.POST.getlist('triagem')
        idades =request.POST.getlist('idade')

        cliente = Cliente.objects.filter(cpf=cpf)

        if cliente.exists():
            return HttpResponse('Cliente já existe')

        if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
         return HttpResponse('Email inválido')
         cliente = Cliente(
           nome =  nome,
           sobrenome = sobrenome,
           email = email,
           cpf = cpf,
        )

        cliente.save()

        for tratamento, triagem, idade in zip(tratamentos, triagens, idades):
            tratar = tratamento(tratamento=tratamento, triagem=triagem, idade=idade, cliente=cliente)
            tratar.save()


        return HttpResponse('teste')
