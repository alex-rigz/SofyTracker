from django.shortcuts import render, redirect
from django.utils import timezone
from django.shortcuts import render


from .models import Actions, Buttons_text
from .forms import ButtonEditor, ActionsEditor
from . import func_added as fnk


def index(request):
    actions_list = (
        Actions.objects.all().order_by('-id')
    )
    context = {
        'button_list': Buttons_text.objects.all(),
        'page_obj': fnk.paginator(request, actions_list),
        'title': 'Трекер малыша',
        'year': timezone.now().date(),
    }
    return render(request, 'tracker/index.html', context)

def index_filter(request, button_action):
    actions_list = (
        Actions.objects.filter(action=button_action).order_by('-id')
    )
    context = {
        'button_list': Buttons_text.objects.all(),
        'page_obj': fnk.paginator(request, actions_list),
        'title': 'Что делает Софушка?',
        'year': timezone.now().date(),
        'button_action':button_action
    }
    return render(request, 'tracker/index.html', context)

def trackview(request):
    if request.method == 'POST':
        action = request.POST.get('name')
        action_ru_name = request.POST.get('name_ru')
        date_time = timezone.now()
        date_w = timezone.now().date()
        Actions.objects.create(action=action, 
                               date_time=date_time, 
                               action_ru_name = action_ru_name, 
                               datecurrent = fnk.datecurrent_calc(date_w))
        fnk.craete_graph(action,date_w)
        return redirect('/')
    else:
        print(f'Действие не найдено')

def edit_actions(request):
    action_list = Actions.objects.all().order_by('-id')
    context = {
        'action_list': action_list,
        'title': 'Редактирование последних действий',
        'year': timezone.now().date(),
    }
    return render(request, 'tracker/edit_actions.html', context)

def edit_actions_edit(request, action_id):
    #  Query the specified data
    action = Actions.objects.get(id=action_id)
    if request.method != 'POST':
      #  If it is not a post, create a form and fill the form with instance=article current data
        form = ActionsEditor(instance=action)  
    else:
    #  If it is post, instance=article fills the form with current data, and uses data=request.POST to get the content in the form
        form = ActionsEditor(instance=action, data=request.POST)
        form.save()  #  save
        if form.is_valid():  #  verification
            return redirect('main_tracker:edit_actions') #  Successful jump
    return render(request, 'tracker/edit_actions_edit.html', {'form':form,'action':action})

def edit_actions_delete(request, action_id):
    action = Actions.objects.get(id=action_id)
    if request.method == 'POST':
        action.delete()
        return redirect('main_tracker:edit_actions')
    return render(request, 'tracker/edit_actions_delete.html', {'action': action})

def settings_main(request):
    buttons_list = Buttons_text.objects.all()
    context = {
        'buttons_list': buttons_list,
        'title': 'Настройки',
        'year': timezone.now().date(),
    }
    return render(request, 'tracker/settings_main.html', context)

def settings_add(request):
    if request.method != 'POST':
        #  Create an empty form to display on the page
        form = ButtonEditor()
    else:
        #  Otherwise, it is POST
        #  The request.POST method will get the data we entered in the form
        new_button = ButtonEditor(request.POST)
        #  To verify its legality, use the is_valid() method
        if new_button.is_valid():
            #  The verification is passed, and the data is saved using the save() method
            new_button.save()
            #  Saved successfully, use redirect() to jump to the specified page
            return redirect('main_tracker:settings_main')
    return render(request, 'tracker/settings_add.html', {'form':form})

#  Edit page
def settings_edit(request, button_id):
    #  Query the specified data
    button = Buttons_text.objects.get(id=button_id)
    if request.method != 'POST':
      #  If it is not a post, create a form and fill the form with instance=article current data
        form = ButtonEditor(instance=button)  
    else:
    #  If it is post, instance=article fills the form with current data, and uses data=request.POST to get the content in the form
        form = ButtonEditor(instance=button, data=request.POST)
        form.save()  #  save
        if form.is_valid():  #  verification
            return redirect('main_tracker:settings_main') #  Successful jump
    return render(request, 'tracker/settings_edit.html', {'form':form,'button':button})

def settings_delete(request, button_id):
    button = Buttons_text.objects.get(id=button_id)
    if request.method == 'POST':
        button.delete()
        return redirect('main_tracker:settings_main')
    return render(request, 'tracker/settings_delete.html', {'button': button})