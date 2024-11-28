from django.urls import path
from . import views

app_name = "main_app"

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('contact/', views.contact_us_view, name='contact_us_view'),
]
