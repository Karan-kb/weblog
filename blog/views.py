from django.http import HttpResponse
from django.shortcuts import render

def aboutUs(request):
    return render(request,"about.html")

def course(request):
    task={
      'top':'Django',
      
    }
    return render(request,"course.html",task)


def homePage(request):
    data={
        'title':'Home Page',
        'b':'Welcome to the blog.',
        'clist':['Python','PHP','Java'],
        'numbers':[10,20,30,40,50],
        'student_details':[
            {'name':'ram' , 'phone':'9845632587'},
            {'name':'hari', 'phone':'9848524175'}
        ]
    }
    return render(request,"index.html",data)

def courseDetails(request,courseid):
    return HttpResponse(courseid)


