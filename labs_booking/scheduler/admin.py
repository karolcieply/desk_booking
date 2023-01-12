from django.contrib import admin

from labs_booking.scheduler.models import Issue, Session

# Register your models here.
admin.site.register(Session)
admin.site.register(Issue)
