from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserCreationCustomForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationCustomForm, self).__init__(*args, **kwargs)
        
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs['class'] = 'form-control'
            self.fields[fieldname].widget.attrs['style'] = 'height: 45px;'
            self.fields[fieldname].label = ''
        
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Password again'