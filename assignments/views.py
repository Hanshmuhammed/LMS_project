from django.shortcuts import render

# Create your views here.
def assignment_page(request):
    return render(request,'assignment.html')