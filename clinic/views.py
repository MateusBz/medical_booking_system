from django.views.generic import ListView
from .models import Office

class OfficeListView(ListView):
    model = Office
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["offices"] = Office.objects.filter(occupied=False)
        return context
    