from django import forms
from .models import Car, Brand


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name']










# class BrandForm(forms.ModelForm):
#     class Meta:
#         model = Brand
#         fields = ['name']


# class CarForm(forms.ModelForm):
#     class Meta:
#         model = Car
#         fields = ['brand', 'name']