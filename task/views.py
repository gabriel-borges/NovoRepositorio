from django.shortcuts import render

from django.http import HttpResponse

class Tarefa(object):

    def __init__(self, titulo, data):
        self.titulo = titulo
        self.data = data

    def __str__(self):
        return self.titulo

def home(request):
    return HttpResponse("Olá, mundo")

def sobre(request):
    return HttpResponse("Esta é a página com informações sobre o projeto")

#   def tarefa(request, numero):
#       return HttpResponse("Tarefa: " + str(numero))

#   def tarefa(request, ano):
#       return HttpResponse("Tarefa: " + str(ano))

def tarefa(request, ano, mes, dia):
    return HttpResponse("Tarefa: " + str(dia) + "/" + str(mes) + "/" + str(ano))
