from django import forms
from django.forms import ModelForm, fields, widgets
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Aid, AidPhotos
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
            'state', 
            'city', 
            'neighborhood', 
            'street',
            'house_number',
        )
    
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control','autocomplete':'off'})

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
            'maxlenght':'9',
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder':'Senha',
            'type':'password',
            'id':'password',
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder':'Confirmar Senha',
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
            'placeholder':'Data de nascimento',
            'type':'date',
            'id':'birth-date',
            'class':'form-control datepicker'
        })
        self.fields['profile_picture'].widget.attrs.update({
            'class':'',
            'id':'_inputIMG'
        })
        self.fields['state'].widget.attrs.update({
            'class':'form-control without-icon',
            'id':'state',
            'placeholder':'UF',
        })
        self.fields['city'].widget.attrs.update({
            'class':'form-control without-icon',
            'id':'city',
            'placeholder':'Cidade',
        })
        self.fields['neighborhood'].widget.attrs.update({
            'class':'form-control without-icon',
            'id':'neighborhood',
            'placeholder':'Bairro',
        })
        self.fields['street'].widget.attrs.update({
            'class':'form-control without-icon',
            'id':'street',
            'placeholder':'Rua',
        })
        self.fields['house_number'].widget.attrs.update({
            'class':'form-control without-icon inputNumber',
            'id':'house_number',
            'placeholder':'Casa',
            'type':'number',
        })
        

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.name = self.cleaned_data['name']
        user.email = self.cleaned_data['email']
        user.phone = self.cleaned_data['phone']
        user.cpf = self.cleaned_data['cpf']
        user.cep = self.cleaned_data['cep']
        user.birth_date = self.cleaned_data['birth_date']

        #ITENS OPCIONAIS
        user.facebook = self.cleaned_data['facebook']
        user.whatsapp = self.cleaned_data['whatsapp']
        user.twitter = self.cleaned_data['twitter']
        user.instagram = self.cleaned_data['facebook']
        user.profile_picture = self.cleaned_data['profile_picture']

        if commit:
            user.save()
        
        return user

class EditProfileForm(UserChangeForm):
    
    class Meta:
        model = User
        fields = (
            'profile_picture',
            'name',
            'email',
            'phone', 
            'facebook', 
            'whatsapp', 
            'instagram', 
            'twitter', 
            'cpf', 
            'cep', 
            'birth_date', 
            'password', 
            )

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})

        self.fields['name'].widget.attrs.update({
            'placeholder':'Nome Completo',
            'type':'text',
            'id':'name',
            'class':'form-control big-input',
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
        self.fields['birth_date'].widget.attrs.update({
            'placeholder':'Data de nascimento',
            'type':'text',
            'id':'birth_date',
            'class':'form-control datepicker',
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
        self.fields['profile_picture'].widget.attrs.update({
            'class':'edit-img',
            'id':'_inputIMG',
            'accept':'image/*',
        })
        


class AidForm(ModelForm):
    class Meta:
        model = Aid
        fields = (
            'author',
            'title',
            'type',
            'description',
            # photos, 
        )
        exclude = ['author']
    
    def __init__(self, *args, **kwargs):
        self._author = kwargs.pop('author') # 'author' será um kwarg (um argumento) que será passado pela views (request.user)
        super(AidForm, self).__init__(*args, **kwargs)
        
        self.fields['title'].widget.attrs.update({
        'placeholder':'Título da Publicação',
        'type':'text',
        'id':'title',
        'class':'form-control big-input',
        })
        self.fields['description'].widget.attrs.update({
            'class':'form-control desc-textarea',
            'id':'aid-desc',
        })
        self.fields['type'].widget.attrs.update({
            'class':'form-control',
            'id':'aid-type',
        })

    def save(self, commit=True):
        aidform = super(AidForm, self).save(commit=False)
        aidform.author = self._author
        if commit:
            aidform.save()
        return aidform
    

class AidPhotosForm(ModelForm):
    class Meta:
        model = AidPhotos
        fields = "__all__"
        exclude = ['aid']
    
    def __init__(self, *args, **kwargs):
        super(AidPhotosForm, self).__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({
            'multiple': True,
            'id':'_aidInputIMG',
            'accept':'image/*',
        })