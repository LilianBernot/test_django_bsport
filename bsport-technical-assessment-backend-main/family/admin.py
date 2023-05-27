from django.contrib import admin

# Register your models here.
from family.models import Family
from user.models import User

admin.site.register(User)
admin.site.register(Family)