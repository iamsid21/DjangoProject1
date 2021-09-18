from typing import ContextManager
from django.http.response import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):

    # here we do , fetch data fro database then turn it into variable then send to template
    context = {  # set of variable we send to template
        "variable1" : "this is variable 01 send from views to html",
        "variable2" : "this is variable 02 send from views to html" 
    }
    return render(request,'index.html',context)
    # return HttpResponse("this is homepage") #strings can be rendered using httpresponse

def about(request):
    return render(request,'about.htm')
    
def services(request):
    return render(request,'services.htm')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent')
    return render(request,'contact.htm')