from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import UserCreationForm
from .models import UserBancamia

class UserBancamiaForm(forms.ModelForm):
    class Meta:
        model = UserBancamia
        fields = '__all__'
        labels = {
            'nombre':"Tu nombre"
        }
        widgets = {
        'password': forms.PasswordInput(),
    }

    def __init__(self, *args, **kwargs):
        super(UserBancamiaForm,self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save User'))


class UserBancamiaCreateForm(forms.ModelForm):
    class Meta:
        model = UserBancamia
        fields = '__all__'
        labels = {
            'nombre':"Tu nombre"
        }
        widgets = {
        'password': forms.PasswordInput(),
    }

    def __init__(self, *args, **kwargs):
        super(UserBancamiaCreateForm,self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Save User'))
