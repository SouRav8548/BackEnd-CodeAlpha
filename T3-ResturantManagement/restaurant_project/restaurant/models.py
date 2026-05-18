from django.db import models

# Create your models here.

class MenuItem(models.Model):
    """Represents a dish on our restaurant menu"""
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=50)  # Like "Appetizer", "Main Course", "Dessert"
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.name} - ${self.price}"
    
    
class Table(models.Model):
    """Represents a table in our restaurant"""
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()  # How many people can sit here
    is_active = models.BooleanField(default=True)  # Is this table usable?
    
    def __str__(self):
        return f"Table {self.table_number} (Seats {self.capacity})"

class Reservation(models.Model):
    """Represents a customer's table reservation"""
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=15)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    party_size = models.IntegerField()
    
    def __str__(self):
        return f"{self.customer_name} - Table {self.table.table_number} on {self.reservation_date}"
    


class Order(models.Model):
    """Represents a customer's food order"""
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PREPARING', 'Preparing'),
        ('READY', 'Ready'),
        ('SERVED', 'Served'),
        ('PAID', 'Paid'),
    ]
    
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True)
    customer_name = models.CharField(max_length=100)
    items = models.ManyToManyField(MenuItem, through='OrderItem')
    total_amount = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Order #{self.id} - {self.customer_name}"

class OrderItem(models.Model):
    """Represents each item within an order"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    item_price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return f"{self.quantity}x {self.menu_item.name}"

class InventoryItem(models.Model):
    """Represents ingredients in our kitchen"""
    name = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=20)  # Like "kg", "liters", "pieces"
    reorder_level = models.DecimalField(max_digits=10, decimal_places=2)
    last_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} - {self.quantity} {self.unit}"
    
    
    

