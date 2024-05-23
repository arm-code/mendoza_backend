from django.db import models

# Create your models here.


class FornitureCategory(models.Model):
    category_name = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Forniture(models.Model):
    type_of_forniture = models.ForeignKey(
        FornitureCategory, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    total_quantity = models.IntegerField()

    def __str__(self):
        return f"{self.type_of_forniture}"


class FornitureCombos(models.Model):
    description = models.CharField(max_length=50, blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0, blank=False)
    chairs_quantity = models.IntegerField()
    tables_quantity = models.IntegerField()
    type_of_tables = models.ForeignKey(FornitureCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

# LOS SIGUIENTES MODELOS SON PARA EL CARRITO DE COMPRAS

class Customer(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)

    def __str__(self):
        return f"{self.name} {self.last_name}"

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"Cart of {self.customer.name} containing {self.quantity} of {self.product.name}"

class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    street = models.CharField(max_length=50)
    colony = models.CharField(max_length=50)
    number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.street}, {self.colony}, {self.number}"

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=7, decimal_places=2)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    deadline = models.DateTimeField()

    def __str__(self):
        return f"Order {self.id} by {self.customer.name}"

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f"Order Detail {self.id} for {self.product.name} (Quantity: {self.quantity})"
