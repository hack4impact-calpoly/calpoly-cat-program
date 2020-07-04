from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect 
from django.db.models import OuterRef, Subquery
from django.contrib.auth import authenticate, login, logout
import datetime
import calendar

from .forms import IntakeForm, DocumentForm, EventForm, PhotoForm, EditForm
from .models import Cat, Document, Photo, Event, FileBackup

def index(request):
    photos = Photo.objects.filter(cat_id=OuterRef('id'))
    cats = Cat.objects.all().annotate(photo=Subquery(photos.values('photo')))

    current_time = datetime.datetime.now()
    start_date = current_time - datetime.timedelta(hours=12)
    end_date = current_time + datetime.timedelta(days=5)
    names = Cat.objects.filter(id=OuterRef('cat_id'))
    events = Event.objects.filter(date__range=(start_date, end_date)).annotate(name=Subquery(names.values('name')))

    return render(request, 'landing.html', {'cats': cats, 'events': events})

def cat_profile(request):
    cat_id = request.GET.get('id')
    cat = Cat.objects.get(id=cat_id)
    photos = Photo.objects.filter(cat_id=cat_id)
    if request.GET.get('action') == "edit":
        form = IntakeForm()
        save = {'title': "Edit "+cat.name+"'s Profile", 'link': '/update_cat/'}
        return render(request, 'intake.html', {'cat': cat, 'form': form, 'save': save, 'photos': photos})
    document_form = DocumentForm()
    documents = Document.objects.filter(cat_id=cat_id)
    return render(request, 'cat_profile.html', {'cat': cat, 'document_form': document_form, 'documents': documents,
        'photos': photos, 'htitle': cat.name})

def help(request):
    return render(request, 'help.html', {'htitle': "Help"})

def events(request):
    now = datetime.datetime.now()
    month = now.month
    year = now.year

    if request.GET.get('m'):
        month = int(request.GET.get('m'))
        year = int(request.GET.get('y'))

    start = datetime.date(year, month, 1)
    end = start + datetime.timedelta(days=calendar.monthrange(year, month)[1])

    dates = []
    for i in range(-2, 3):
        if month+i < 1:
            dates.append(tuple((month+i+12, year-1)))
        elif month+i > 12:
            dates.append(tuple((month+i-12, year+1)))
        else:
            dates.append(tuple((month+i, year)))

    names = Cat.objects.filter(id=OuterRef('cat_id'))
    events = Event.objects.filter(date__range=(start, end)).annotate(name=Subquery(names.values('name'))).order_by('date', 'time')
    
    return render(request, 'events.html', {'events': events, 'dates': dates, 'names': names,
        'htitle': "Events ({0}-{1})".format(month, year%100)})

def single_event(request):
    if request.method == 'POST' and request.user.is_authenticated and request.POST.get('event_id') is None:
        form = EventForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            event = Event(
                    title = data.get('title'),
                    event_type = data.get('event_type'),
                    cat_id = data.get('cat_id'),
                    date = data.get('date'),
                    time = data.get('time'),
                    notes = data.get('notes'))
            event.save()
            return redirect('/event/?id=' + str(event.id))
    if request.method == 'POST' and request.user.is_authenticated and request.POST.get('event_id') is not None:
        form = EventForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Event.objects.filter(id=request.POST.get('event_id')).update(
                    title = data.get('title'),
                    event_type = data.get('event_type'),
                    cat_id = data.get('cat_id'),
                    date = data.get('date'),
                    time = data.get('time'),
                    notes = data.get('notes'))
            return redirect('/event/?id=' + str(request.POST.get('event_id')))
    if request.GET.get('action') == 'add' and request.user.is_authenticated:
        form = EventForm()
        cats = Cat.objects.all()
        return render(request, 'add_event.html', {'form': form, 'cats': cats, 'htitle': "Create Event"})
    if request.GET.get('id') is not None:
        e_id = request.GET.get('id')
        event = Event.objects.get(id=e_id)
        cat = Cat.objects.get(id=event.cat_id)
        if request.GET.get('action') == 'edit':
            cats = Cat.objects.all()
            return render(request, 'edit_event.html', {'event': event, 'cat': cat, 'cats': cats, 'htitle': "Edit: "+event.title})
        return render(request, 'event.html', {'event': event, 'cat': cat, 'htitle': event.title })

    return redirect('/events/')

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
            return HttpResponseRedirect('/cat/?id=' + str(cat.id))
    else:
        form = IntakeForm()
    return render(request, 'intake.html', {'form': form, 'htitle': "Intake Form"})

def update_cat(request):
    if request.method == 'POST' and request.user.is_authenticated:
        form = IntakeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Cat.objects.filter(id=request.POST.get('id')).update(
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
            return HttpResponseRedirect('/cat/?id=' + request.POST.get('id'))
    else:
        return redirect('/')

def document_upload(request):
    cat_id = request.POST.get('cat')
    cat = Cat.objects.get(id=cat_id)
    if request.method == 'POST' and request.user.is_authenticated:
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            document = Document(
                    cat_id = cat_id,
                    document = data.get('document'),
                    name = request.FILES['document'].name,
                    description = data.get('description')
            )
            document.save()

            FileBackup(
                cat_id = cat_id,
                cat_name = cat.name,
                file_title = request.FILES['document'].name,
                url = 'https://cpcp-cats.herokuapp.com/media/documents/cat_{0}/{1}'.format(cat_id, request.FILES['photo'].name)
            ).save()
    return redirect('/cat/?id=' + str(cat_id))

def photo_upload(request):
    cat_id = request.POST.get('cat_id')
    cat = Cat.objects.get(id=cat_id)
    if request.method == 'POST' and request.user.is_authenticated:
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            photo = Photo(
                    cat_id = cat_id,
                    photo = data.get('photo'),
                    description = data.get('description'), 
                    name = request.FILES['photo'].name, #name called by html
            )
            photo.save()

            FileBackup(
                cat_id = cat_id,
                cat_name = cat.name,
                file_title = request.FILES['photo'].name,
                url = 'https://cpcp-cats.herokuapp.com/media/documents/cat_{0}/photos/{1}'.format(cat_id, request.FILES['photo'].name)
            ).save()

    return redirect('/cat/?id=' + str(cat_id))

def delete_document(request):
    doc_id = request.GET.get('id')
    doc = Document.objects.get(id=doc_id)
    cat_id = doc.cat_id
    if not request.user.is_authenticated:
        return redirect('/cat/?id=' + str(cat_id))
    doc.delete()
    return redirect('/cat/?id=' + str(cat_id))

def delete_photo(request):
    photo_id = request.GET.get('id')
    photo = Photo.objects.get(id=photo_id)
    cat_id = photo.cat_id
    if not request.user.is_authenticated:
        return redirect('/cat/?id=' + str(cat_id))
    photo.delete()
    return redirect('/cat/?action=edit&id=' + str(cat_id))

def delete_event(request):
    if not request.user.is_authenticated:
        return redirect('/events/')
    event_id = request.GET.get('id')
    event = Event.objects.get(id=event_id)
    event.delete()
    return redirect('/events/')
