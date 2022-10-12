from django.urls import path
from todolist.views import render_todolist
from todolist.views import render_login
from todolist.views import render_logout
from todolist.views import register
from todolist.views import render_create
from todolist.views import render_delete
from todolist.views import render_update
from todolist.views import render_json
from todolist.views import add_task


app_name = 'todolist'

urlpatterns = [
    path('', render_todolist, name='render_todolist'),
    path('login/', render_login, name='render_login'),
    path('logout/', render_logout, name='render_logout'),
    path('register/', register, name='register'),
    path('create-task/', render_create, name='render_create'),
    path('delete-task/<str:id>/', render_delete, name='render_delete'),
    path('update-task/<str:id>/', render_update, name='render_update'),
    path('json/', render_json, name = 'render_json'),
    path('add/', add_task, name = 'add_task'),
]