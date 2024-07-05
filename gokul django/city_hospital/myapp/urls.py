from django.urls import path
from myapp import views
from django.contrib import admin

urlpatterns = [
    path('base/', views.base, name='base'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('booking/', views.booking, name='booking'),
    path('doctor/', views.doctors, name='doctor'),
    path('appoinment/',views.appoinment, name='appoinment'),
    path('department/', views.department, name='department'),
    path('contact/', views.contact, name='contact'),
    # path('book/', views.book_appointment, name='book_appointment'),
]

