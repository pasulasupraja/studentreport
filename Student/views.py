from django.shortcuts import render

from report.models import Student


def home(request):
    students=Student.objects.all()
    context={
        'students':students,
    }
    return render(request,'home.html',context)