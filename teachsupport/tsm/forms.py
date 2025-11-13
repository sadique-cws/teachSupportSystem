
from django import forms
from tsm.models import TicketComment


class CommentTicketForm(forms.ModelForm):
    class Meta:
        model = TicketComment
        fields = ["comment",]