from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    text = "Bu mening django loyiham"
    return HttpResponse(text)
