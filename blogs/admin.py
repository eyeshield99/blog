from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Blog

admin.site.register(Blog)

admin.site.unregister(Group)

admin.site.site_header = "Chester's World Admin"
admin.site.site_title = "Chester's World Admin Portal"
admin.site.index_title = "Welcome to Chester's World Admin Portal"
