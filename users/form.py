'''It creates a form which inherits from user creation form'''
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    '''
        This class inherits from usercreastion form to add
        a new field form
    '''
    #required is set to true or could be set to false
    email = forms.EmailField() 


    class Meta:
        '''
        We specify the model we want the class to interate with
        We specify the fields we want to be shown in our form
        Class meta gives us a nested name space for configration. Within the configration
        were saying the model that is affected is the user model, for example when we do form.save it
        would save it to user model. The field denoted the fields in the form and in what order.
        '''
        model = User #model we want this form to interact with

        #fields that are going to be shown on our form
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField() #fields in addition to the model


    class Meta:
        
        model = User #model we want this form to interact with

        #fields that are going to be shown on our form
        fields = ['username', 'email'] #


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile  #model we want the form to deal with
        fields = ['image']
