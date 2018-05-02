from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^specialties/$', views.specialties, name='specialties'),
    url(r'^specialties/list$', views.specialties_as_json, name='specialties_list'),
    url(r'^specialties/create/$', views.specialty_create, name='specialty_create'),
    url(r'^specialties/update/$', views.specialty_update, name='specialty_update'),
    url(r'^specialties/delete/$', views.specialty_delete, name='specialty_delete'),

    url(r'^students$', views.students, name='students'),
    url(r'^students/list$', views.students_list_json, name='students_list'),
    url(r'^students/create/$', views.student_create, name='student_create'),
    url(r'^students/update/$', views.students_update, name='student_update'),
    url(r'^students/delete/$', views.students_delete, name='student_delete'),

    url(r'^subjects$', views.subjects, name='subjects'),
    url(r'^subjects/list$', views.subjects_list_json, name='subjects_list'),
    url(r'^subjects/create/$', views.subject_create, name='subject_create'),
    url(r'^subjects/update/$', views.subject_update, name='subject_update'),
    url(r'^subjects/delete/$', views.subject_delete, name='subject_delete'),

    url(r'^courses$', views.courses, name='courses'),
    url(r'^courses/list$', views.courses_list_json, name='courses_list'),
    url(r'^courses/create/$', views.course_create, name='course_create'),
    url(r'^courses/update/$', views.course_update, name='course_update'),
    url(r'^courses/delete/$', views.course_delete, name='course_delete'),

    url(r'^appraisals$', views.appraisals, name='appraisals'),
    url(r'^appraisals/list$', views.appraisals_list_json, name='appraisals_list'),
    url(r'^appraisals/create/$', views.appraisal_create, name='appraisal_create'),
    url(r'^appraisals/update/$', views.appraisal_update, name='appraisal_update'),
    url(r'^appraisals/delete/$', views.appraisal_delete, name='appraisal_delete'),
]
