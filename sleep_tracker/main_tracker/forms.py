from django import forms

from .models import Buttons_text, Actions

class ButtonEditor(forms.ModelForm):
    
    class Meta:
        model = Buttons_text
        fields = ("button_text",'action_ru_name')
        labels = {
            "button_text": ("action name"), 'action_ru_name': ('Читаемое название')
        }

class ActionsEditor(forms.ModelForm):
    
    class Meta:
        model = Actions
        fields = ('date_time',)
        labels = {
            'date_time': ('Дата и время'),
        }