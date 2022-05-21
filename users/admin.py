from django.contrib import admin
from .models import User, Skills, Language


class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'surname', 'age', 'hobby','is_active', 'is_admin',
     'url']
    list_display_links = ['name']
    list_filter = ['is_active', 'is_admin']


class SkillsAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']


class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']

admin.site.register(User, UserAdmin)
admin.site.register(Skills, SkillsAdmin)
admin.site.register(Language, LanguageAdmin)
