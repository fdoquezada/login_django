from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html', {'message': '¡Bienvenido al Proyecto Educativo!'})