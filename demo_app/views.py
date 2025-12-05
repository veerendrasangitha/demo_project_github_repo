from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_page(request):
    # return HttpResponse("THIS IS HOME PAGE")
    return render(request,"home.html")
def about_page(req):
    # return HttpResponse("THIS IS ABOUT PAGE")
    return render(req,"about.html")
def contact_page(req):
    # return HttpResponse("THIS IS CONTACT PAGE")
    return render(req,"contact.html")
