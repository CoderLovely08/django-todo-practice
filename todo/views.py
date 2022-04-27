from django.shortcuts import render

def index(request):
    return render(request,'todo/home.html')

def portfolio(request):
    return render(request,'todo/portfolio.html')

def contact(request):
    return render(request,'todo/contact.html')