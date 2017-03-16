from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # eg: /polls/4/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name="detail"),
    # eg: /polls/4/results/
    url(r'^(?P<question_id>[0-9]+)/results/', views.results, name="results"),
]
