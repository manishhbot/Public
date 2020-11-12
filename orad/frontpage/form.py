from django import forms
from django.forms import ModelForm
from pip._vendor.urllib3 import fields
from django.contrib.auth.models import User
from .models import Details, Auth


class Newfile(ModelForm):
    class Meta:
        model = Details
        fields = '__all__'
class Usern(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class Authh(ModelForm):
    class Meta:
        model = Auth
        fields = '__all__'
