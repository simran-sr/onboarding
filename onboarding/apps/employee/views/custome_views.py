from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from onboarding.apps.employee.models.employee import ModelEmployee


class NoteList(ListView):
    model = ModelEmployee