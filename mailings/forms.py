from django import forms
from .models import Subscriber, Campaign


class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ["message", "subscribers", "start_time", "end_time"]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super(CampaignForm, self).__init__(*args, **kwargs)

        if user:
            self.fields["subscribers"].queryset = Subscriber.objects.filter(owner=user)

        self.update_field_attributes()

    def update_field_attributes(self):
        """Обновляем атрибуты полей для улучшения чтения и поддерживаемости."""
        placeholders = {
            "message": "Выберите сообщение",
            "subscribers": "Выберите получателей",
            "start_time": "Введите дату и время начала отправки в формате YYYY-MM-DD HH:MM",
            "end_time": "Введите дату и время конца отправки в формате YYYY-MM-DD HH:MM",
        }

        for field, placeholder in placeholders.items():
            self.fields[field].widget.attrs.update({
                "class": "form-control",
                "placeholder": placeholder,
            })
