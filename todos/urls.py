
from django.urls import path
from todos import views

app_name = 'todos'

urlpatterns = [
    path('', views.ListToDos.as_view(), name='list'),
    path('active/', views.ListActiveToDos.as_view(), name='list-active'),
    path('completed/', views.ListCompletedToDos.as_view(), name='list-completed'),

    path('create/', views.CreateToDo.as_view(), name='create'),
    path('<int:pk>/complete/', views.CompleteToDo.as_view(), name='complete'),
    path('<int:pk>/delete/', views.DeleteToDo.as_view(), name='delete'),
    path('<int:pk>/update/', views.UpdateToDo.as_view(), name='update'),

    path('clear-completed/', views.ClearCompletedToDos.as_view(), name='clear-completed'),
    path('toggle-all/', views.ToggleAllToDos.as_view(), name='toggle-all'),
]
