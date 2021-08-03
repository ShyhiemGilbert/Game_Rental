from django.urls import path
from . import views # . means in current directory

urlpatterns = [
    path('',views.index, name='index')
]
