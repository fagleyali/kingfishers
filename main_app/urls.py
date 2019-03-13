from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('kingfishers/',views.kingfisher_index,name='index'),
    path('kingfishers/<int:kingfisher_id>/',views.kingfishers_detail,name='detail'),
    path('kingfishers/create/',views.KingfisherCreate.as_view(),name='kingfishers_create'),
    path('kingfishers/<int:pk>/update/', views.KingfisherUpdate.as_view(),name='kingfishers_update'),
    path('kingfishers/<int:pk>/delete/', views.KingfisherDelete.as_view(),name='kingfishers_delete'),
    path('kingfishers/<int:kingfisher_id>/add_feeding/', views.add_feeding, name='add_feeding')

]
