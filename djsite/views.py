from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return render(request, 'hello.html')

def articles(request, year):
    return render(request, 'articles.html', {'v_idade': year})

def site(request):
    return render(request, 'index.html')
