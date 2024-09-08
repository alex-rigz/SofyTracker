from django.shortcuts import render
from graph.models import Graph
import pandas as pd
from plotly.offline import plot # type: ignore
import plotly.express as px # type: ignore
from main_tracker.models import Graph_data
from main_tracker import func_added as fnk
from datetime import datetime as dt
import pytz # type: ignore
from django.utils import timezone

def graph_sleep(request):
    local_tz = pytz.timezone('Europe/Moscow')

    ds = Graph_data.objects.order_by('datecurrent__datecurrent').filter(
        datecurrent__datecurrent__range=[fnk.current_day_delta(),
                                         dt.now().astimezone(local_tz)])
    
    qs = Graph_data.objects.order_by('-datecurrent__datecurrent').values('datecurrent__dayoftheweek', 'datecurrent__datecurrent').distinct()[:1]

    deltas_data = [
        {
            'Summ': fnk.deltas_calc(day['datecurrent__datecurrent']).strftime('%H часов %M минут'),
            'Day': day['datecurrent__dayoftheweek']
        } for day in qs
    ]
    
    sleep_data = [
        {
            'Start_time': y.start_time.date_time.astimezone(local_tz) ,
            'Finish_time': y.finish_time.date_time.astimezone(local_tz),
            'Day': y.datecurrent.dayoftheweek,
        } for y in ds
    ]
    df = pd.DataFrame(sleep_data)
    fig = px.timeline(
        df, x_start="Start_time", x_end="Finish_time", y='Day', color="Day"
    )
    fig.update_layout(
                      yaxis=dict( 
                      tickformat = '%H:%M:%S',),paper_bgcolor="#6c757d",)
    gantt_plot = plot(fig, output_type="div")
    context = {'plot_div': gantt_plot,
               'deltas_data': deltas_data,
               'title': 'График сна',
               'year': timezone.now().date(),
               }
    return render(request, 'graph.html', context)