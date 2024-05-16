from django.http  import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Hello, World. You are at in world of Raso Home Page")
    return render(request, 'website/index.html')
    

def about(request):
    return HttpResponse("Hello, World. You are at in world of Raso About Page")

def contact(request):
    return HttpResponse("Hello, World. You are at in world of Contact Page")