from django.shortcuts import render
from . models import Contact

# Create your views here.
def contact(request):
   if request.method == "POST":
       print(request.POST)
       name = request.POST.get('name')
       email = request.POST.get('email')
       subject = request.POST.get('subject')
       message = request.POST.get('message')

       contact_entry = Contact(name=name, email=email, subject=subject, message=message)
       contact_entry.save()
       
        
        
   return render(request,'contact.html')