from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import WeekDay, Subjects


def index(request):
    week_days_list = WeekDay.objects.all()
    context = {'week_days_list': week_days_list}
    print(week_days_list)
    return render(request, 'table/index.html', context)


def detail(request, day_id):
    day = get_object_or_404(WeekDay, pk=day_id)
    subjects = Subjects.objects.filter(day_id=day_id)
    context = {'day': day, 'subjects': subjects}
    return render(request, 'table/detail.html', context)
