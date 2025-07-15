from django import forms
from .models import *


class BrowseForm(forms.ModelForm):
    class Meta:
        model = Browse
        fields = '__all__'


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['location', 'email', 'phone', ]

class TopicListingForm(forms.ModelForm):
    class Meta:
        model = TopicListing
        fields = '__all__'
