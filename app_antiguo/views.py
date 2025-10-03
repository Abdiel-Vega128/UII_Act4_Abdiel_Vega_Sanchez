from django.shortcuts import render

# Create your views here.
def index(request):
    antiguedades = [
        {"nombre": "Jarrón Ming", "año": "1644"},
        {"nombre": "Reloj de bolsillo victoriano", "año": "1890"},
        {"nombre": "Máquina de escribir antigua", "año": "1920"},
    ]
    contexto = {'antiguedades': antiguedades}
    return render(request, 'index.html', contexto)
