from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    print(request.method)
    return render(request,'form.html')

def login(request):
    return render(request,'login.html')