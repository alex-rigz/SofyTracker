import datetime
from django.db import models
from django.utils import timezone


class Datesw(models.Model):
    dayoftheweek = models.CharField(max_length=20)
    datecurrent = models.DateTimeField('date')

class Actions(models.Model):
    action = models.CharField(max_length=200)
    action_ru_name = models.CharField(max_length=200)
    date_time = models.DateTimeField("action date and time")
    datecurrent = models.ForeignKey(Datesw, on_delete=models.CASCADE, related_name='date')
    def __str__(self):
        return self.action
    def was_published_recently(self):
        return self.date_time >= timezone.now() - datetime.timedelta(days=1)
    
class Buttons_text(models.Model):
    button_text = models.CharField(max_length=2000)
    action_ru_name = models.CharField(max_length=200)
    def __str__(self):
        return self.button_text
    
class Actions_deltas(models.Model):
    deltatime = models.FloatField('time deltas')
    datecurrent = models.ForeignKey(Datesw, on_delete=models.CASCADE, related_name='current_date')

class Graph_data(models.Model):
    datecurrent = models.ForeignKey(Datesw, on_delete=models.CASCADE, related_name='graph_date')
    start_time = models.ForeignKey(Actions, on_delete=models.CASCADE, related_name='start_time')
    finish_time = models.ForeignKey(Actions, on_delete=models.CASCADE, related_name='finish_time')

