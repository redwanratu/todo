from django.urls import path
from . import views 
app_name='tasks'

urlpatterns = [
    path('',views.index,name='index'),
    path('add/',views.add,name='add'),
    path('update/<int:task_id>',views.update,name='update'),
    path('delete/<int:task_id>',views.delete,name='delete'),
    path('done/<int:task_id>',views.done,name='done'),
]
