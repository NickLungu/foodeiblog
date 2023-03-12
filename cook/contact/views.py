from django.shortcuts import render
from django.views.generic import CreateView

from .models import ContactLink, AboutModel
from .forms import ContactForm
from django.views.generic import ListView, DetailView
from django.views import View


class Feedback(CreateView):
    """save feedback in base and go to the root of the site"""
    form_class = ContactForm
    success_url = "/"


class AboutView(View):
    """render about page"""
    def get(self, request):
        about = AboutModel.objects.last()
        contacts = ContactLink.objects.all()
        return render(request, 'contact/about.html', {'about': about, 'contacts': contacts})


class ContactView(View):
    """render contact page and all links of the site"""
    def get(self, request):
        contacts = ContactLink.objects.all()
        form = ContactForm()
        return render(request, "contact/contact.html", {"contacts": contacts, "form": form})