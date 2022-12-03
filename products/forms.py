from django import forms


class ProductCreateForm(forms.Form):
    """Create new product"""
    title = forms.CharField(min_length=10, max_length=150)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.FloatField(min_value=9, max_value=1000000)


class ReviewCreateForm(forms.Form):
    """Create reviews to product"""
    text = forms.CharField(min_length=5, max_length=150)
