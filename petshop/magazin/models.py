from django.db import models
from datetime import date, datetime, timedelta
from django.utils.text import slugify

class Locatie(models.Model):
    adresa = models.CharField(max_length=255)
    oras = models.CharField(max_length=100)
    judet = models.CharField(max_length=100)
    cod_postal = models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.adresa}, {self.oras}"

class Animal(models.Model):
    DIMENSIUNE_CHOICES = [
        ('Mic', 'Mic'),
        ('Mediu', 'Mediu'),
        ('Mare', 'Mare'),
        ('N/A', 'Nu se aplică'),
    ]
    dimensiune = models.CharField(
        max_length=50, 
        choices=DIMENSIUNE_CHOICES, 
        default='N/A'
    )
    specie = models.CharField(max_length=100)
    rasa = models.CharField(max_length=100)
    greutate = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        null=True,
        blank=True,
        help_text="Greutatea medie în KG (optional)"
    )
    descriere = models.TextField(blank=True)

    def __str__(self):
        return f"{self.specie} - {self.rasa} ({self.dimensiune})"

    class Meta:
        verbose_name_plural = "Animale"
        unique_together = ('specie', 'rasa', 'dimensiune')


class Serviciu(models.Model):
    nume = models.CharField(max_length=200)
    descriere = models.TextField()
    animale = models.ManyToManyField(
        Animal,
        through='Pret_Serviciu',
        related_name='serviciu'
    )

    def __str__(self):
        return self.nume

    class Meta:
        verbose_name_plural = "Servicii"


class Categorie(models.Model):
    denumire = models.CharField(
        max_length=100, 
        unique=True 
    )
    descriere = models.TextField(blank=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    icon_class = models.CharField(
        max_length=100, 
        blank=True, 
        null=True, 
        help_text="Clasa FontAwesome"
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.denumire)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.denumire

    class Meta:
        verbose_name_plural = "Categorii"


class Brand(models.Model):
    nume = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='branduri/', null=True, blank=True)
    data_fond = models.DateField(verbose_name="Data fondării", null=True, blank=True)
    descriere = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nume

    class Meta:
        verbose_name_plural = "Branduri"


class Furnizor(models.Model):
    nume_companie = models.CharField(max_length=200, unique=True) 
    email_contact = models.EmailField(blank=True)
    telefon = models.CharField(max_length=20, blank=True)
    parteneri_din = models.DateField(null=True, blank=True)
    note = models.TextField(blank=True)

    def __str__(self):
        return self.nume_companie

    class Meta:
        verbose_name_plural = "Furnizori"

class Pret_Serviciu(models.Model):
    """
    Tabelul intermediar pentru preturile serviciilor in functie de tipul animalului
    """
    serviciu = models.ForeignKey(Serviciu, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    pret = models.DecimalField(max_digits=7, decimal_places=2)
    durata = models.IntegerField(help_text="Durata estimata in minute")

    class Meta:
        unique_together = ('serviciu', 'animal')
        verbose_name_plural = "Prețuri Servicii"

    def __str__(self):
        return f"{self.serviciu.nume} {self.animal} - {self.pret} RON"

def data_sf_default():
    return date.today() + timedelta(days=14)

class Oferta(models.Model):
    nume = models.CharField(max_length=100)
    data_inceput = models.DateField(default= date.today)
    data_sfarsit = models.DateField(default= data_sf_default)
    reducere = models.DecimalField(max_digits=5, decimal_places=2, help_text="Procentaj, ex: 15.00 pentru 15%")
    servicii = models.ManyToManyField(Serviciu, blank=True)
    categorii = models.ManyToManyField(Categorie, blank=True)

    def __str__(self):
        return f"{self.nume}, {self.reducere}%"

    class Meta:
        verbose_name_plural = "Oferte"


class Produs(models.Model):
    nume = models.CharField(max_length=255)
    descriere = models.TextField()
    pret = models.DecimalField(max_digits=10, decimal_places=2)
    stoc = models.IntegerField(default=0)
    imagine = models.ImageField(upload_to='produse/', null=True, blank=True)
    data_adaugarii = models.DateTimeField(auto_now_add=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    furnizori = models.ManyToManyField(Furnizor, blank=True)
    greutate = models.DecimalField(
        max_digits=7, 
        decimal_places=3, 
        null=True,
        blank=True
    )

    def __str__(self):
        return self.nume

    class Meta:
        verbose_name_plural = "Produse"