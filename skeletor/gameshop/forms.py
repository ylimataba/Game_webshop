from django import forms            
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm      
from .models import Gamer, Developer

class RegistrationForm(UserCreationForm):
    username = forms.CharField(required = True)
    email = forms.EmailField(required = True)
    first_name = forms.CharField(required = False)
    last_name = forms.CharField(required = False)
    #birthday = forms.DateField(required = False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')        

    def save(self,commit = True):   
        user = super(RegistrationForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        #user.birthday = self.cleaned_data['Birthday']

        if commit:
            user.save()
            gamer = Gamer(user=user)
            developer = Developer(user=user)
            gamer.save()
            developer.save()

        return user
