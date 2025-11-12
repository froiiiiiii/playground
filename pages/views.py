from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Page
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class PageListView(LoginRequiredMixin,ListView):
    model = Page

class PageDetailView(LoginRequiredMixin,DetailView):
    model = Page
    pk_url_kwarg = 'page_id'

    slug_url_kwarg = 'page_slug'

    slug_field = 'slug'

class PageCreateView(LoginRequiredMixin,CreateView):
    model = Page
    fields = ["title", "content", "order"]
    success_url = reverse_lazy("pages:pages")