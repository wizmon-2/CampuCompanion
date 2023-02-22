from django.urls import path
from . import views

urlpatterns = [
    path('createtodo/', views.CreateTodo.as_view(), name='todo')
]