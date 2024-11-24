from django.shortcuts import render

# Create your views here.
def index_page(request):
    return render(request,'index.html')

def about_page(request):
    return render(request,'about.html')

def course_page(request):
    return render(request,'course.html')


def xstudents_page(request):
    return render(request,'xstudents.html')