# SofyTracker
Трекер для малыша - учитываем все важные события

Простой трекер важных событий. 
Возможности приложения: 
1. Добавление собственный действий
2. Построение графика сна (для отображения графика, необходимо добавить действия - sleep, awake)
3. Фильтрация по созданным событиям на главной странице
4. Редактирование добавленных событий

Поддерживается адаптивная верстка

Главный экран:
<img width="327" alt="image" src="https://github.com/user-attachments/assets/31dc5b2c-5011-4214-8b38-8da68dece1e7">

Настраиваемый график сна: 
<img width="330" alt="image" src="https://github.com/user-attachments/assets/1b4f6f1a-6594-4ad7-984d-5964ebc3db1e">

## Установка:
0. Установите python3.10, brew, pip
1. Скопируйте репозиторий
2. Установите виртуальное окружение - python3.10 -m venv venv
3. Активируйте виртуальное окружение - source venv/bin/activate
4. Установите требуемые библиотеки - pip install -r requirements.txt
5. Добавьте админа - python manage.py createsuperuser
6. Сделайте миграцию базы - python manage.py makemigrations , python manage.py migrate
7. Запустите сервер - python manage.py runserver
8. Переходите на локальный адрес - http://127.0.0.1:8000/
9. Сайт будет пустой, для этого сначала нужно создать первые действия, необходимо зайти в настройки и добавить новые действия. Для начала необходимо создать действие awake, затем отдельно sleep - читаемое название по вашему желанию.
10. Трекер запущен и работет

## Настройка графика: 
По желанию можно изменять количество отображаемых дней на графике, для этого необходимо:
1. В папке sleep_tracker/graph - найти файл views.py - на 19 строчке в переменной "qs" - в самом конце изменить цифру на желаемую. Это значение количества возвращаемых объектов дней с подсчетом количества сна. Для изменения количество дней на графике, необходимо перейти в папку sleep_tracker/main_tracker в файл func_added.py - в функции def current_day_delta() изменить количество дней в конце функции td(days=7).
