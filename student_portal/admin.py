from django.contrib import admin
from .models import MeetingMinute, Announcement, UserExtension

# Register your models here.
admin.site.register(MeetingMinute)
admin.site.register(Announcement)
admin.site.register(UserExtension)