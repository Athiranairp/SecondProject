from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def add(request):
    return render(request,'add.html')
def addition(request):
    n1=int(request.GET['num1'])
    n2=int(request.GET['num2'])
    res=n1+n2
    res1=n1*n2
    res2=n1/n2
    res3=n1-n2
    return render(request,'result.html',{'result':res,'result1':res1,'result2':res2,'result3':res3})