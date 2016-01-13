from django.shortcuts import render
from django.views.generic.base import TemplateView

from braces.views import SetHeadlineMixin


class IndexView(SetHeadlineMixin, TemplateView):

    template_name = 'index.html'
    headline = "Broadcast Chat"