from django.urls import path
from .views import collect
urlpatterns = [
    path('collect/', collect, name='collect'),
]