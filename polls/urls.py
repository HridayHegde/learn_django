from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('',views.index,name="index"),
    path('users',views.listofusers,name="users"),
    path('form',views.show_form,name="form"),
    path('adduser',views.add_user, name="adduser"),
]
