from django import forms


class CheckoutForm(forms.Form):
    first_name = forms.CharField(label="Prénom", max_length=80)
    last_name = forms.CharField(label="Nom", max_length=80)
    phone = forms.CharField(label="Numéro de téléphone", max_length=30)
    email = forms.EmailField(label="Email", required=False)

    country = forms.CharField(label="Pays", max_length=100, initial="Sénégal")
    city = forms.CharField(label="Ville", max_length=100)
    district = forms.CharField(label="Quartier", max_length=100, required=False)
    full_address = forms.CharField(label="Adresse complète", widget=forms.Textarea(attrs={"rows": 2}))
    postal_code = forms.CharField(label="Code postal", max_length=20, required=False)
    extra_info = forms.CharField(label="Indication complémentaire", max_length=255, required=False)
