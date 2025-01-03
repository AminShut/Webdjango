from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home/home_page.html'

class AboutPageView(TemplateView):
    template_name = 'home/about_page.html'
