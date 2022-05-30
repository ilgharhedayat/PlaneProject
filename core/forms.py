from django import forms
from .models import ContactUs, WorkWith


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = (
            'email',
            'phone_number',
            'title',
            'text',
        )
        labels = {
            'email': 'ایمیل',
            'phone_number': 'شماره تماس',
            'title': 'موضوع',
            'text': 'متن',
        }

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "travelSrc",
                    "placeholder": "موضوع",
                }
            ),
            "text": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "travelSrc",
                    "placeholder": "متن",
                }
            ),
            "phone_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "travelSrc",
                    "placeholder": "شماره تلفن",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "ایمیل",
                }
            )}


class WorkWithForm(ContactUsForm):
    class Meta(ContactUsForm.Meta):
        model = WorkWith
        fields = ContactUsForm.Meta.fields
