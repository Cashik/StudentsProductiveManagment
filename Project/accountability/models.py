from django.db import models

# Create your models here.
from django.utils.timezone import now


class Subject(models.Model):
    name = models.CharField(max_length=80)


class Specialties(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Students(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    patronymic = models.CharField(max_length=20)

    @property
    def fio(self):
        return "{0} {1} {2}".format(self.surname, self.name, self.patronymic)

    course = models.IntegerField(default=1)
    specialty = models.ForeignKey(Specialties, on_delete=models.SET_NULL, null=True, default=True)


class Session(models.Model):
    data = models.DateField(default=now)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    rating = models.IntegerField(default=100)

    # TODO: оценка в шкале А,B,C. . .
    '''
    @property
    def grade(self):
        if self.rating >= 90:
            return 'A'
        elif
    '''
    pass
