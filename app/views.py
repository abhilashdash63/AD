from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def string_response(request):
    return HttpResponse('<h1>this is my first string</h1>')
def string_response2(request):
    return HttpResponse('this is my second string')


