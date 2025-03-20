from django import forms
from .models import SupportTicket

class SupportForm(forms.ModelForm):
    class Meta:
        model = SupportTicket
        fields = ['name', 'email', 'subject', 'message']
