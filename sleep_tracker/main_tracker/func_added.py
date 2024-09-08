from django.core.paginator import Paginator
import pytz # type: ignore
import locale

from .models import Actions, Actions_deltas, Datesw, Graph_data
from datetime import datetime as dt
from datetime import timedelta as td


local_tz = pytz.timezone('Europe/Moscow')

def total_seconds(td):
    seconds = (td.microseconds + 
               (td.seconds + td.days * 24 * 3600) * 10**6) / 10**6
    return seconds

def current_day_delta():
    daycurrent = dt.now().astimezone(local_tz)-td(days=1)
    return daycurrent

def datecurrent_calc(date):
    try:
        locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')  # Для Unix/Linux
    except locale.Error:
        try:
            locale.setlocale(locale.LC_TIME, 'russian')  # Для Windows
        except locale.Error:
            # В случае если локаль не установлена
            return "Ошибка: локаль русского языка"
        
    if Datesw.objects.filter(datecurrent=date):
        return Datesw.objects.get(datecurrent=date)
    else:
        str_date_time = dt.now().strftime('%a')
        Datesw.objects.create(dayoftheweek=str_date_time,datecurrent=date)
        new_pk = Datesw.objects.latest('id')
    return new_pk

def craete_graph(action, date_w):
    last_sleep = Actions.objects.filter(action='sleep').latest('date_time')
    last_awake = Actions.objects.filter(action='awake').latest('date_time')
    if action == 'awake':
        Graph_data.objects.create(
            datecurrent=datecurrent_calc(date_w),
            start_time=last_sleep,
            finish_time=last_awake)
    else: pass
    
def paginator(request, object):
    paginator = Paginator(object, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj

def deltas_calc(datecurrent):
    all_times = Graph_data.objects.filter(datecurrent__datecurrent=datecurrent).order_by('-id')

    total_delta = td()
    for i in all_times:
        start = i.start_time.date_time
        finish = i.finish_time.date_time
        delta = finish - start
        #sec_delta = total_seconds(delta)
        total_delta =+ delta # type: ignore

    base_datetime = dt(1970, 1, 1)  # Базовая дата
    total_time_as_datetime = base_datetime + total_delta

    return total_time_as_datetime

