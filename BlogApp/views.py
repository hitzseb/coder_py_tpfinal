from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('home')

def post(request):
    return HttpResponse('post')

def category(request):
    return HttpResponse('category')

def author(request):
    return HttpResponse('author')
