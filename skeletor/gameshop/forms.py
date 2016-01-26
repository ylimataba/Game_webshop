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

class PaymentForm(forms.Form):
    pid = forms.CharField(initial='mytestsale',widget = forms.HiddenInput())
    sid = forms.CharField(initial='tester',widget = forms.HiddenInput())
    success_url = forms.URLField(initial='http://localhost:8000/shop/success',widget = forms.HiddenInput())
    cancel_url = forms.URLField(initial='http://localhost:8000/shop/cancel',widget = forms.HiddenInput())
    error_url = forms.URLField(initial='http://localhost:8000/shop/error',widget = forms.HiddenInput())
    checksum = forms.CharField(initial='a91552055bda336550a65c1964f8e013', widget = forms.HiddenInput())
    amount = forms.FloatField(initial=15, widget = forms.HiddenInput())
