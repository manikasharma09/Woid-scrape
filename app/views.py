from django.shortcuts import render
from .bs import *

def home(request):
	p=[]
	m=[]
	p=func()
	m=func1()
	return render(request,'app/home.html', {'p':p,'m':m})
