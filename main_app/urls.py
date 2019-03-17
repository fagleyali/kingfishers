from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('kingfishers/',views.kingfisher_index,name='index'),
    path('kingfishers/<int:kingfisher_id>/',views.kingfishers_detail,name='detail'),
    path('kingfishers/create/',views.KingfisherCreate.as_view(),name='kingfishers_create'),
    path('kingfishers/<int:pk>/update/', views.KingfisherUpdate.as_view(),name='kingfishers_update'),
    path('kingfishers/<int:pk>/delete/', views.KingfisherDelete.as_view(),name='kingfishers_delete'),
    path('kingfishers/<int:kingfisher_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('locations/', views.LocationList.as_view(),name='locations_index'),
    path('locations/<int:pk>/', views.LocationDetail.as_view(),name='locations_detail'),
    path('locations/create/', views.LocationCreate.as_view(),name='locations_create'),
    path('locations/<int:pk>/update/',views.LocationUpdate.as_view(),name='locations_update'),
    path('locations/<int:pk>/delete/',views.LocationDelete.as_view(),name='locations_delete'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/signup',views.signup,name='signup'),


]
