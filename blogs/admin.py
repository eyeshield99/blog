from django.contrib import admin
from django.contrib.auth.models import Group
from django_summernote.admin import SummernoteModelAdmin

from .models import Blog


class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = ("content",)


admin.site.register(Blog, BlogAdmin)

admin.site.unregister(Group)

admin.site.site_header = "Chester's World Admin"
admin.site.site_title = "Chester's World Admin Portal"
admin.site.index_title = "Welcome to Chester's World Admin Portal"
