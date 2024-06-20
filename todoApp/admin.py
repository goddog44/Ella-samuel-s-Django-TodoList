from django.contrib import admin
from .models import Task, Tag, DiaryEntry
from django.contrib.admin import TabularInline


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'due_date')
    list_filter = ('status', 'due_date')
    search_fields = ('title', 'description')

class TagAdmin(admin.ModelAdmin):
    list_display = ('tag_name', 'slug')  # Use 'tag_name' instead of 'name'
    prepopulated_fields = {'slug': ('tag_name',)}  # Use 'tag_name' instead of 'name'

admin.site.register(Task, TaskAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.site_header = 'To-Do List Administration'
admin.site.site_title = 'To-Do List Admin'
admin.site.index_title = 'Welcome to To-Do List'


class TagInline(TabularInline):
     model = DiaryEntry.tags.through
     extra = 1  # Add an extra empty tag field

class DiaryEntryAdmin(admin.ModelAdmin):
     list_display = ('title', 'created_at', 'updated_at')
     search_fields = ('title', 'content')
     inlines = [TagInline]
     prepopulated_fields = {'slug': ('title',)}

admin.site.register(DiaryEntry, DiaryEntryAdmin)
