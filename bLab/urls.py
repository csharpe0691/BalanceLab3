from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^selector/', views.selector, name='selector'),
    url(r'^selection/', views.initialize, name='initialize'),
    url(r'^single_patient_search/', views.single_patient_search, name='single_patient_search'),
    url(r'^single_patient_BR/', views.single_patient_BR, name='single_patient_BR'),
    url(r'^group_compar/', views.group_compar, name='group_compar'),
    url(r'^group_report/', views.group_report, name='group_report'),
    #url(r'^sample_plot/$', views.samplePlot, name= 'samplePlot'),
    url(r'^pick_file/', views.pickFile, name='pickFile'),
    url(r'^$', views.home, name='home')
]
