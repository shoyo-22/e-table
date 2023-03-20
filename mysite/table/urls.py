from django.urls import path

from . import views

app_name = 'table'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:day_id>/', views.detail, name='detail'),
]
