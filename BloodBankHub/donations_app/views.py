from django.shortcuts import render

def donate_info_view(request):
    return render(request, 'donations_app/donate_info.html')

def blood_bank_view(request):
    # Logic to fetch and display blood donations
    return render(request, 'donations_app/blood_bank.html')