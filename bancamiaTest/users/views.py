from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from .models import UserBancamia
from.forms import UserBancamiaForm, UserBancamiaCreateForm
import json

# Create your views here.
def register2(request):
    return render(request, 'users/register2.html')

class RegisterUserCreateView(CreateView):
    model = UserBancamia
    form_class = UserBancamiaCreateForm
    template_name = 'users/register2.html'

    def get_success_url(self):
        return reverse('list_users')


def register_user(request):
    form = UserBancamiaCreateForm
    context = {"form":form}
    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         print(form)
    #         form.save()
    #         return redirect('inicio')
    return render(request, 'users/register2.html',context)


def list_users(request):
    users = UserBancamia.objects.all().values()
    users_count = UserBancamia.objects.count()
    data = {"users": users, "users_count": users_count}
    
    return render(request,'users/index.html', {"users": users, "users_count": users_count})


class UserBancamiaCreateView(CreateView):
    model = UserBancamia
    form_class = UserBancamiaForm
    template_name = 'users/userbancamia_form.html'
    
    def get_success_url(self):
        return reverse('list_users')