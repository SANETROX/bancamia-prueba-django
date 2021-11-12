from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.urls import reverse
from .models import UserBancamia
from.forms import UserBancamiaForm
import json

# Create your views here.

def list_users(request):
    users = UserBancamia.objects.all().values()
    print(users)
    data = {"data": users}
    
    return render(request,'users/index.html', data)

class UserBancamiaCreateView(CreateView):
    model = UserBancamia
    form_class = UserBancamiaForm
    template_name = 'users/userbancamia_form.html'
    
    def get_success_url(self):
        return reverse('list_users')