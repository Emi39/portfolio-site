from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User, Group
from unfold.admin import ModelAdmin
from .models import Project, Tag, Profile, ContactMessage

# Unregister default User/Group to use Unfold if desired, or just register our apps
admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    pass

@admin.register(Group)
class GroupAdmin(ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    list_display = ('title', 'short_description', 'is_featured', 'created_at')
    list_filter = ('is_featured', 'tags')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('tags',)

@admin.register(Profile)
class ProfileAdmin(ModelAdmin):
    list_display = ('name', 'title', 'email')
    
    def has_add_permission(self, request):
        # Allow only one profile usually, but for now simple logic
        if Profile.objects.exists():
             return False
        return True

@admin.register(ContactMessage)
class ContactMessageAdmin(ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
