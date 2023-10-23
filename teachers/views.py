from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse("Welcome to emobilis")

def about(request):
    return HttpResponse("about emobilis")

def services(request):
    return HttpResponse("Our services")