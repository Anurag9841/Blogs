from django.shortcuts import render
from .models import posts
# Create your views here.
def index(request):
    post = posts.objects.all()
    return render(request,'index.html',{'posts':post})

def post(request,title):
    post = posts.objects.get(title=title)
    return render(request,'post.html',{'posts':post})
