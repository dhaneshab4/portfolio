from django.urls import path
from .views import portfolio_list, user_logout, add_project, add_education

urlpatterns = [
    path('portfolio/', portfolio_list, name='portfolio_list'),
    path('logout/', user_logout, name='logout'),
    path('add_project/', add_project, name='add_project'),
    path('add_education/', add_education, name='add_education'),
]
