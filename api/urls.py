
from django.urls import path

from api import views

app_name = 'todos'

urlpatterns = [
    path('todo/<int:pk>/', views.ToggleToDo.as_view(), name='toggle'),
]
