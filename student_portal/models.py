from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Announcement(models.Model):
  title = models.CharField(max_length=200)
  date = models.DateField(default=timezone.now)
  contents = models.TextField(max_length=2000)
  sender = models.ForeignKey(User, on_delete=models.CASCADE)

  class Meta:
    ordering = ["-date"]

class MeetingMinute(models.Model):
  date = models.DateField(default=timezone.now)
  contents = models.TextField(max_length=3000)

  class Meta:
    ordering = ["-date"]
  
class UserExtension(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)

  class Meta:
    permissions = [
      ("add_announcement", "User can add or clear announcements"),
      ("add_meeting minute", "User can add meeting minute"),
      ("edit_cursus", "User can edit the Cursus Honorum")
    ]

class Consul(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return(f"{self.user}")

class Praetor(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return(f"{self.user}")

class Quaestor(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return(f"{self.user}")

class Aedile(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return(f"{self.user}")

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
  if created:
    UserExtension.objects.create(user=instance)