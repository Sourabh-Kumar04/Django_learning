from django.shortcuts import render

# Create your views here.
def all_raso(request) :
    return render(request, 'raso/all_raso.html')