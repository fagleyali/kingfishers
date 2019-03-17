from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView,DetailView
from .models import Kingfisher, Location
from .forms import FeedingForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from django.http import HttpResponse


# Create your views here.



def home(request):
    return HttpResponse("<h1> Welcome to the Kingfishers' world </h1>" )

def about(request):
    return render(request,'about.html')

@login_required
def kingfisher_index(request):
    kingfishers = Kingfisher.objects.filter(user=request.user)
    return render(request,'kingfishers/index.html',{'kingfishers':kingfishers})

@login_required
def kingfishers_detail(request,kingfisher_id):
    kingfisher = Kingfisher.objects.get(id=kingfisher_id)
    feeding_form=FeedingForm()
    locations_kf_doesnot_have=Location.objects.exclude(id__in=kingfisher.location.all().values_list('id'))
    return render(request,'kingfishers/detail.html',{
      'kingfisher': kingfisher,
      'feeding_form':feeding_form,
      'locations': locations_kf_doesnot_have
      
      })

class KingfisherCreate(LoginRequiredMixin,CreateView):
    model = Kingfisher
    fields = ['name','breed','diet','description','age']

    def form_valid(self, form):
          form.instance.user=self.request.user
          return super().form_valid(form)


class KingfisherUpdate(LoginRequiredMixin,UpdateView):
    model = Kingfisher
    fields = ['breed','diet','description','age']


class KingfisherDelete(LoginRequiredMixin,DeleteView):
    model = Kingfisher
    success_url = '/kingfishers/'

@login_required
def add_feeding(request, kingfisher_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding=form.save(commit=False)
    new_feeding.kingfisher_id=kingfisher_id
    new_feeding.save()
  return redirect('detail',kingfisher_id=kingfisher_id)


class LocationList(LoginRequiredMixin,ListView):
  model = Location


class LocationDetail(LoginRequiredMixin,DetailView):
  model = Location


class LocationCreate(LoginRequiredMixin,CreateView):
  model = Location
  fields = '__all__'


class LocationUpdate(LoginRequiredMixin,UpdateView):
  model = Location
  fields = ['where']


class LocationDelete(LoginRequiredMixin,DeleteView):
  model = Location
  success_url = '/locations/'


def signup(request):
      error_message=''
      if request.method=='POST':
            form=UserCreationForm(request.POST)
            if form.is_valid():
                  user=form.save()
                  login(request,user)
                  return redirect('index')
            else:
                  error_message='Invalid credentials. Try agin'
      form=UserCreationForm()
      context={'form':form,'error_message':error_message}
      return render(request,'registration/signup.html',context)

