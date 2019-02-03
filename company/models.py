from django.db import models
from students.models import Student

class Specialities(models.Model):
    title = models.CharField(max_length=256, blank=True, null=True, default=None)

    def __str__(self):
        return "Специализация %s" % self.title

    class Meta:
        verbose_name = "Специализация"
        verbose_name_plural = "Специализации"

class Contract(models.Model):
    about = models.TextField(blank=True, null=True, default=None)

    def __str__(self):
        return "Контаркт %s" % self.id

    class Meta:
        verbose_name = "Контаркт"
        verbose_name_plural = "Контаркты"


class Profile(models.Model):
    id_student = models.ForeignKey(Student, on_delete=models.DO_NOTHING, default=0)
    faculty = models.CharField(max_length=100, blank=False, default=None)
    speciality = models.ForeignKey(Specialities, on_delete=models.DO_NOTHING)
    registar = models.CharField(max_length=100, blank=False, default=None)
    talk = models.BooleanField(default=False)
    result = models.IntegerField(default=0)
    payment = models.BooleanField(default=False)
    type = models.IntegerField(default=0)
    contract_bool = models.BooleanField(default=False)
    contract = models.ForeignKey(Contract, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "Профиль %s" % self.id

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
