from django.shortcuts import render


# Create your views here.
def home(request):
    context = {}
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")

def contact(request):
    context = {}
    return render(request,"contact.html",context)

