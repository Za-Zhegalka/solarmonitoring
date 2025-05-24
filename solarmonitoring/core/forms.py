from django import forms
from .models import SupportRequest, SaleAdvertisement


class SupportRequestReplyForm(forms.ModelForm):
    reply = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4}),
        required=False,
        label='Ваш ответ'
    )

    class Meta:
        model = SupportRequest
        fields = ['status', 'reply']
        widgets = {
            'status': forms.Select(attrs={
                'class': 'form-select',
                'style': 'width: 200px;'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].choices = [
            ('open', 'Открыт'),
            ('in_progress', 'В работе'),
            ('resolved', 'Решен'),
        ]


class AdvertisementModerationForm(forms.ModelForm):
    rejection_reason = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}),
        required=False,
        label='Причина отклонения (если отклоняете)'
    )

    class Meta:
        model = SaleAdvertisement
        fields = ['status', 'rejection_reason']
        widgets = {
            'status': forms.Select(attrs={
                'class': 'form-select',
                'style': 'width: 200px;'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].choices = [
            ('pending', 'На рассмотрении'),
            ('approved', 'Одобрено'),
            ('rejected', 'Отклонено'),
        ]

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('status') == 'rejected' and not cleaned_data.get('rejection_reason'):
            self.add_error('rejection_reason', 'Укажите причину отклонения')
        return cleaned_data