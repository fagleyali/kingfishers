from django.shortcuts import render
from .models import Kingfisher

from django.http import HttpResponse


# Create your views here.



def home(request):
    return HttpResponse("<h1> Welcome to the Kingfishers' world </h1>" )

def about(request):
    return render(request,'about.html')

def kingfisher_index(request):
    kingfishers = Kingfisher.objects.all()
    return render(request,'kingfishers/index.html',{'kingfishers':kingfishers})

def kingfishers_detail(request,kingfisher_id):
    kingfisher = Kingfisher.objects.get(id=kingfisher_id)
    return render(request,'kingfishers/detail.html',{'kingfisher': kingfisher})