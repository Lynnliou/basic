#coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse
from djangobasic.models import *
from django.core.paginator import *
from django.utils import timezone
from form import *
import  json
# Create your views here.
def todo_list(request):
    event_list= event.objects.all().order_by('-event_time')
    paginator=Paginator(event_list,3)
    try:
         page = int(request.GET.get('page', 1))
         event_list = paginator.page(page)
    except (PageNotAnInteger,InvalidPage,EmptyPage):
         event_list=paginator.page(1)
    return  render(request,'demo.html',locals())

def event_add(request):
    if request.method == 'POST':
        event_form=add_event(request.POST)
        if event_form.is_valid():
            text=event_form.cleaned_data['event_date']
            event.objects.create(event_context=text,event_time=timezone.now(),event_state=False,update_time=None)
            return redirect('/index/')
        else:
            event_form=add_event()
    return  render(request,'demo.html',locals())

def event_del(request,del_id):
    eventlist = event.objects.get(pk=del_id)
    eventlist.delete()
    flag=True
    return HttpResponse(json.dumps(flag), content_type="application/json")

def event_check(request):
    try:
        event_id = request.GET.get('event_id', None)
        if len(event_id) > 0:
            item = event.objects.get(pk=event_id)
            item.event_state = False if item.event_state else True
            item.save()
        return redirect('/index/')
    except Exception as e:
        print(e)


def event_edit(request):
     try:
        Event_id = request.GET.get('event_id', None)
        E_content = request.GET.get('event', None)
        if len(Event_id)>0 and len(E_content)>0:
           event.objects.filter(id=Event_id).update(event_context=E_content,update_time=timezone.now())
        else:
            pass
        return redirect('/index/')
     except Exception as e:
         print(e)
