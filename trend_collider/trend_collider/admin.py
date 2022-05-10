from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, Weigh_In, Stock_Pick

# Register your models here.

# admin.site.register(User, UserAdmin)

admin.site.register(Account)
admin.site.register(Weigh_In)
admin.site.register(Stock_Pick)
