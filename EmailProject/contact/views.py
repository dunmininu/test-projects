from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy

from .forms import ContactForm

# Create your views here.


class ContactView(FormView):
    template_name = "contact/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("contact:success")

    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)


class ContactSuccessView(TemplateView):
    template_name = "contact/success.html"
