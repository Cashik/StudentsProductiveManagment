# Create your views here.
import json
from time import strftime

from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

from accountability.forms import SpecialtyForm, StudentForm, CourseForm, SubjectForm, AppraisalForm
from .models import Specialties, Students, Courses, Subjects, Appraisals


# Specialties --------------------------------------------------------------

def specialties(request):
    return render(request, 'accountability/Spec/spec_list.html', {})


def specialties_as_json(request):
    data = Specialties.objects.all().values('id', 'name', 'description')
    data = json.dumps({"data": list(data)})
    print(data)
    return HttpResponse(data, content_type='application/json')


@csrf_exempt
def save_specialty_form(request, form, template_name, modal_title):
    data = dict()
    print(request.path.split('/'))
    if request.method == 'POST':
        if request.path.split('/')[-2] == 'delete':
            form.instance.delete()
            data['form_is_valid'] = True
        else:
            # add,edit
            if form.is_valid():
                form.save()
                data['form_is_valid'] = True
            else:
                data['form_is_valid'] = False

    context = {'form': form, 'modal_title': modal_title, 'url': request.path}
    data['html_form'] = render_to_string(template_name, context, request=request, )
    return JsonResponse(data)


@csrf_exempt
def specialty_create(request):
    if request.method == 'POST':
        form = SpecialtyForm(request.POST)
    else:
        form = SpecialtyForm()
    return save_specialty_form(request,
                               form,
                               'accountability/particle/modal.html',
                               'Добавить специальность')


@csrf_exempt
def specialty_update(request):
    if request.method == 'POST':
        spec = get_object_or_404(Specialties, pk=request.POST['id'])
        form = SpecialtyForm(request.POST, instance=spec)
    else:
        spec = get_object_or_404(Specialties, pk=request.GET['id'])
        form = SpecialtyForm(instance=spec)
    return save_specialty_form(request,
                               form,
                               'accountability/particle/modal.html',
                               'Изменить специальность')


@csrf_exempt
def specialty_delete(request):
    if request.method == 'POST':
        spec = get_object_or_404(Specialties, pk=request.POST['id'])
        form = SpecialtyForm(request.POST, instance=spec)
    else:
        spec = get_object_or_404(Specialties, pk=request.GET['id'])
        form = SpecialtyForm(instance=spec)
    return save_specialty_form(request,
                               form,
                               'accountability/particle/modal.html',
                               'Удалить специальность?')


# Students --------------------------------------------------------------

def students(request):
    return render(request, 'accountability/Students/students_list.html', {})


def students_list_json(request):
    data = Students.objects.all().values('id', 'name', 'surname', 'patronymic', 'course', 'specialty')

    for student in data:
        student['fio'] = student['surname'] + ' ' + student['name'] + ' ' + student['patronymic']
        student['specialty_name'] = Specialties.objects.all().filter(id=student['specialty'])[0].name
        student['course_name'] = Courses.objects.all().filter(id=student['course'])[0].name

    data = json.dumps({"data": list(data)})
    return HttpResponse(data, content_type='application/json')


@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
    else:
        form = StudentForm()
    return save_specialty_form(request,
                               form,
                               'accountability/particle/modal.html',
                               'Добавить данные о студенте')


@csrf_exempt
def students_update(request):
    if request.method == 'POST':
        itm = get_object_or_404(Students, pk=request.POST['id'])
        form = StudentForm(request.POST, instance=itm)
    else:
        itm = get_object_or_404(Students, pk=request.GET['id'])
        form = StudentForm(instance=itm)
    return save_specialty_form(request,
                               form,
                               'accountability/particle/modal.html',
                               'Изменить данные о студенте')


@csrf_exempt
def students_delete(request):
    if request.method == 'POST':
        itm = get_object_or_404(Students, pk=request.POST['id'])
        form = StudentForm(request.POST, instance=itm)
    else:
        itm = get_object_or_404(Students, pk=request.GET['id'])
        form = StudentForm(instance=itm)
    return save_specialty_form(request,
                               form,
                               'accountability/particle/modal.html',
                               'Удалить запись?')


# Courses --------------------------------------------------------------

def courses(request):
    return render(request, 'accountability/Courses/courses_list.html', {})


def courses_list_json(request):
    data = Courses.objects.all().values('id', 'name', 'description')
    data = json.dumps({"data": list(data)})
    return HttpResponse(data, content_type='application/json')


@csrf_exempt
def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
    else:
        form = CourseForm()
    return save_specialty_form(request,
                               form,
                               'accountability/particle/modal.html',
                               'Добавить курс')


