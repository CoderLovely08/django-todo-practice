import imp
from django.shortcuts import render
from .models import Student

def index(request):
    return render(request,'todo/home.html')

def portfolio(request):
    return render(request,'todo/portfolio.html')

def contact(request):
    print(request.method)
    if request.method=='POST':
        print(request.POST.get('first_name'))
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        student_age=request.POST.get('student_age')

        query = Student(first_name=first_name,last_name=last_name,student_age=student_age)
        query.save()

        return render(request,'todo/contact.html')
    else: print('ahhh')
    return render(request,'todo/contact.html')