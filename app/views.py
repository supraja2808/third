from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def string_response(request):
    return HttpResponse('This is my first string')

def second_response(request):
    return HttpResponse('This is my second string')

def third_response(request):
    return HttpResponse('This is my third string')
