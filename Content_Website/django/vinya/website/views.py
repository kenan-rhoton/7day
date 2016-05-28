from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return HttpResponse("Mah title. Mah content.")
