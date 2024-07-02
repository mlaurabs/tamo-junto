from django.db import models

# Create your models here.

class Membro(models.Model):
    CITY_OPTIONS = [
    ("Brasil", "Brasil"),
]
    COUNTRY_OPTIONS = [
    ("Rio de Janeiro", "Rio de Janeiro"),
    ("Niterói", "Niterói"),
]
    GENDER_OPTIONS =[
        ("Feminino", "Feminino"),
        ("Masculino", "Masculino"),
        ("Outro", "Outro"),
    ]
    full_name = models.CharField(max_length=70)
    age = models.IntegerField()
    #country = models.CharField(max_length=20)
    cep = models.CharField(max_length=8)
    country = models.CharField(max_length=20, choices=COUNTRY_OPTIONS)
    city = models.CharField(max_length=20, choices=CITY_OPTIONS)
    street = models.CharField(max_length=50)
    address_number = models.IntegerField()
    address_complement = models.CharField(max_length=50)
    tel_ddd = models.CharField(max_length=2)
    tel = models.CharField(max_length=9)
    gender = models.CharField(max_length=20, choices=GENDER_OPTIONS)
    #profile_photo = models.ImageField(upload_to='') PRECISO TESTAR ISSO COM O FORMS
    # falta o campo dos interesses
    bio = models.CharField(max_length=200)

class Instrutor(models.Model):
    CITY_OPTIONS = [
    ("Brasil", "Brasil"),
]
    COUNTRY_OPTIONS = [
    ("Rio de Janeiro", "Rio de Janeiro"),
    ("Niterói", "Niterói"),
]
    GENDER_OPTIONS =[
        ("Feminino", "Feminino"),
        ("Masculino", "Masculino"),
        ("Outro", "Outro"),
    ]
    full_name = models.CharField(max_length=70)
    age = models.IntegerField()
    #country = models.CharField(max_length=20)
    cep = models.CharField(max_length=8)
    country = models.CharField(max_length=20, choices=COUNTRY_OPTIONS)
    city = models.CharField(max_length=20, choices=CITY_OPTIONS)
    street = models.CharField(max_length=50)
    address_number = models.IntegerField()
    address_complement = models.CharField(max_length=50)
    tel_ddd = models.CharField(max_length=2)
    tel = models.CharField(max_length=9)
    gender = models.CharField(max_length=20, choices=GENDER_OPTIONS)
    #profile_photo = models.ImageField(upload_to='') PRECISO TESTAR ISSO COM O FORMS
    # falta o campo dos interesses
    # falta o campo doas aulas lecionadas
    #certificate = models.FileField(upload_to='') PRECISO TESTAR ISSO COM O FORMS
    bio = models.CharField(max_length=200)