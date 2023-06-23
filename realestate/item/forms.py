from django import forms

from .models import Item

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('catergory_id', 'name', 'descripion', 'price', 'currency_value', 'image', 'contact_info')

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'descripion', 'price', 'currency_value', 'image', 'contact_info')

