from django.contrib import admin
from .models import MeetingMinute, Announcement

# Register your models here.
admin.site.register(MeetingMinute)
admin.site.register(Announcement)