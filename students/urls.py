from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<student_id>\d+)$', views.student, name='student'),

    url(r'^ajax_add_student/$', views.ajax_add_student, name='ajax_add_student'),
]