from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('member/<int:id>/', views.edit),
    path('member/', views.save),
    path('member/<int:id>/delete/', views.delete),
]

