from django import forms
from django.forms import ModelForm, fields, widgets
from django.contrib.auth.forms import UserCreationForm
from .models import User, Aid
from django.contrib.admin import widgets

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
            'facebook',
            'whatsapp',
            'twitter',
            'instagram',
            'profile_picture',
            'password1', # Campo - Senha
            'password2', # Campo - Confirme sua senha
        )
    
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})

        self.fields['name'].widget.attrs.update({
            'placeholder':'Nome Completo',
            'type':'text',
            'id':'name',
        })
        self.fields['email'].widget.attrs.update({
            'placeholder':'Email',
            'type':'email',
            'id':'email',
        })
        self.fields['phone'].widget.attrs.update({
            'placeholder':'Celular',
            'type':'text',
            'id':'phone',
        })
        self.fields['cpf'].widget.attrs.update({
            'placeholder':'CPF',
            'type':'text',
            'id':'cpf',
        })
        self.fields['cep'].widget.attrs.update({
            'placeholder':'CEP',
            'type':'text',
            'id':'cep',
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder':'Senha',
            'type':'password',
            'id':'password',
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder':'Senha',
            'type':'password',
            'id':'ConfirmPassword',
        })
        self.fields['facebook'].widget.attrs.update({
            'placeholder':'Informe seu facebook',
            'type':'text',
            'id':'facebook-input',
        })
        self.fields['whatsapp'].widget.attrs.update({
            'placeholder':'Informe seu número de whatsapp',
            'type':'text',
            'id':'whatsapp-input',
        })
        self.fields['instagram'].widget.attrs.update({
            'placeholder':'Informe seu Instagram',
            'type':'text',
            'id':'instagram-input',
        })
        self.fields['twitter'].widget.attrs.update({
            'placeholder':'Informe seu twitter',
            'type':'text',
            'id':'twitter-input',
        })
        self.fields['birth_date'].widget.attrs.update({
            'placeholder':'',
            'type':'date',
            'id':'date-input',
        })
        self.fields['profile_picture'].widget.attrs.update({
            'class':'',
            'id':'_inputIMG'
            })

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