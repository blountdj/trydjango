from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={
            "class": "new-class-name two",
            "id": "my-id-for-textarea",
            "rows": 20,
            "cols": 120,
            "placeholder": "Your description"
        }
    ))
    price = forms.DecimalField(initial=199.99)
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    # this get called when form is submitted if method name format (clean_<field_title>) is followed. (not sure how)
    def clean_title(self, *args, **kwargs):
        """
        Make sure title contains the text 'CFE'
        """
        title = self.cleaned_data.get('title')
        if not "CFE" in title:
            raise forms.ValidationError('This is not a valid title')
        if not "news" in title:
            raise forms.ValidationError('This is not a valid title')

        return title


class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={
            "class": "new-class-name two",
            "id": "my-id-for-textarea",
            "rows": 20,
            "cols": 120,
            "placeholder": "Your description"
        }
    ))
    price = forms.DecimalField(initial=199.99)
