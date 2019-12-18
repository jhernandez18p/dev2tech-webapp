from django.urls import path, include
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

from .views import HomeView, PortfolioView, ContactView, \
    QuotationView, ThanksView, SuscribeView, DisplayPDFView, \
    PricePDFView, PromoQuotationView, Promo125


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('brochure_pdf', DisplayPDFView.as_view(), name='brochure_pdf'),
    path('brochure/precios', PricePDFView.as_view(), name='price_pdf'),
    path('cotiza-gratis', QuotationView.as_view(), name='quotation'),
    path('portafolio', PortfolioView.as_view(), name='portfolio'),
    path('contacto', ContactView.as_view(), name='contact'),
    path('suscribe', SuscribeView.as_view(), name='suscribe'),
    path('gracias', ThanksView.as_view(), name='thanks'),
    path('promo125', Promo125.as_view(), name='promo125'),
    #
    path('brochure', RedirectView.as_view(url='/'), name='brochure'),
    path('mailto', RedirectView.as_view(url='/contacto'), name='mailto'),
    path('instagram', RedirectView.as_view(url='/'), name='instagram'),
    path('facebook', RedirectView.as_view(url='/'), name='facebook'),
    path('twitter', RedirectView.as_view(url='/'), name='twitter'),
    path('whatsapp', RedirectView.as_view(
        url='https://wa.me/50762667545'), name='whatsapp'),
    path('go-to-instagram', RedirectView.as_view(
        url='https://www.instagram.com/dev2tech/'), name='social_instagram'),
    path('go-to-facebook', RedirectView.as_view(
        url='https://www.facebook.com/dev2tech/'), name='social_facebook'),
    path('go-to-twitter', RedirectView.as_view(
        url='https://www.twitter.com/dev2tech/'), name='social_twitter'),
    #
    path('web-45n', PromoQuotationView.as_view(), name='promo-web-45n'),
]