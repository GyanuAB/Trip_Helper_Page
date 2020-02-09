from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html',{'name':'akhil'})
    
def add(request):
    var1 = int(request.POST['num1'])
    var2 = int(request.POST['num2'])
    res = var1 + var2 
    return render(request, 'result.html',{'result':res} )