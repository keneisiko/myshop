from django import forms

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(
        min_value=1,
        max_value=10,
        initial=1,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

class CardDataForm(forms.Form):
    card_number = forms.CharField(max_length=19, widget=forms.TextInput(attrs={'placeholder': '0000 0000 0000 0000', 'class': 'form-control'}))
    card_expiry = forms.CharField(max_length=5, widget=forms.TextInput(attrs={'placeholder': 'MM/YY', 'class': 'form-control'}))
    card_cvv = forms.CharField(max_length=4, widget=forms.TextInput(attrs={'placeholder': 'CVV', 'class': 'form-control'}))
    card_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'IVAN IVANOV', 'class': 'form-control'}))