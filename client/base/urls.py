from django.urls import path
from django.views.generic import TemplateView
from .views import HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('servicios', HomeView.as_view(), name='services' ),
    path('portafolio', HomeView.as_view(), name='portfolio'),
    path('blog', HomeView.as_view(), name='blog'),
    path('contacto', HomeView.as_view(), name='contact'),
]