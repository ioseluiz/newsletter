from django import forms 
from .models import NewsletterUser, Newsletter


class NewsletterUserSingUpForm(forms.ModelForm):
    class meta:
        model = NewsletterUser 
        fields = ['email']

class NewsletterCreationForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['name','subject','body','email']