from django.urls import path
from . import views  # Import your views

urlpatterns = [
    path('', views.index_view, name='home'),  # Home page
    path('contact/', views.contact_view, name='contact'),
]