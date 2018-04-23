from django import forms
from .models import Specialties, Students, Courses, Subjects, Appraisals


class SpecialtyForm(forms.ModelForm):
    class Meta:
        model = Specialties
        fields = ('id', 'name', 'description')


class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ('id', 'name', 'surname', 'patronymic', 'course', 'specialty')


class CourseForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ('id', 'name', 'description')


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = ('id', 'name', 'specialty', 'description')


class AppraisalForm(forms.ModelForm):
    class Meta:
        model = Appraisals
        fields = ('id', 'student', 'subject', 'rating')
