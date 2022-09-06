from django.db import models

# Create your models here.
class Brand(models.Model):
    brand_name = models.CharField(max_length=200)
    brand_sector = models.CharField(max_length=200)
    brand_contact = models.EmailField()
    
    def __str__(self):
        return self.brand_name
    
class Product(models.Model):
    DAIRY = "DR"
    FRESH = "FR"
    CANNED = "CN"
    MEAT = "MT"
    OTHER = "OT"
    CATEGORY_CHOICES = [
        (DAIRY, "Dairy Product"),
        (FRESH, "Fresh Product"),
        (CANNED, "Canned Product"),
        (MEAT, "Meat, Chicken and Fish Product"),
        (OTHER, "Other Product")
    ]
    
    KG = "KG"
    UNIT = "UN"
    LITRE = "LT"
    UNIT_CHOICES = [
        (KG, "Kilogram"),
        (UNIT, "Unit"),
        (LITRE, "Litre")
    ]
    
    brand = models.ForeignKey(Brand, on_delete = models.CASCADE)
    product_name = models.CharField(max_length=200)
    category = models.CharField(
        max_length = 2,
        choices = CATEGORY_CHOICES,
        default = OTHER
    )
    price = models.FloatField()
    unit = models.CharField(
        max_length = 2,
        choices = UNIT_CHOICES,
        default = UNIT
    )
    barcode = models.IntegerField(unique=True)
    
    def __str__(self):
        return self.product_name

class Supermarket(models.Model):
    supermarket_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    opening_date = models.DateField()
    def __str__(self):
        return self.supermarket_name+" @ "+self.address

class Stock(models.Model):
    supermarket = models.ForeignKey(Supermarket, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    expiry_date = models.DateField()
    number_in_stock = models.IntegerField()
    def __str__(self):
        return self.product.__str__()+": "+str(self.number_in_stock)
    