from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import Registration

from django.shortcuts import get_object_or_404

from django.shortcuts import render
from .models import Event
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Event, Registration

def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'events/register.html', {'form': form})


def home(request):
    """Home page - redirect to event list"""
    return redirect('event_list')

def event_list(request):
    """Show all upcoming events"""
    events = Event.objects.all().order_by('date')
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, event_id):
    """Show details of a specific event"""
    event = get_object_or_404(Event, id=event_id)
    is_registered = False
    if request.user.is_authenticated:
        is_registered = Registration.objects.filter(
            event=event, 
            participant=request.user
        ).exists()
    
    # Count current registrations
    registration_count = Registration.objects.filter(event=event).count()
    spots_left = event.capacity - registration_count
    
    return render(request, 'events/event_detail.html', {
        'event': event,
        'is_registered': is_registered,
        'spots_left': spots_left,
        'registration_count': registration_count,
    })

@login_required
def register_for_event(request, event_id):
    """Register current user for an event"""
    event = get_object_or_404(Event, id=event_id)
    
    # Check if already registered
    if Registration.objects.filter(event=event, participant=request.user).exists():
        messages.warning(request, 'You are already registered for this event!')
    else:
        # Check if event is full
        current_count = Registration.objects.filter(event=event).count()
        if current_count >= event.capacity:
            messages.error(request, 'Sorry, this event is full!')
        else:
            Registration.objects.create(event=event, participant=request.user)
            messages.success(request, f'Successfully registered for {event.title}!')
    
    return redirect('event_detail', event_id=event.id)

@login_required
def cancel_registration(request, event_id):
    """Cancel user's registration for an event"""
    event = get_object_or_404(Event, id=event_id)
    registration = Registration.objects.filter(event=event, participant=request.user)
    
    if registration.exists():
        registration.delete()
        messages.success(request, f'Registration for {event.title} cancelled.')
    else:
        messages.warning(request, 'You were not registered for this event.')
    
    return redirect('event_detail', event_id=event.id)

@login_required
def my_registrations(request):
    """Show all registrations for the current user"""
    registrations = Registration.objects.filter(
        participant=request.user
    ).select_related('event').order_by('event__date')
    
    return render(request, 'events/my_registrations.html', {
        'registrations': registrations
    })