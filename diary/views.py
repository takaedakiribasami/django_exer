from django.shortcuts import render
from django.views import generic
from . import forms


class IndexView(generic.TemplateView):
    template_name = "index.html"


class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = forms.InquiryForm
