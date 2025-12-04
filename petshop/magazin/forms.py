from django import forms
from .models import Categorie, Brand, User
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from datetime import date
import re
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm

def validare_text(value):
    """Validare i"""
    if not value:
        return
    if not re.match(r'^[A-ZȘȚÂĂÎ][a-zA-Zșțâăî\s-]*$', value):
        raise ValidationError(
            'Textul trebuie să înceapă cu majusculă și să conțină doar litere, spații sau cratime.',
            code='format_invalid'
        )

def validare_cap_sep(value):
    """Validare j"""
    if not value:
        return
    if re.search(r'[\s-][a-zșțâăî]', value):
        raise ValidationError(
            'Fiecare cuvânt dupa separator trebuie să înceapă cu majusculă.',
            code='capitalizare_invalida'
        )

def validare_no_links(value):
    """Validare d"""
    if not value:
        return
    
    text_mic = value.lower()
    if 'http://' in text_mic or 'https://' in text_mic:
        raise ValidationError(
            'Acest câmp nu poate conține link-uri (http:// sau https://).',
            code='link_invalid'
        )

def validare_word_cnt(value):
    """Validare b"""
    words = re.findall(r'\w+', value)
    if not 5 <= len(words) <= 100:
        raise ValidationError(
            f'Mesajul trebuie să conțină între 5 și 100 de cuvinte (actual: {len(words)}).',
            code='word_count_invalid'
        )

def validare_max_len(value):
    """Validare c"""
    words = re.findall(r'\w+', value)
    for word in words:
        if len(word) > 15:
            raise ValidationError(
                f'Cuvântul "{word[:15]}..." depășește limita de 15 caractere.',
                code='word_length_invalid'
            )

def validare_temp_email(value):
    """Validare h"""
    temp_email = ['guerillamail.com', 'yopmail.com']
    if value.split('@')[-1].lower() in temp_email:
        raise ValidationError(
            'Nu acceptăm adrese de e-mail temporare (guerillamail, yopmail).',
            code='temp_email'
        )

