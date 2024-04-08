from .import views
from django.urls import path
from .views import add

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.view_student, name='view_student'),
    path('add/', add, name='add'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('students/<int:id>/delete/', views.delete_student, name='delete_student'),
    
    
]