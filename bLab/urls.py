from django.conf.urls import url
from . import views
#from jchart.views import ChartView

#line_chart = 1 #LineChart1()
#line_chart2 = 2 #LineChart2()

urlpatterns = [
    url(r'^single_patient_search/', views.single_patient_search, name='single_patient_search'),
    url(r'^single_patient_BR/(?P<first_name>.*?)/(?P<last_name>.*?)/(?P<gender>.*?)/(?P<age1>.*?)/(?P<age2>.*?)/(?P<search_word_1>.*?)/(?P<search_word_2>.*?)/(?P<search_word_3>.*?)/(?P<search_word_4>.*?)/(?P<search_word_5>.*?)/', views.single_query, name='single_query'),
    url(r'^group_compar/', views.group_compar, name='group_compar'),
    url(r'^group_report/(?P<genderG1>.*?)/(?P<age1G1>.*?)/(?P<age2G1>.*?)/(?P<key1G1>.*?)/(?P<key2G1>.*?)/(?P<key3G1>.*?)/(?P<key4G1>.*?)/(?P<key5G1>.*?)/(?P<genderG2>.*?)/(?P<age1G2>.*?)/(?P<age2G2>.*?)/(?P<key1G2>.*?)/(?P<key2G2>.*?)/(?P<key3G2>.*?)/(?P<key4G2>.*?)/(?P<key5G2>.*?)/(?P<genderG3>.*?)/(?P<age1G3>.*?)/(?P<age2G3>.*?)/(?P<key1G3>.*?)/(?P<key2G3>.*?)/(?P<key3G3>.*?)/(?P<key4G3>.*?)/(?P<key5G3>.*?)/', views.groups_query, name='groups_query'),
    url(r'^upload_page', views.uploadPage, name='uploadPage'),
    url(r'^upload/', views.upload, name="upload"),
    url(r'^deleteDB/', views.deleteDB, name="deleteDB"),
    #url(r'^charts/line_chart/$', ChartView.from_chart(line_chart), name='line_chart'),
    #url(r'^charts/line_chart2/$', ChartView.from_chart(line_chart2), name='line_chart2'),
    url(r'^$', views.home, name='home'),
]

