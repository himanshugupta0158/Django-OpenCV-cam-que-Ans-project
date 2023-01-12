from django.urls import path
from .views import demo, CamOn

urlpatterns = [
    path('', demo),
    path('camOn', CamOn, name="camOn"),
]
