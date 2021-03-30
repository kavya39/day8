from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
	return HttpResponse("<h1 style='color:blue;background-color:green;text-align:center'>welcome to home page</h1>")

def chk(request):
	return HttpResponse("<script> alert('hello gm')</script> <h2> welcome </h2>")

def home(request):
	return render(request,'kr/home.html')

def lgn(re):
	return render(re,'kr/login.html')

def reg(rt):
	return render(rt,'kr/register.html')


