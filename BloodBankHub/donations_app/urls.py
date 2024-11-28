from django.urls import path
from . import views

app_name = "donations_app"

urlpatterns = [
    path('', views.blood_bank_view, name='blood_bank_view'),
    path('donate/', views.donate_info_view, name='donate_info_view'),
]