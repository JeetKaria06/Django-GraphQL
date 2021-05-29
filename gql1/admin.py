from django.contrib import admin
from .models import BankBranches, Banks, Branches
# Register your models here.

admin.site.register(Banks)
admin.site.register(Branches)
admin.site.register(BankBranches)