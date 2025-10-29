from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Hello, welcome to the home page!")

def about_view(request):
    return HttpResponse("This is the about page.")

def contact_view(a):
    return HttpResponse("kantakt")

def login_view(request):
    return HttpResponse("Login page")

def register_view(request):
    return HttpResponse("Register page")
def profile_view(request):  
    return HttpResponse("Profile page")