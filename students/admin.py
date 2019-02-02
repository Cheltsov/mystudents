from django.contrib import admin
from .models import *


class StudentAttestatEgeInline(admin.TabularInline):
    model = StudentAttestatEge
    extra = 1
    max_num = 1


class StudentPassportInline(admin.TabularInline):
    model = StudentPassport
    extra = 1
    max_num = 1


class StudentImageInline(admin.TabularInline):
    model = StudentImage
    extra = 1
    max_num = 1


class StudentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Student._meta.fields]
    inlines = [StudentImageInline, StudentPassportInline, StudentAttestatEgeInline]

    class Meta:
        model = Student

admin.site.register(Student, StudentAdmin)


class StudentImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in StudentImage._meta.fields]

    class Meta:
        model = StudentImage

admin.site.register(StudentImage, StudentImageAdmin)


class StudentPassportAdmin(admin.ModelAdmin):
    list_display = [field.name for field in StudentPassport._meta.fields]

    class Meta:
        model = StudentPassport

admin.site.register(StudentPassport, StudentPassportAdmin)


class StudentAttestatEgeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in StudentAttestatEge._meta.fields]

    class Meta:
        model = StudentAttestatEge

admin.site.register(StudentAttestatEge, StudentAttestatEgeAdmin)
