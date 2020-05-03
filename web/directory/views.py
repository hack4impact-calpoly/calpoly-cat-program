from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect 

from .forms import IntakeForm 
from .models import Cat

def index(request):
    cats = Cat.objects.all()
    return render(request, 'landing.html', {'cats': cats})

def cat_profile(request):
    cat_id = request.GET.get('id')
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cat_profile.html', {'cat': cat})

def help(request):
    return render(request, 'help.html')

def intake_form(request):
    if request.method == 'POST':
        form = IntakeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            cat = Cat(
                    name = data.get('name'),
                    gender = data.get('gender'),
                    age = data.get('age'),
                    description = data.get('description'),
                    breed = data.get('breed'),
                    itype = data.get('itype'),
                    status = data.get('status'),
                    arrival_date = data.get('arrival_date'),
                    arrival_details = data.get('arrival_details'),
                    medical_history = data.get('medical_history'),
                    vaccinations = data.get('vaccinations'),
                    is_microchipped = data.get('is_microchipped'),
                    flea_control_date = data.get('flea_control_date'),
                    deworming_date = data.get('deworming_date'),
                    fiv_felv_date = data.get('fiv_felv_date'),
                    special_needs = data.get('special_needs'),
                    personality = data.get('personality'),
                    more_personality = data.get('more_personality'),
                    comments = data.get('comments'),
                    personal_exp = data.get('personal_exp'))

            cat.save()
        return HttpResponseRedirect('/cat/?id=' + cat.id)
    else:
        form = IntakeForm()
        return render(request, 'intake.html', {'form': form})
