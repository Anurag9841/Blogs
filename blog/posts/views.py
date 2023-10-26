from django.shortcuts import render
from .models import posts
# Create your views here.
def index(request):
    post = posts.objects.all()
    return render(request,'index.html',{'posts':post})
