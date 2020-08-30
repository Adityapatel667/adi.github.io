from django.shortcuts import render
from django.http import HttpResponse
from home.models import Contact
# Create your views here.
def home(request):
    #return HttpResponse("home homepage")
    return render (request , "home/home.html")
def resume(request):
    #return HttpResponse("home homepage")
    return render (request , "home/resume.html")
def about(request):
    #return HttpResponse('about page')
    return render(request , "home/about.html")
def contact (request):
    #return HttpResponse('contact page')
    if request.method=='POST':
        name= request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        phone=request.POST['phone']
        contact=Contact(name=name,email=email,message=message,phone=phone)
        
    return render (request , "home/contact.html")
def blogpost (request):
    return render(request, "home/blogpost.html")