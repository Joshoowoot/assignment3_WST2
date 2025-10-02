from django.contrib import admin
from .models import Announcement

# Register your models here.

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date_created', 'is_published']
    list_filter = ['is_published', 'date_created', 'author']
    search_fields = ['title', 'content', 'author']
    list_editable = ['is_published']
    date_hierarchy = 'date_created'
    ordering = ['-date_created']
