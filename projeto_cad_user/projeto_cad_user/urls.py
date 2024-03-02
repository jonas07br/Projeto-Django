
from django.urls import path
from app_cad import views
urlpatterns = [
    path('',views.index,name='home'),
]
