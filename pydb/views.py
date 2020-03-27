from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from .models import Dancer, Crew, Style
from django.shortcuts import get_object_or_404
from .forms import DancerForm
from django.core.context_processors import csrf

# Create your views here.


def dancer_list(request):
    queryset = Dancer.objects.all()
    context = {'queryset': queryset, 'title': 'Dancers List'}
    return render(request, 'index.html', context)


def dancer_detail(request, id=None):
    instance = get_object_or_404(Dancer, id=id)
    context = {'title': 'Dancer Detail',
               'instance': instance}
    return render(request, 'dancer_detail.html', context)


def dancer_create(request):
    form = DancerForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {'pageTitle': 'Create dancer',
               'form': form,
               'btnValue': 'Create'}
    return render(request, 'dancer_create.html', context)


def dancer_update(request, id=None):
    instance = get_object_or_404(Dancer, id=id)
    form = DancerForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {'pageTitle': 'Update dancer',
               'dancer_name': instance.dancer_name,
               'instance': instance,
               'form': form,
               'btnValue': 'Update'}
    return render(request, 'dancer_create.html', context)
