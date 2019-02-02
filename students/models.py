from django.db import models

class Student(models.Model):
    name = models.TextField(max_length=40, blank=False, null=False, default=None)
    address = models.TextField(blank=True, null=True, default=None)
    phone = models.TextField(max_length=15, blank=True, null=True, default=None)
    birth = models.DateField(blank=False, null=True, default=None)
    school = models.TextField(blank=True, null=True, default=None)
    money = models.BooleanField(blank=False, null=False, default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"


class StudentImage(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='students_images/')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"


class StudentPassport(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    passport = models.CharField(max_length=20, blank=False, null=True, default=None)
    region = models.TextField(blank=False, null=True, default=None)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = "Паспорт студента"
        verbose_name_plural = "Паспорта студентов"


class StudentAttestatEge(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    attestat = models.CharField(max_length=20, blank=False, null=True, default=None)
    middle = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    ege = models.CharField(max_length=20, blank=False, null=True, default=None)
    lesson = models.CharField(max_length=20, blank=False, null=True, default=None)
    score = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = "Аттестат и ЕГЕ студента"
        verbose_name_plural = "Аттестаты и ЕГЕ студентов"
