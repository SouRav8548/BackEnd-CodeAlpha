from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make the form fields look nicer
        for field_name in self.fields:
            self.fields[field_name].help_text = None
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})