from django import forms
from models import Reminder

class AddReminderForm(forms.Form):
   zipcode = forms.CharField(
       required=True,
       label="Zip Code",
       error_messages={'required': 'Please input Zip Code'},
       widget=forms.TextInput(
           attrs={
               'placeholder': "Zip Code",
               'class': 'form-control',
           }
       )
   )
   reminder = forms.ChoiceField(
       choices=list(Reminder.WARNING_CHOICE),
       widget=forms.Select(
           attrs={
               'class': 'form-control',
           }
       )
   )