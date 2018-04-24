from django.db import models

# Create your models here.
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.timezone import now


class Specialties(models.Model):
    name = models.CharField(max_length=80, verbose_name="Название")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name


class Subjects(models.Model):
    name = models.CharField(max_length=80, verbose_name="Название")
    specialty = models.ManyToManyField(Specialties, verbose_name="Специальность")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name


class Courses(models.Model):
    name = models.CharField(max_length=80, verbose_name="Название")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name


class Students(models.Model):
    name = models.CharField(max_length=20, verbose_name="Имя")
    surname = models.CharField(max_length=20, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=20, verbose_name="Отчество")

    @property
    def fio(self):
        return "{0} {1} {2}".format(self.surname, self.name, self.patronymic)

    course = models.ForeignKey(Courses, on_delete=models.SET_NULL, null=True, default=True, verbose_name="Курс")
    specialty = models.ForeignKey(Specialties,
                                  on_delete=models.SET_NULL,
                                  null=True,
                                  default=True,
                                  verbose_name="Специальность")

    def __str__(self):
        return self.surname


class Appraisals(models.Model):
    changed_date = models.DateTimeField(default=now, verbose_name="Дата изменения")
    student = models.ForeignKey(Students, on_delete=models.CASCADE, verbose_name="Студент")
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, verbose_name="Предмет")
    rating = models.IntegerField(default=100, verbose_name="Оценка")

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
