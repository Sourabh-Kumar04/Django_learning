
from django.urls import path
from . import views

# localhost:8000/raso
# localhost:8000/raso/order
urlpatterns = [
    path('', views.all_raso, name='all_raso'),
]