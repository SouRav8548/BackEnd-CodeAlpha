from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/menu/', views.menu_view, name='menu'),
    path('api/orders/create/', views.create_order, name='create_order'),
    path('api/tables/', views.check_tables, name='check_tables'),
    path('api/inventory/update/', views.update_inventory, name='update_inventory'),
    path('api/reports/daily/', views.daily_report, name='daily_report'),
    path('api/alerts/low-stock/', views.low_stock_alert, name='low_stock_alert'),
]