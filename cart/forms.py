from django import forms
from .models import CartItem


class MeasurementForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ["bust", "waist", "hips", "shoulders", "desired_length", "sleeve_length", "extra_notes"]
        widgets = {
            "bust": forms.NumberInput(attrs={"placeholder": "ex: 92", "step": "0.5", "class": "field-input"}),
            "waist": forms.NumberInput(attrs={"placeholder": "ex: 75", "step": "0.5", "class": "field-input"}),
            "hips": forms.NumberInput(attrs={"placeholder": "ex: 102", "step": "0.5", "class": "field-input"}),
            "shoulders": forms.NumberInput(attrs={"placeholder": "ex: 40", "step": "0.5", "class": "field-input"}),
            "desired_length": forms.NumberInput(attrs={"placeholder": "ex: 140", "step": "0.5", "class": "field-input"}),
            "sleeve_length": forms.NumberInput(attrs={"placeholder": "ex: 58", "step": "0.5", "class": "field-input"}),
            "extra_notes": forms.Textarea(attrs={"rows": 3, "placeholder": "Précisions utiles pour la couturière…", "class": "field-input"}),
        }
        labels = {
            "bust": "Tour de poitrine (cm)",
            "waist": "Tour de taille (cm)",
            "hips": "Tour de hanches (cm)",
            "shoulders": "Largeur des épaules (cm)",
            "desired_length": "Longueur souhaitée (cm)",
            "sleeve_length": "Longueur des manches (cm)",
            "extra_notes": "Informations complémentaires",
        }
