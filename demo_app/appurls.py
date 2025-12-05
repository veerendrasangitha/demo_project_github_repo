from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    # path("",views.home_page)
    path("",views.empty_page),
    path("home/",views.home_page),
    path("about/",views.about_page),
    path("contact/",views.contact_page)
]
