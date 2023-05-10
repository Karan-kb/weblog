from django.http import HttpResponse
from django.shortcuts import render

def aboutUs(request):
    return render(request,"aboutus.html")

def course(request):
    task={
      'top':'Django',
      
    }
    return render(request,"course.html",task)


def homePage(request):
    data={
        'title':'Home Page',
        'b':'Welcome to the blog.',
        'clist':['Python','PHP','Java']
    }
    return render(request,"index.html",data)

def courseDetails(request,courseid):
    return HttpResponse(courseid)


