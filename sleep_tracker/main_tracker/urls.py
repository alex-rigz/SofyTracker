from django.urls import path, include

from . import views

app_name = 'main_tracker'

urlpatterns = [
    path("", views.index, name="index"),
    path("filter/<str:button_action>/", views.index_filter, name="index_filter"),
    path('graph/', include('graph.urls', namespace='graph')),
    path("action/", views.trackview, name="trackview"), # type: ignore
    path("edit_actions/", views.edit_actions, name="edit_actions"),
    path("edit_actions_delete/<int:action_id>/", views.edit_actions_delete, name="edit_actions_delete"),
    path("edit_actions_edit/<int:action_id>/", views.edit_actions_edit, name="edit_actions_edit"),
    path("settings_main/", views.settings_main, name="settings_main"),
    path("settings_add/", views.settings_add, name="settings_add"),
    path("settings_edit/<int:button_id>/", views.settings_edit, name="settings_edit"),
    path("settings_delete/<int:button_id>/", views.settings_delete, name="settings_delete"),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
]
