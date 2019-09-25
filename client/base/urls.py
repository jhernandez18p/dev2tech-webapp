from django.urls import path
from django.views.generic import TemplateView
from .views import HomeView, PortfolioView, ContactView, BlogView, BlogDetailView, \
    ServicesView, QuotationView, ThanksView, SuscribeView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('servicios', ServicesView.as_view(), name='services' ),
    path('cotiza-gratis', QuotationView.as_view(), name='quotation'),
    path('portafolio', PortfolioView.as_view(), name='portfolio'),
    path('blog', BlogView.as_view(), name='blog'),
    path('blog/<slug:slug>', BlogDetailView.as_view(), name='blog-detail'),
    path('contacto', ContactView.as_view(), name='contact'),
    path('suscribe', SuscribeView.as_view(), name='suscribe'),
    path('gracias', ThanksView.as_view(), name='thanks'),
]