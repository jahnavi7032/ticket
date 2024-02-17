from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        exclude = ['status', 'creation_date', 'last_modified_date']

class SearchTicketForm(forms.Form):
    phone_email = forms.CharField(required=False)
    category = forms.CharField(required=False)
    start_date = forms.DateField(required=False)
    end_date = forms.DateField(required=False)
