
from django import forms
from tsm.models import Ticket

class RaiseTIcketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description']