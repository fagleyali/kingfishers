from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Kingfisher
from .forms import FeedingForm

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
    feeding_form=FeedingForm()
    return render(request,'kingfishers/detail.html',{'kingfisher': kingfisher,'feeding_form':feeding_form})

class KingfisherCreate(CreateView):
    model = Kingfisher
    fields = '__all__'

class KingfisherUpdate(UpdateView):
    model = Kingfisher
    fields = ['breed','diet','description','age']

class KingfisherDelete(DeleteView):
    model = Kingfisher
    success_url = '/kingfishers/'

def add_feeding(request, kingfisher_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding=form.save(commit=False)
    new_feeding.kingfisher_id=kingfisher_id
    new_feeding.save()
  return redirect('detail',kingfisher_id=kingfisher_id)