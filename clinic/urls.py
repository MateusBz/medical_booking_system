from django.urls import path
from .views import VisitCreateView, VisitDetailView, VisitListView

urlpatterns = [
    path('', VisitCreateView.as_view(), name='visit_creation'),
    path('<int:pk>/', VisitDetailView.as_view(), name='visit_detail'),
    path('visits/', VisitListView.as_view(), name='visits_list'),
    ]