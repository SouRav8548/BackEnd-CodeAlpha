from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    capacity = models.IntegerField(help_text="Maximum number of attendees")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')
    participant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registrations')
    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('event', 'participant')  # A user can register only once per event

    def __str__(self):
        return f"{self.participant.username} -> {self.event.title}"