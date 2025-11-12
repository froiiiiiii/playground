from django.urls import path
from . import views
from.views import PageListView, PageDetailView, PageCreateView

app_name = "pages"  # <- esto permite usar un namespace en include()

urlpatterns = [
    path('', PageListView.as_view(), name='pages'),
    path('<int:page_id>/<slug:page_slug>/', PageDetailView.as_view(), name='page'),
    path('create/', PageCreateView.as_view(), name='create'),
]