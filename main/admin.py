from django.contrib import admin
from .models import Subscriber, Service, Organization, UserInfo, Office, Officer
# Register your models here.

admin.site.register(Subscriber)
admin.site.register(Service)
admin.site.register(Organization)
admin.site.register(UserInfo)
admin.site.register(Office)
admin.site.register(Officer)