from django.shortcuts import render
from .models import RasoVarity
from django.shortcuts import get_object_or_404

# Create your views here.
def all_raso(request) :
    rasos = RasoVarity.objects.all()
    return render(request, 'raso/all_raso.html', {'rasos': rasos})

def raso_detail(request, raso_id):
    raso = get_object_or_404(RasoVarity, pk=raso_id)
    return render(request, 'raso/raso_detail.html', {'raso': raso})