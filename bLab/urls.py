from django.conf.urls import url
from . import views
from bLab.views import LineChart
from jchart.views import ChartView
line_chart = LineChart()


urlpatterns = [
    url(r'^single_patient_search/', views.single_patient_search, name='single_patient_search'),
    url(r'^single_patient_BR/', views.single_patient_BR, name='single_patient_BR'),
    url(r'^group_compar/', views.group_compar, name='group_compar'),
    url(r'^group_report/', views.group_report, name='group_report'),
    url(r'^upload_page', views.uploadPage, name='uploadPage'),
    url(r'^upload/', views.upload, name="upload"),
    url(r'^charts/line_chart/$', ChartView.from_chart(line_chart), name='line_chart'),
    url(r'^$', views.home, name='home'),
]

