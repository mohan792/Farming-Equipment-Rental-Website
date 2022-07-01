from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.basepage, name='basepage'),
    path('loginpage',views.loginpage, name='loginpage'),
    path('handellogin',views.handellogin, name='handellogin'),
    path('registerpage',views.registerpage, name='registerpage'),
    path('handleregister',views.handleregister, name='handleregister'),
    path('equipmentholderpage',views.equipmentholderpage, name='equipmentholderpage'),
    path('addequipment',views.addequipment, name='addequipment'),
    path('add',views.add, name='add'),
    path('handleLogout',views.handleLogout, name='handleLogout'),
    path('deleteequipment',views.deleteequipment, name='deleteequipment'),
    path('delete/<str:slug>',views.delete, name='delete'),
    path('applicantpage',views.applicantpage, name='applicantpage'),
    path('requests',views.requests, name='requests'),
    path('apply/<str:slug>',views.apply, name='apply'),
    path('denied_request/<str:slug>',views.denied_request, name='denied_request'),
    path('accept_request/<str:slug>',views.accept_request,name='accept_request'),
]