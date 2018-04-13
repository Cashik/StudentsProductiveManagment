from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.specialties, name='specialties'),
    url(r'^specialties/list$', views.specialties_as_json, name='specialties_list'),
    url(r'^specialties/create/$', views.specialty_create, name='specialty_create'),
    url(r'^specialties/update/$', views.specialty_update, name='specialty_update'),
    url(r'^specialties/delete/$', views.specialty_delete, name='specialty_delete'),
]
