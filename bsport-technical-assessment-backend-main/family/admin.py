from django.contrib import admin

# Register your models here.
from family.models import Family
from user.models import User

class UserAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('email', 'first_name', 'last_name', 'is_staff')

admin.site.register(User, UserAdmin)
admin.site.register(Family)