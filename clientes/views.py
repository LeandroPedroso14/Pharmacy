from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente, Tratamento

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
