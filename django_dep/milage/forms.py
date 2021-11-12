from django import forms
from .models import Post
from django.forms import widgets

class DateInput(forms.DateInput):
    input_type = 'date'


class PostMilageForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'miles', 'date_driven']
        widgets = {
            'date_driven' : DateInput()
        }