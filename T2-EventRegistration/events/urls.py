from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.event_list, name='home'),
    
    # Event URLs
    path('events/', views.event_list, name='event_list'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('event/<int:event_id>/register/', views.register_for_event, name='register'),
    path('event/<int:event_id>/cancel/', views.cancel_registration, name='cancel_registration'),
    
    # User URLs
    path('register/', views.register_user, name='register'),
    path('my-registrations/', views.my_registrations, name='my_registrations'),
]