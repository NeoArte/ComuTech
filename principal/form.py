from django import forms
from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from .models import User, Aid

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'name',
            'email',
            'phone',
            'cpf',
            'cep',
            'birth_date',
            'password1', # Campo - Senha
            'password2', # Campo - Confirme sua senha
        )
    
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'style': 'display: block'})

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.name = self.cleaned_data['name']
        user.email = self.cleaned_data['email']
        user.phone = self.cleaned_data['phone']
        user.cpf = self.cleaned_data['cpf']
        user.cep = self.cleaned_data['cep']
        user.birth_date = self.cleaned_data['birth_date']

        if commit:
            user.save()
        
        return user


class AidForm(ModelForm):
    class Meta:
        model = Aid
        fields = (
            'author',
            'title',
            'description',
            # 'tag', -> quando adicionar as tags novamente
            # photos, 
        )
    
    def __init__(self, *args, **kwargs):
        super(AidForm, self).__init__(*args, **kwargs)
        self.fields['author'].widget = forms.HiddenInput()
        for field in self.fields:
            self.fields[field].widget.attrs.update({'style': 'display: block; margin: 10px auto'})