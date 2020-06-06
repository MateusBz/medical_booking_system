from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.http import HttpResponse

from ..forms import PatientSignUpForm
from ..models import CustomUser


class PatientSignUpView(CreateView):
    model = CustomUser
    form_class = PatientSignUpForm
    template_name = 'accounts/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'patient'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('login')
