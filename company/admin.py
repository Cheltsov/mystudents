from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Profile._meta.fields]

    class Meta:
        model = Profile

admin.site.register(Profile, ProfileAdmin)


class ContractAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Contract._meta.fields]

    class Meta:
        model = Contract

admin.site.register(Contract, ContractAdmin)


class SpecialitiesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Specialities._meta.fields]

    class Meta:
        model = Specialities

admin.site.register(Specialities, SpecialitiesAdmin)