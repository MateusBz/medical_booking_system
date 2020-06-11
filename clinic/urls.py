from django.urls import path
from .views import OfficeListView

urlpatterns = [
    path('', OfficeListView.as_view(), name='offices_list'),
    ]