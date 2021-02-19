from django.urls import path

from .views import create_employee, get_employee, search_employee

urlpatterns = [
    path('create/emp_dashboard/', create_employee, name='create_employee'),
    path('get_employee/', get_employee, name='get_employee'),
    path('search_employee/', search_employee, name='search_employee'),
]