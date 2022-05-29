from django.contrib import admin
from .models import MeetingMinute, Announcement, UserExtension, Consul, Praetor, Quaestor, Aedile

# Register your models here.
admin.site.register(MeetingMinute)
admin.site.register(Announcement)
admin.site.register(UserExtension)
admin.site.register(Consul)
admin.site.register(Praetor)
admin.site.register(Quaestor)
admin.site.register(Aedile)