@csrf_exempt
def course_update(request):
    if request.method == 'POST':
        itm = get_object_or_404(Courses, pk=request.POST['id'])
        form = CourseForm(request.POST, instance=itm)
    else:
        itm = get_object_or_404(Courses, pk=request.GET['id'])
        form = CourseForm(instance=itm)
    return save_specialty_form(request,
                               form,
                               'accountability/particle/modal.html',
                               'Изменить курс')


@csrf_exempt
def course_delete(request):
    if request.method == 'POST':
        itm = get_object_or_404(Courses, pk=request.POST['id'])
        form = CourseForm(request.POST, instance=itm)
    else:
        itm = get_object_or_404(Courses, pk=request.GET['id'])
        form = CourseForm(instance=itm)
    return save_specialty_form(request,
                               form,
                               'accountability/particle/modal.html',
                               'Удалить курс?')


# Subjects --------------------------------------------------------------

def subjects(request):
    return render(request, 'accountability/Subject/subjects_list.html', {})


def subjects_list_json(request):
    data = []

    for subject in Subjects.objects.all():
        s = {'id': subject.id, 'name': subject.name, 'description': subject.description}
        subject_specialties = list(subject.specialty.all().values('name'))
        print(subject_specialties)
        s['specialties'] = ', '.join([subject_specialty['name'] for subject_specialty in subject_specialties])
        data.append(s)

    data = json.dumps({"data": data})
    return HttpResponse(data, content_type='application/json')


@csrf_exempt
def subject_create(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
    else:
        form = SubjectForm()
    return save_specialty_form(request,
                               form,
                               'accountability/particle/modal.html',
                               'Добавить курс')


@csrf_exempt
def subject_update(request):
    if request.method == 'POST':
        itm = get_object_or_404(Subjects, pk=request.POST['id'])
        form = SubjectForm(request.POST, instance=itm)
    else:
        itm = get_object_or_404(Subjects, pk=request.GET['id'])
        form = SubjectForm(instance=itm)
    return save_specialty_form(request,
                               form,
                               'accountability/particle/modal.html',
                               'Изменить курс')


@csrf_exempt
def subject_delete(request):
    if request.method == 'POST':
        itm = get_object_or_404(Subjects, pk=request.POST['id'])
        form = SubjectForm(request.POST, instance=itm)
    else:
        itm = get_object_or_404(Subjects, pk=request.GET['id'])
        form = SubjectForm(instance=itm)
    return save_specialty_form(request,
                               form,
                               'accountability/particle/modal.html',
                               'Удалить курс?')


# Appraisals --------------------------------------------------------------

def appraisals(request):
    return render(request, 'accountability/Appraisals/appraisals_list.html', {})


def appraisals_list_json(request):
    data = Appraisals.objects.all().values('id', 'student', 'subject', 'rating', 'changed_date')

    for appraisal in data:
        appraisal['student_name'] = Students.objects.all().get(id=appraisal['student']).fio
        appraisal['changed_date'] = appraisal['changed_date'].strftime("%Y.%m.%d %H:%M:%S")
        appraisal['subject_name'] = Subjects.objects.all().get(id=appraisal['subject']).name

    data = json.dumps({"data": list(data)})
    return HttpResponse(data, content_type='application/json')


@csrf_exempt
def appraisal_create(request):
    if request.method == 'POST':
        form = AppraisalForm(request.POST)
    else:
        form = AppraisalForm()
    return save_specialty_form(request,
                               form,
                               'accountability/particle/modal.html',
                               'Добавить курс')


@csrf_exempt
def appraisal_update(request):
    if request.method == 'POST':
        itm = get_object_or_404(Appraisals, pk=request.POST['id'])
        form = AppraisalForm(request.POST, instance=itm)
    else:
        itm = get_object_or_404(Appraisals, pk=request.GET['id'])
        form = AppraisalForm(instance=itm)
    return save_specialty_form(request,
                               form,
                               'accountability/particle/modal.html',
                               'Изменить курс')


@csrf_exempt
def appraisal_delete(request):
    if request.method == 'POST':
        itm = get_object_or_404(Appraisals, pk=request.POST['id'])
        form = AppraisalForm(request.POST, instance=itm)
    else:
        itm = get_object_or_404(Appraisals, pk=request.GET['id'])
        form = AppraisalForm(instance=itm)
    return save_specialty_form(request,
                               form,
                               'accountability/particle/modal.html',
                               'Удалить курс?')
