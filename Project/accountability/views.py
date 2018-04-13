# Create your views here.
import json

from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

from accountability.forms import SpecialtyForm
from .models import Specialties


def specialties(request):
    return render(request, 'accountability\\specialties_list.html', {})


def specialties_as_json(request):
    data = Specialties.objects.all().values('id', 'name', 'description')
    data = json.dumps({"data": list(data)})
    print(data)
    return HttpResponse(data, content_type='application/json')


@csrf_exempt
def save_specialty_form(request, form, template_name):
    data = dict()

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request, )
    return JsonResponse(data)


@csrf_exempt
def specialty_create(request):
    if request.method == 'POST':
        print(request.POST)
        form = SpecialtyForm(request.POST)
    else:
        form = SpecialtyForm()
    return save_specialty_form(request, form, 'accountability\\partical_spec_create.html')


@csrf_exempt
def specialty_update(request):
    if request.method == 'POST':
        print(request.POST)
        spec = get_object_or_404(Specialties, pk=request.POST['id'])
        form = SpecialtyForm(request.POST, instance=spec)
    else:
        spec = get_object_or_404(Specialties, pk=request.GET['id'])
        print(request.GET)
        form = SpecialtyForm(instance=spec)
    return save_specialty_form(request, form, 'accountability\\partical_spec_update.html')


@csrf_exempt
def specialty_delete(request):
    data = dict()
    if request.method == 'POST':
        spec = get_object_or_404(Specialties, pk=request.POST['id'])
        spec.delete()
        data['form_is_valid'] = True
    else:
        spec = get_object_or_404(Specialties, pk=request.GET['id'])
        #data['form_is_valid'] = False
        context = {'spec': spec}
        data['html_form'] = render_to_string('accountability\\partical_spec_delete.html',
                                             context,
                                             request=request, )
    return JsonResponse(data)
