from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

"""
Base View
"""
class HomeView(TemplateView):
    template_name = "blank.html"
