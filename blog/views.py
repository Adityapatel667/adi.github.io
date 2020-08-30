from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bloghome(request):

    #return HttpResponse('homepage')
    return render(request , "blog/blog.html")
def blogpost (request ):
    #return HttpResponse(f'blogpost: {slug}')  
    return render(request , "blog/blogpost.html")
   # return HttpResponse("blogpost")
def test(request):
       return HttpResponse('test html')