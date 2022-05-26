from django.db import models
import random

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.title

class Negocios(models.Model):
    name = models.CharField(max_length=100)
    cat_name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to ='uploads/', blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=255)
    mail = models.EmailField(max_length = 254)
    description = models.TextField()

    def __str__(self):
        return self.name


class Competencia(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to ='uploads/', blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']
    def __str__(self):
        return self.title

def random_string():
      return str(random.randint(1000000, 99999999))

class Producto(models.Model):
    name = models.CharField(max_length=155)
    description = models.TextField()
    price = models.IntegerField()
    negocio_parent = models.ForeignKey(Negocios, on_delete=models.CASCADE, null=True)
    buy_order = models.CharField(default=random_string, max_length=100)
    session_id = models.CharField(default=random_string, max_length=100)

    def __str__(self):
        return self.name
