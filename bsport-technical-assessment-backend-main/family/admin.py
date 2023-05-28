from django.contrib import admin

# Register your models here.
from family.models import Family
from user.models import User

class UserAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('email', 'first_name', 'last_name', 'is_staff')

class FamilyAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('user', 'father', 'mother', 'is_in_relationship', 'relationship', 'child')

admin.site.register(User, UserAdmin)
admin.site.register(Family, FamilyAdmin)