from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(LoginRequiredMixin, TemplateView):
    template_name = 'core/Home.html'
class Sample(LoginRequiredMixin, TemplateView):
    template_name = 'core/Sample.html'

