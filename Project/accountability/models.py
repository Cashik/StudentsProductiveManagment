from django.db import models

# Create your models here.
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.timezone import now


class Specialties(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Subjects(models.Model):
    name = models.CharField(max_length=80)
    specialty = models.ManyToManyField(Specialties)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Courses(models.Model):
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

    course = models.ForeignKey(Courses, on_delete=models.SET_NULL, null=True, default=True)
    specialty = models.ForeignKey(Specialties, on_delete=models.SET_NULL, null=True, default=True)

    def __str__(self):
        return self.surname


class Appraisals(models.Model):
    changed_date = models.DateTimeField(default=now)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
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


@receiver(pre_save, sender=Appraisals)
def clear_trigger(sender, instance, *args, **kwargs):
    instance.changed_date = now()
