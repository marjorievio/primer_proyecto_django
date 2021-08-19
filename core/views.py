from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

# Create your views here.

def root(request):
	return redirect("/blogs") 

def index(request):
    return HttpResponse("<h1>placeholder para luego mostrar una lista de todos los blogs</h1>")

def new(request):
    return HttpResponse("placeholder para mostrar un nuevo formulario para crear un nuevo blog")

def create(request):
    return redirect("/")

def show(request, number):
    return HttpResponse(f"placeholder para mostrar el blog numero: {number}")

def edit(request, number):
    return HttpResponse(f"placeholder para editar el blog {number}")

def destroy(request, number):
    return redirect("/blogs")

def json(request):
    return JsonResponse({
        'titulo':'placeholder para mostrar un json',
        'nombre':'Marjorie',
        'apellido':'Vio',
        'curso':'Full Stack Python'
    })