from django.http import HttpResponse
from django.shortcuts import render

def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>") # string of HTML
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Contact Page</h1>") # string of HTML
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
   my_context = {
       "title": "this is about us",
       "my_number": 123,
       "my_list": [123,456,789, "ABC"],
       "my_html": "<h1>Hello World</h1>"
   }
   return render(request, "about.html", my_context)

def social_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Social Page</h1>") # string of HTML
    return render(request, "social.html", {})