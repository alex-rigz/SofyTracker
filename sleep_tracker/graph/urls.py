from django.urls import path

from .views import graph_sleep

app_name = 'graph'

urlpatterns = [
    path("graph/", graph_sleep, name="graph"),
]
