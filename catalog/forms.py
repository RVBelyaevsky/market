from django import forms
from django.forms import BooleanField

from catalog.models import Product, Blog, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    danger = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at',)

    def clean_product_name(self):
        cleaned_data = self.cleaned_data.get('product_name')

        if cleaned_data in self.danger:
            raise forms.ValidationError('не допустимое имя продукта.')

        return cleaned_data

    def clean_product_description(self):
        cleaned_data = self.cleaned_data.get('product_description')

        if cleaned_data in self.danger:
            raise forms.ValidationError('не допустимое описание продукта.')

        return cleaned_data


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        exclude = ('created_at', 'count_views',)


class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'

