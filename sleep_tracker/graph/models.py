from django.db import models
from django.contrib.auth.models import User

class Graph(models.Model):
    name = models.CharField(max_length=200) 
    start_date = models.DateField()
    responsible = models.ForeignKey(User, on_delete=models.CASCADE)
    finish_date = models.DateField()


    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        print(self.start_date.isocalendar()[1])
        super().save(*args, **kwargs)
