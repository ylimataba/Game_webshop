from django import forms            
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm      
from .models import Gamer, Developer, Game

class RegistrationForm(UserCreationForm):
    username = forms.CharField(required = True)
    email = forms.EmailField(required = True)
    first_name = forms.CharField(required = False)
    last_name = forms.CharField(required = False)
    developer = forms.BooleanField(label="Register as developer", required = False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')        

    def save(self,commit = True):   
        user = super(RegistrationForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            print('saving user')
            user.save()
            if self.cleaned_data['developer']:
                developer = Developer(user=user)
                developer.save()
            gamer = Gamer(user=user)
            gamer.save()


        return user

class PaymentForm(forms.Form):
    pid = forms.CharField(widget = forms.HiddenInput())
    sid = forms.CharField(widget = forms.HiddenInput())
    success_url = forms.URLField(widget = forms.HiddenInput())
    cancel_url = forms.URLField(widget = forms.HiddenInput())
    error_url = forms.URLField(widget = forms.HiddenInput())
    checksum = forms.CharField(widget = forms.HiddenInput())
    amount = forms.FloatField(widget = forms.HiddenInput())
    
class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'description', 'publisher', 'genre', 'source', 'price']


