from django import forms
from .models import Categorie, Brand

class ProdusFilterForm(forms.Form):
    # Filtru pentru câmpul 'nume' (text)
    nume = forms.CharField(
        label='Nume produs',
        required=False, # Toate câmpurile trebuie să fie opționale într-un filtru
        widget=forms.TextInput(attrs={'placeholder': 'Căutare după nume...'})
    )
    
    # Filtre pentru câmpul 'pret' (numeric)
    # Cerința 1: Inputuri separate pentru min și max
    pret_min = forms.DecimalField(
        label='Preț minim',
        required=False,
        min_value=0,
        widget=forms.NumberInput(attrs={'placeholder': 'Preț minim'})
    )
    pret_max = forms.DecimalField(
        label='Preț maxim',
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'Preț maxim'})
    )
    
    # Filtru pentru câmpul 'categorie' (ForeignKey)
    # Acoperă și Cerința 6
    categorie = forms.ModelChoiceField(
        queryset=Categorie.objects.all().order_by('denumire'),
        required=False,
        empty_label="Toate Categoriile", # Textul pentru "fără filtru"
        label="Categorie"
    )
    
    # Filtru pentru câmpul 'brand' (ForeignKey)
    brand = forms.ModelChoiceField(
        queryset=Brand.objects.all().order_by('nume'),
        required=False,
        empty_label="Toate Brandurile",
        label="Brand"
    )
    
    # Filtru pentru câmpul 'stoc' (boolean)
    in_stoc = forms.BooleanField(
        label='Doar în stoc',
        required=False
    )
    
    # Filtru pentru câmpul 'data_adaugarii' (data)
    # Acoperă și Cerința 4 (widget corespunzător)
    data_adaugare_dupa = forms.DateField(
        label='Adăugat după',
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'}) # Folosim widget-ul HTML5 de dată
    )

    # Putem adăuga și greutate, similar cu prețul
    greutate_min = forms.DecimalField(
        label='Greutate minimă (kg)',
        required=False,
        min_value=0,
        widget=forms.NumberInput(attrs={'placeholder': 'Min kg'})
    )
    greutate_max = forms.DecimalField(
        label='Greutate maximă (kg)',
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'Max kg'})
    )
    
    ITEMS_PER_PAGE_CHOICES = [
        (5, '5 pe pagină'),
        (10, '10 pe pagină'),
        (20, '20 pe pagină'),
    ]
    items_per_page = forms.TypedChoiceField(
        choices=ITEMS_PER_PAGE_CHOICES,
        required=False,
        label='Afișare',
        initial='5', # Valoare implicită
        coerce=int
    )
    
    # --- LOGICĂ ADĂUGATĂ (Req 8) ---
    def __init__(self, *args, **kwargs):
        categorie_blocata = kwargs.pop('categorie_blocata', None)
        super().__init__(*args, **kwargs)

        if categorie_blocata:
            self.fields['categorie'].initial = categorie_blocata
            # Setăm câmpul ca hidden și readonly
            self.fields['categorie'].widget = forms.HiddenInput()
            self.fields['categorie'].disabled = True # Important pentru Req 9

    # --- VALIDĂRI ADĂUGATE (Req 5) ---
    def clean_nume(self):
        # Validare 1: Numele, dacă e completat, să aibă min 3 caractere
        nume = self.cleaned_data.get('nume')
        if nume and len(nume) < 3:
            raise forms.ValidationError("Numele trebuie să conțină cel puțin 3 caractere.")
        return nume

    def clean_pret_max(self):
        # Validare 2: Prețul maxim să fie pozitiv
        pret_max = self.cleaned_data.get('pret_max')
        if pret_max and pret_max < 0:
            raise forms.ValidationError("Prețul maxim nu poate fi negativ.")
        return pret_max

    def clean(self):
        # Validare 3: pret_min < pret_max
        cleaned_data = super().clean()
        pret_min = cleaned_data.get('pret_min')
        pret_max = cleaned_data.get('pret_max')

        if pret_min is not None and pret_max is not None:
            if pret_min > pret_max:
                raise forms.ValidationError(
                    "Eroare: Prețul minim nu poate fi mai mare decât prețul maxim."
                )
        return cleaned_data

class ContactForm(forms.Form):
    nume = forms.CharField(max_length=100, label='Nume', required=True)
    email = forms.EmailField(label='Email', required=True)
    mesaj = forms.CharField(widget=forms.Textarea, label='Mesaj', required=True)
    confirm_email = forms.EmailField(label='Confirmare Email', required=True)
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@domeniu.com'):
            raise forms.ValidationError("Adresa de email trebuie să fie de la domeniu.com")
        return email
    
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        confirm_email = cleaned_data.get("confirm_email")
        if email and confirm_email and email != confirm_email:
            raise forms.ValidationError("Adresele de email nu coincid.")
        



