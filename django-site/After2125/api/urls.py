from django.urls import path

from . import views



urlpatterns = [
    path('index/', views.index, name='index' ),
    path('Menus/', views.MenusView, name='Menus' ),
]
