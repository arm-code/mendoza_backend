from django.db import models

# Create your models here.
class FornitureCategory(models.Model):
    category_name = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name
    
class Forniture(models.Model):
    type_of_forniture = models.ForeignKey(FornitureCategory, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    total_quantity = models.IntegerField()

    def __str__(self):
        return f"{self.type_of_forniture}"


# LOS SIGUIENTES MODELOS SON PARA EL CARRITO DE COMPRAS

class Client(models.Model):
    name_client = models.CharField(max_length=50, blank=False)
    last_name_client = models.CharField(max_length=50)
    phone = models.CharField(max_length=12, blank=False)

    def __str__(self):
        return self.name_client
    
class Address(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=False)
    street = models.CharField(max_length=50, blank=False)
    number = models.IntegerField(blank=False)
    cologne = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return f"{self.street} {self.number} {self.cologne}"

class Product(models.Model):
    product_name = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=50, blank=False)
    product_cost = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return self.product_name

class FornitureCombos(models.Model):
    description = models.CharField(max_length=50, blank=False)
    cost = models.DecimalField(max_digits=5, decimal_places=2, default=0, blank=False)
    chairs_quantity = models.IntegerField()
    tables_quantity = models.IntegerField()
    type_of_tables = models.ForeignKey(FornitureCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

class ShoppingCart(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False)
    quantity = models.IntegerField(blank=False)    

    def __str__(self):
        return self.client

class PurchaseOrder(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=False)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, blank=False)
    total_cost = models.DecimalField(blank=False, max_digits=5, decimal_places=2)
    deadline = models.DateField(blank=False, default=None)

    def __str__(self):
        return f"{self.client} {self.address} {self.total_cost}"

class DetailedOrder(models.Model):
    order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False)
    quantity = models.IntegerField(default=1, blank=False)
    unit_cost = models.DecimalField(max_digits=5, decimal_places=2, blank=False)

    def __str__(self):
        return self.order