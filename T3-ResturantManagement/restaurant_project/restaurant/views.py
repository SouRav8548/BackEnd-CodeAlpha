from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import MenuItem, Table, Order, OrderItem, InventoryItem, Reservation
from django.views.decorators.csrf import csrf_exempt
from django.db import models
import json
from decimal import Decimal

def home(request):
    """The main page of our restaurant system"""
    return render(request, 'restaurant/home.html')

def menu_view(request):
    """Display all available menu items"""
    items = MenuItem.objects.filter(is_available=True)
    menu_data = []
    for item in items:
        menu_data.append({
            'id': item.id,
            'name': item.name,
            'description': item.description,
            'price': str(item.price),
            'category': item.category,
        })
    return JsonResponse({'menu': menu_data})

@csrf_exempt
def create_order(request):
    """Handle placing a new order"""
    if request.method == 'POST':
        data = json.loads(request.body)
        
        # Create the order
        order = Order.objects.create(
            table_id=data['table_id'],
            customer_name=data['customer_name'],
            total_amount=0  # We'll calculate this
        )
        
        total = Decimal('0.00')
        
        # Add items to the order
        for item_data in data['items']:
            menu_item = MenuItem.objects.get(id=item_data['menu_item_id'])
            quantity = item_data['quantity']
            item_price = menu_item.price * quantity
            
            OrderItem.objects.create(
                order=order,
                menu_item=menu_item,
                quantity=quantity,
                item_price=item_price
            )
            
            total += item_price
        
        # Update the order total
        order.total_amount = total
        order.save()
        
        return JsonResponse({
            'message': 'Order placed successfully!',
            'order_id': order.id,
            'total': str(total)
        })

def check_tables(request):
    """Show which tables are available"""
    tables = Table.objects.filter(is_active=True)
    table_data = []
    
    for table in tables:
        # Check if table has an active reservation or unpaid order
        has_active_order = Order.objects.filter(
            table=table
        ).exclude(status__in=['SERVED', 'PAID']).exists()
        
        table_data.append({
            'id': table.id,
            'table_number': table.table_number,
            'capacity': table.capacity,
            'is_available': not has_active_order
        })
    
    return JsonResponse({'tables': table_data})

@csrf_exempt
def update_inventory(request):
    """Update inventory when ingredients are used"""
    if request.method == 'POST':
        data = json.loads(request.body)
        item = InventoryItem.objects.get(id=data['item_id'])
        
        if data['action'] == 'use':
            item.quantity -= Decimal(str(data['amount']))
        elif data['action'] == 'restock':
            item.quantity += Decimal(str(data['amount']))
        
        item.save()
        
        # Check if we need to reorder
        alert = ""
        if item.quantity <= item.reorder_level:
            alert = f"⚠️ Low stock alert! Only {item.quantity} {item.unit} of {item.name} remaining!"
        
        return JsonResponse({
            'message': 'Inventory updated!',
            'current_quantity': str(item.quantity),
            'alert': alert
        })

def daily_report(request):
    """Generate a simple daily sales report"""
    from datetime import datetime, timedelta
    today = datetime.now().date()
    
    orders_today = Order.objects.filter(created_at__date=today)
    total_sales = sum(order.total_amount for order in orders_today)
    
    return JsonResponse({
        'date': str(today),
        'total_orders': orders_today.count(),
        'total_sales': str(total_sales),
    })

def low_stock_alert(request):
    """Check for items that need reordering"""
    low_items = InventoryItem.objects.filter(quantity__lte=models.F('reorder_level'))
    alerts = []
    
    for item in low_items:
        alerts.append({
            'item': item.name,
            'current_quantity': str(item.quantity),
            'unit': item.unit,
            'reorder_level': str(item.reorder_level),
        })
    
    return JsonResponse({'low_stock_items': alerts})