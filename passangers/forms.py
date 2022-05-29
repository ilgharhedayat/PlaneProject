from django import forms

# from django.forms import formset_factory, modelformset_factory
from django.forms.formsets import BaseFormSet

from .models import Passenger


#
class PassengerForm(forms.ModelForm):
    pass
    # email = forms.EmailField(
    #     widget=forms.EmailInput(attrs={'class': 'form-control me-2', 'placeholder': 'Email', 'required': False}))
    # phone_number = forms.CharField(max_length=10,
    #                                widget=forms.TextInput(
    #                                    attrs={'class': 'form-control', 'placeholder': 'تلفن همراه', 'required': False}))

    # class Meta:
    #     model = Passenger
    #     fields = (
    #         "en_name",
    #         # "en_family",
    # "gender",
    # "national_code",
    # "ir_name",
    # 'ir_family',
    # "day",
    # "month",
    # "year ",
    # )
    # widgets = {
    #     "en_name": forms.TextInput(
    #         attrs={
    #             "class": "form-control",
    #             "id": "travelSrc",
    #             "placeholder": "نام لاتین ",
    #         }
    #     ),
    # "en_family": forms.TextInput(
    #     attrs={
    #         "class": "form-control",
    #         "id": "travelSrc",
    #         "placeholder": "نام خانوادگی لایتن",
    #     }
    # ),
    # "gender": forms.TextInput(
    #     attrs={
    #         "class": "form-control",
    #         "id": "travelSrc",
    #         "placeholder": "جنسیت",
    #     }
    # ),
    # "national_code": forms.TextInput(
    #     attrs={
    #         "class": "form-control",
    #         "id": "travelSrc",
    #         "placeholder": "کد ملی",
    #     }
    # ),
    # "ir_name": forms.TextInput(
    #     attrs={
    #         "class": "form-control",
    #         "id": "travelGoal",
    #         "placeholder": "نام",
    #     }
    # ),
    # }


# class BaseLinkFormSet(BaseFormSet):
#     def clean(self):
#         """
#         Adds validation to check that no two links have the same anchor or URL
#         and that all links have both an anchor and URL.
#         """
#         if any(self.errors):
#             return
#
#         en_name = []
#         en_family = []
#         gender = []
#         national_code = []
#         ir_family = []
#         day = []
#         month = []
#         year = []
#         duplicates = False
#
#         for form in self.forms:
#             if form.cleaned_data:
#                 en_name = form.cleaned_data['en_name']
#                 en_family = form.cleaned_data['en_family']
#                 gender = form.cleaned_data['gender']
#                 ir_name = form.cleaned_data['ir_name']
#                 ir_family = form.cleaned_data['ir_family']
#                 national_code = form.cleaned_data['national_code']
#                 day = form.cleaned_data['day']
#                 month = form.cleaned_data['month']
#                 year = form.cleaned_data['year']
#
#                 # Check that no two links have the same anchor or URL
#                 if en_name and en_family and gender and national_code and national_code and ir_name and ir_family and day and month and year:
#                     if en_name in en_name:
#                         duplicates = True
#                     en_name.append(en_name)
#
#                 if en_name and en_family and gender and national_code and national_code and ir_name and ir_family and day and month and year:
#                     if en_family in en_family:
#                         duplicates = True
#                     en_family.append(en_family)
#
#                 if en_name and en_family and gender and national_code and national_code and ir_name and ir_family and day and month and year:
#                     if gender in gender:
#                         duplicates = True
#                     gender.append(gender)
#
#                 if en_name and en_family and gender and national_code and national_code and ir_name and ir_family and day and month and year:
#                     if ir_name in ir_name:
#                         duplicates = True
#                     ir_name.append(ir_name)
#
#                 if en_name and en_family and gender and national_code and national_code and ir_name and ir_family and day and month and year:
#                     if ir_family in ir_family:
#                         duplicates = True
#                     ir_family.append(ir_family)
#
#                 if en_name and en_family and gender and national_code and national_code and ir_name and ir_family and day and month and year:
#                     if national_code in national_code:
#                         duplicates = True
#                     national_code.append(national_code)
#
#                 if en_name and en_family and gender and national_code and national_code and ir_name and ir_family and day and month and year:
#                     if day in day:
#                         duplicates = True
#                     day.append(day)
#
#                 if en_name and en_family and gender and national_code and national_code and ir_name and ir_family and day and month and year:
#                     if month in month:
#                         duplicates = True
#                     month.append(month)
#
#                 if en_name and en_family and gender and national_code and national_code and ir_name and ir_family and day and month and year:
#                     if year in year:
#                         duplicates = True
#                     year.append(year)
#
#                 if duplicates:
#                     raise forms.ValidationError(
#                         'Links must have unique anchors and URLs.',
#                         code='duplicate_links'
#                     )
#
#                 # # Check that all links have both an anchor and URL
#                 # if url and not anchor:
#                 #     raise forms.ValidationError(
#                 #         'All links must have an anchor.',
#                 #         code='missing_anchor'
#                 #     )
#                 # elif anchor and not url:
#                 #     raise forms.ValidationError(
#                 #         'All links must have a URL.',
#                 #         code='missing_URL'
#                 #     )


# from django import forms
#
#
# class CallForm(forms.Form):
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control me-2', 'placeholder': 'Email'}))
#     phone_number = forms.CharField(max_length=10,
#                                    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'تلفن همراه'}))
