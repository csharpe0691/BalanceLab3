from django.conf.urls import url
from . import views
from bLab.views import LineChart1, LineChart2
from jchart.views import ChartView

line_chart = LineChart1()
line_chart2 = LineChart2()

urlpatterns = [
    url(r'^single_patient_search/', views.single_patient_search, name='single_patient_search'),
    url(r'^single_patient_BR/(?P<first_name>.*?)/(?P<last_name>.*?)/(?P<gender>.*?)/(?P<age1>.*?)/(?P<age2>.*?)/(?P<search_word_1>.*?)/(?P<search_word_2>.*?)/(?P<search_word_3>.*?)/(?P<search_word_4>.*?)/(?P<search_word_5>.*?)/', views.single_query, name='single_query'),
    url(r'^group_compar/', views.group_compar, name='group_compar'),
    url(r'^group_report/', views.group_report, name='group_report'),
    url(r'^upload_page', views.uploadPage, name='uploadPage'),
    url(r'^upload/', views.upload, name="upload"),
    url(r'^charts/line_chart/$', ChartView.from_chart(line_chart), name='line_chart'),
    url(r'^charts/line_chart2/$', ChartView.from_chart(line_chart2), name='line_chart2'),
    url(r'^$', views.home, name='home'),
]

