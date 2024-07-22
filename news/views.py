from django.shortcuts import render
from .models import News
# Create your views here.
def index(request):
    news=News.objects.all()
    return render(request,'index.html',{"news":news})

def category(req):
    return render (req, 'category.html')

def contact(req):
    return render(req, 'contact.html')

def single(req, id):
    data=News.objects.get(id=id)
    return render (req, 'single.html',{'data':data})