class ContactForm(forms.Form):

    nume = forms.CharField(
        max_length=10, 
        required=True, 
        label='Nume',
        validators=[validare_text, validare_cap_sep]
    )
    
    prenume = forms.CharField(
        max_length=10, 
        required=False, 
        label='Prenume',
        validators=[validare_text, validare_cap_sep]
    )
    
    CNP = forms.CharField(
        max_length=13, 
        min_length=13,
        required=False, 
        label='CNP',
        validators=[
            # Validare f
            RegexValidator(r'^\d{13}$', "CNP-ul trebuie să conțină exact 13 cifre.")
        ]
    )
    
    data_nasterii = forms.DateField(
        required=True, 
        label='Data nașterii',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    
    email = forms.EmailField(
        required=True, 
        label='E-mail',
        validators=[validare_temp_email]
    )
    
    confirmare_email = forms.EmailField(
        required=True, 
        label='Confirmare e-mail'
    )
    
    TIP_MESAJ_CHOICES = [
        ('neselectat', 'Neselectat'),
        ('reclamatie', 'Reclamație'),
        ('intrebare', 'Întrebare'),
        ('review', 'Review'),
        ('cerere', 'Cerere'),
        ('programare', 'Programare'),
    ]
    tip_mesaj = forms.ChoiceField(
        choices=TIP_MESAJ_CHOICES,
        initial='neselectat', 
        label="Tip mesaj"
    )
    
    subiect = forms.CharField(
        max_length=100, 
        required=True, 
        label='Subiect',
        validators=[validare_text, validare_no_links]
    )
    
    zile_asteptare_help = (
        "Pentru review-uri/cereri minimul de zile de asteptare trebuie setat de la 4 incolo "
        "iar pentru cereri/intrebari de la 2 incolo. Maximul e 30."
    )
    minim_zile_asteptare = forms.IntegerField(
        required=True,
        label="Minim zile asteptare",
        min_value=0, 
        max_value=30,
        help_text=zile_asteptare_help
    )
    
    mesaj = forms.CharField(
        required=True,
        widget=forms.Textarea,
        label="Mesaj (vă rugăm să vă și semnați)",
        validators=[validare_word_cnt, validare_max_len, validare_no_links]
    )
    
    def clean_data_nasterii(self):
        """Validare a"""
        data_n = self.cleaned_data.get('data_nasterii')
        if data_n:
            today = date.today()
            data_maj = today.replace(year=today.year - 18)
            if data_n > data_maj:
                raise ValidationError("Expeditorul trebuie sa fie major")
        return data_n
    
    def clean_CNP(self):
        """Validare g"""
        cnp = self.cleaned_data.get('CNP')
        if not cnp:
            return cnp
        if cnp[0] not in ['1', '2']:
             raise ValidationError("CNP-ul trebuie sa inceapa cu 1 sau 2")
        try:
            an_prefix = "19" if cnp[0] == '1' else "20"
            an = int(an_prefix + cnp[1:3])
            luna = int(cnp[3:5])
            zi = int(cnp[5:7])
            date(an, luna, zi) 
        except ValueError:
            raise ValidationError("Cifrele 2-7 din CNP nu formează o data valida")
        
        return cnp
    
    def clean_tip_mesaj(self):
        """Validare e"""
        tip = self.cleaned_data.get('tip_mesaj')
        if tip == 'neselectat':
            raise ValidationError("Nu ai selectat un tip de mesaj valid")
        return tip

    def clean(self):
        cleaned_data = super().clean()
        
        # Validare a
        email = cleaned_data.get('email')
        confirm_email = cleaned_data.get('confirmare_email')
        if email and confirm_email and email != confirm_email:
            self.add_error('confirmare_email', "Adresele de e-mail nu se potrivesc.")

        # Validare b
        nume = cleaned_data.get('nume')
        mesaj = cleaned_data.get('mesaj')
        if nume and mesaj and not mesaj.strip().endswith(nume):
            self.add_error('mesaj', f"Mesajul trebuie să se încheie cu semnătura (numele dvs.: '{nume}').")
            
        # Validare c
        tip_mesaj = cleaned_data.get('tip_mesaj')
        zile = cleaned_data.get('minim_zile_asteptare')
        if tip_mesaj and zile is not None:
            if tip_mesaj in ['review', 'cerere'] and zile < 4:
                self.add_error('minim_zile_asteptare', f"Pentru '{tip_mesaj}', minimul de zile este 4")
            elif tip_mesaj in ['reclamatie', 'intrebare'] and zile < 2:
                self.add_error('minim_zile_asteptare', f"Pentru '{tip_mesaj}', minimul de zile este 2")

        # Validare d
        cnp = cleaned_data.get('CNP')
        data_n = cleaned_data.get('data_nasterii')
        if cnp and data_n:
            an_prefix = "19" if cnp[0] == '1' else "20"
            an = int(an_prefix + cnp[1:3])
            luna = int(cnp[3:5])
            zi = int(cnp[5:7])
            cnp_date = date(an, luna, zi)
            if cnp_date != data_n:
                self.add_error('CNP', "Data din CNP nu corespunde cu cea introdusa")

        if not self.errors:
            # Preproc a
            if data_n:
                today = date.today()
                total_luni = (today.year - data_n.year) * 12 + (today.month - data_n.month)
                if today.day < data_n.day:
                    total_luni -= 1
                ani = total_luni // 12
                luni = total_luni % 12
                cleaned_data['varsta'] = f"{ani} ani și {luni} luni"
                del cleaned_data['data_nasterii']

            if mesaj:
                # Preproc b
                mesaj_proc = mesaj.replace('\r\n', ' ').replace('\n', ' ')
                mesaj_proc = re.sub(r'\s+', ' ', mesaj_proc).strip()
                # Preproc c
                mesaj_proc = re.sub(
                    r'([.?!]+)(\s*)(\w)', 
                    lambda m: m.group(1) + m.group(2) + m.group(3).upper(), 
                    mesaj_proc
                )
                cleaned_data['mesaj'] = mesaj_proc
            
            # Preproc d
            cleaned_data['urgent'] = False 
            if tip_mesaj and zile is not None:
                if (tip_mesaj in ['review', 'cerere'] and zile == 4) or \
                   (tip_mesaj in ['reclamatie', 'intrebare'] and zile == 2):
                    cleaned_data['urgent'] = True
            
            if 'confirmare_email' in cleaned_data:
                del cleaned_data['confirmare_email']

        return cleaned_data
    
class ProdusFilterForm(forms.Form):
    nume = forms.CharField(
        label='Nume produs',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Căutare după nume...'})
    )

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
    
    categorie = forms.ModelChoiceField(
        queryset=Categorie.objects.all().order_by('denumire'),
        required=False,
        empty_label="Toate Categoriile", 
        label="Categorie"
    )

    brand = forms.ModelChoiceField(
        queryset=Brand.objects.all().order_by('nume'),
        required=False,
        empty_label="Toate Brandurile",
        label="Brand"
    )
    
    in_stoc = forms.BooleanField(
        label='Doar în stoc',
        required=False
    )
    
    data_adaugare_dupa = forms.DateField(
        label='Adăugat după',
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'})
    )

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
        initial='5', 
        coerce=int
    )
    
    def __init__(self, *args, **kwargs):
        categorie_blocata = kwargs.pop('categorie_blocata', None)
        super().__init__(*args, **kwargs)
        if categorie_blocata:
            self.fields['categorie'].initial = categorie_blocata
            self.fields['categorie'].widget = forms.HiddenInput()
            self.fields['categorie'].disabled = True 

    def clean_nume(self):
        nume = self.cleaned_data.get('nume')
        if nume and len(nume) < 3:
            raise forms.ValidationError("Numele trebuie să conțină cel puțin 3 caractere.")
        return nume

    def clean_pret_max(self):
        pret_max = self.cleaned_data.get('pret_max')
        if pret_max and pret_max < 0:
            raise forms.ValidationError("Prețul maxim nu poate fi negativ.")
        return pret_max

    def clean(self):
        cleaned_data = super().clean()
        pret_min = cleaned_data.get('pret_min')
        pret_max = cleaned_data.get('pret_max')
        if pret_min is not None and pret_max is not None:
            if pret_min > pret_max:
                raise forms.ValidationError(
                    "Eroare: Prețul minim nu poate fi mai mare decât prețul maxim."
                )
        return cleaned_data

class InregistrareForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Adresă de Email")
    first_name = forms.CharField(required=True, label="Prenume")
    last_name = forms.CharField(required=True, label="Nume")
    class Meta:
        model = User
        fields = [
            'username', 'email', 'first_name', 'last_name', 
            'telefon', 'adresa', 'judet', 'localitate', 'cod_postal'
        ]
        
    def clean_telefon(self):
        telefon = self.cleaned_data.get('telefon')
        if not telefon:
            raise forms.ValidationError("Numărul de telefon este obligatoriu.")
        if not telefon.isdigit():
            raise forms.ValidationError("Numărul de telefon trebuie să conțină doar cifre.")

        if len(telefon) < 10:
            raise forms.ValidationError("Numărul de telefon este prea scurt (minim 10 cifre).")
        return telefon
    
    def clean_cod_postal(self):
        cod = self.cleaned_data.get('cod_postal')
        if cod:
            if not cod.isdigit():
                raise forms.ValidationError("Codul poștal trebuie să conțină doar cifre.")
            if len(cod) != 6:
                raise forms.ValidationError("Codul poștal trebuie să aibă exact 6 cifre.")
        return cod

    def clean_judet(self):
        judet = self.cleaned_data.get('judet')
        if judet:
            if not judet[0].isupper():
                raise forms.ValidationError("Numele județului trebuie să înceapă cu literă mare (ex: București, Ilfov).")
        return judet

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Acest email este deja folosit de un alt cont.")
        return email        

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Parola'}))
    ramane_logat = forms.BooleanField(
        required=False, 
        label="Păstrează-mă logat pentru o zi",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

