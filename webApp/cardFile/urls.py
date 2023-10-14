from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.mainList),
    path('videoCards', views.videoCards, name='videoCards'),
    path('ssdHdd', views.ssdHdd, name='ssdHdd'),
    path('ram', views.ram, name='ram'),
    path('core', views.core, name='core'),
    path('power', views.power, name='power'),
    path('cooler', views.cooler, name='cooler'),
]