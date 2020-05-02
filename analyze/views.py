from django.shortcuts import render, redirect
from django.template import loader
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from .models import Report
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.http import HttpResponse

# Create your views here.


def index(request):
    template = loader.get_template('analyze/index.html')
    context = {}
    return HttpResponse(template.render(context,request))


class ReportDetailView(DetailView):
    model = Report

class ReportDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Report
    success_url = '/profile'

    def test_func(self):
        report = self.get_object()
        if report.author == self.request.user:
            return True

        return False


#login mixin is a super class that handles the login requirement
class ReportCreateView(LoginRequiredMixin, CreateView):
    model = Report
    fields = ["headline", "content"]

    #link the report to the request user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ReportUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Report
    fields = ["headline", "content"]
    template_name_suffix = "_update_form"

    #link the report to the request user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    #make sure the logged in user is the author of the report
    def test_func(self):
        #get the report that is being edited on
        report = self.get_object()
        if self.request.user == report.author:
            return True
        
        return False