from django.shortcuts import render

# Create your views here.

def h1(request):
    d={'name':'madhu'}
    return render(request,'h1.html',d)