from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.http import HttpResponse

from ..forms import DoctorCreationForm
from ..models import CustomUser


class DoctorSignUpView(CreateView):
    model = CustomUser
    form_class = DoctorCreationForm
    template_name = 'accounts/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'doctor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return HttpResponse('Witaj doctorze!')
