from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('kingfishers/',views.kingfisher_index,name='index'),
    path('kingfishers/<int:kingfisher_id>/',views.kingfishers_detail,name='detail')
]