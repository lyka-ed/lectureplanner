from django.urls import path

from . import views

urlpatterns = [ 
      path('<int:id>',views.details, name="details"),
      path('labs',views.labs_list, name='labs_list'),
      path('form', views.form, name='form')
]
