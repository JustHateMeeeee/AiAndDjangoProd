from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.mainList),
    path('videoCards', views.videoCards),
    path('ssdHdd', views.ssdHdd),
    path('ram', views.ram),
    path('core', views.core),
    path('power', views.power),
    path('cooler', views.cooler),
]