from django.shortcuts import render

def home_view(request):
    return render(request, 'main_app/home.html')

def contact_us_view(request):
    return render(request, 'main_app/contact_us.html')
