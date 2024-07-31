from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("services", views.services, name="services"),
    path("contact", views.contact, name="contact"),
    path("addstylist/", views.addstylist, name="addstylist"),
    path("appointment/", views.appointment, name="appointment"),
    path("voucher/", views.voucher, name="voucher"),
    path("bookappointment/", views.bookappointment, name="bookappointment"),

    path('appointment/delete/<int:id>', views.delete, name='delete'),

    path('adminToAddStylist', views.adminToAddStylist, name='adminToAddStylist'),
     # try for admin page 1
    path('adminToAddStylist', views.adminToAddStylist, name='adminToAddStylist'), # try for admin page 2

    path('adminToAddStylist', views.adminToAddStylist, name='adminToAddStylist'), # try for admin page 3

    path('sendemail', views.sendemail, name="sendemail"),
    path('admincontact/', views.admincontact, name="admincontact"),
]