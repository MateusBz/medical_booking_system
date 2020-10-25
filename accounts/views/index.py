from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["info"] = ["To jest demonstracyjna wersja aplikacji do zarządzania wizytami pacjentów i lekarzy. ", "Jeśli nie chcesz zakładać nowego konta użyj kont testowych:", "user: test_patient password: test_user", "user: test_doctor password: test_user"]
        
        return context
    
   