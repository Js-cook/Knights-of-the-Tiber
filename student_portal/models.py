from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Announcement(models.Model):
  title = models.CharField(max_length=200)
  date = models.DateField(default=timezone.now)
  contents = models.CharField(max_length=2000)
  sender = models.ForeignKey(User, on_delete=models.CASCADE)

  class Meta:
    ordering = ["-date"]

class MeetingMinute(models.Model):
  date = models.DateField(default=timezone.now)
  contents = models.CharField(max_length=3000)

  class Meta:
    ordering = ["-date"]
  