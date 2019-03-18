from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView,DetailView
import uuid
import boto3
from .models import Kingfisher, Location, Photo
from .forms import FeedingForm

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

S3_BASE_URL = 'https://s3-us-west-2.amazonaws.com/'
BUCKET = 'kingfisherali'



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
    print(locations_kf_doesnot_have)
    return render(request,'kingfishers/detail.html',{
      'kingfisher': kingfisher,
      'feeding_form':feeding_form,
      'location': locations_kf_doesnot_have
      
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

@login_required
def add_photo(request, kingfisher_id):
    	# photo-file was the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            print(url)
            # we can assign to cat_id or cat (if you have a cat object
            photo = Photo(url=url, Kingfisher_id=kingfisher_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', kingfisher_id=kingfisher_id)

@login_required
def assoc_location(request,kingfisher_id,location_id):
      
      Kingfisher.objects.get(id=kingfisher_id).location.add(location_id)
      
      return redirect('detail',kingfisher_id=kingfisher_id)
      print(kingfisher_id)




