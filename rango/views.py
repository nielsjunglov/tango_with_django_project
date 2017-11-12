from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Rango siger velkommen i skuret<br><a href='/rango/about'>about</a><br><a href='/rango/contact'>contact</a>")
	
def about(request):
	return HttpResponse("Rango siger velkommen til About-siden<br><a href='/rango'>rango index</a><br><a href='/rango/contact'>contact</a>")

def contact(request):
	return HttpResponse("Rango siger velkommen til contact-siden<br><a href='/rango'>rango index</a><br><a href='/rango/about'>about</a>")