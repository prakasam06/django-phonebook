from django import forms

from .models import contacts

class contact_form(forms.ModelForm):

    class Meta:
        model = contacts
        fields = ('name', 'phonenumber',)