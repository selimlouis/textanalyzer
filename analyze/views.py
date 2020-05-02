from django.shortcuts import render, redirect
from django.template import loader
from django.views.generic import DetailView, CreateView
from .models import Report

from django.http import HttpResponse

# Create your views here.


def index(request):
    template = loader.get_template('analyze/index.html')
    context = {}
    return HttpResponse(template.render(context,request))


class ReportDetailView(DetailView):
    model = Report


class ReportCreateView(CreateView):
    model = Report
    fields = ["headline", "content"]

    #link the report to the request user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
