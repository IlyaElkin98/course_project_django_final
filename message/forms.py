from django import forms
from message.models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["topic_letter", "body_letter"]
