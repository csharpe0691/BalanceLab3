from django.contrib.auth.decorators import login_required
from django.contrib import messages

import os
import scipy.io
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from jchart import Chart
from jchart.config import Axes, DataSet
import ast
from rest_pandas import PandasSimpleView
import django_tables2 as tables
import pandas as pd

from bokeh.plotting import figure, output_file, show
from bokeh.embed import components

import pymongo
from pymongo import *

class LineChart1(Chart):
    chart_type ='bubble'
    legend = {
       'display' : False
    }

    def get_datasets(self, **kwargs):
        data = [{'y': 8,'x': 3,'r': 2},
                 {'y': 11,'x': 5,'r': 2},
                 {'y': 12,'x': 8,'r': 2},
                 {'y': 11,'x': 11,'r': 2},
                 {'y': 7,'x': 11,'r': 2},
                 {'y': 6,'x': 14,'r': 2},
                 {'y': 2,'x': 12,'r': 2},
                 {'y': 4,'x': 9,'r': 2},
                 {'y': 3,'x': 6,'r': 2},
                {'y': 8,'x': 3,'r': 2}]
        scales = {
           'xAxes': [Axes(type='linear', position='bottom')],
        }
        return [
            DataSet(type='line',
                    label='Line',
                    borderColor='red',
                    data=data)
        ]

class LineChart2(Chart):
    chart_type ='bubble'
    legend = {
       'display' : False
    }

    data = [{'y': 8,'x': 3,'r': 2},
             {'y': 11,'x': 5,'r': 2},
             {'y': 4,'x': 8,'r': 2},
             {'y': 11,'x': 11,'r': 2},
             {'y': 7,'x': 11,'r': 2},
             {'y': 4,'x': 13,'r': 2},
             {'y': 2,'x': 12,'r': 2},
             {'y': 3,'x': 9,'r': 2},
             {'y': 3,'x': 6,'r': 2},
             {'y': 8,'x': 3,'r': 2}]

    def set_data(self, data_in):
            self.data = data_in

    def get_datasets(self, **kwargs):
        scales = {
           'xAxes': [Axes(type='linear', position='bottom')],
        }
        return [
            DataSet(type='line',
                    label='Line',
                    borderColor='green',
                    data=self.data)
        ]



class single_patient_response_table(tables.Table):
    class Meta:
        attrs = {'width': '80%'}

    row_name = tables.Column(verbose_name='')
    BEO_pt = tables.Column(verbose_name='BEO Pt')
    BEO_ctrls = tables.Column(verbose_name='BEO Ctrls')
    BEO_Pcnt = tables.Column(verbose_name='BEO %')
    BEC_pt = tables.Column(verbose_name='BEC Pt')
    BEC_ctrls = tables.Column(verbose_name='BEC Ctrls')
    BEC_Pcnt = tables.Column(verbose_name='BEC %')
    UEO_pt = tables.Column(verbose_name='UEO Pt')
    UEO_ctrls = tables.Column(verbose_name='UEO Ctrls')
    UEO_Pcnt = tables.Column(verbose_name='UEO %')
    UEC_pt = tables.Column(verbose_name='UEC Pt')
    UEC_ctrls = tables.Column(verbose_name='UEC Ctrls')
    UEC_Pcnt = tables.Column(verbose_name='UEC %')
    BND_pt = tables.Column(verbose_name='BND Pt')
    BND_ctrls = tables.Column(verbose_name='BND Ctrls')
    BND_Pcnt = tables.Column(verbose_name='  BND %')

class SingleResultsView(PandasSimpleView):
    def get_data(self, request, *args, **kwargs):
        return singleResultsdf

@login_required(login_url="login/")
def home(request):
    return render(request,"home.html")

#THIS IS NEW STUFF FOR FILE PICKER!!!!!!
@login_required()
def uploadPage(request):
    return render(request,'upload_page.html', {'what':'BalanceLab File Upload'})


def loadFile(filename):
    mat = scipy.io.loadmat(filename)
    record_doc = {
       'header':mat['__header__'],
       'version':mat['__version__'],
       'globals':mat['__globals__'],
       'patient_id':mat['final'][0][0][0],
       'first_name':mat['final'][1][0][0],
       'last_name':mat['final'][2][0][0],
       'address':mat['final'][3][0][0],
       'city':mat['final'][4][0][0],
       'state':mat['final'][5][0][0],
       'phone':mat['final'][6][0][0],
       'age':mat['final'][7][0][0],
       'gender':mat['final'][8][0][0],
       'search_word_1':mat['final'][9][0][0],
       'search_word_2':mat['final'][10][0][0],
       'search_word_3':mat['final'][11][0][0],
       'search_word_4':mat['final'][12][0][0],
       'search_word_5':mat['final'][13][0][0],
       'feet_size':mat['final'][14][0][0][0],
       'height':int(mat['final'][15][0][0][0]),
       'NSI1':int(mat['final'][17][0][0][0]),
       'NSI2':int(mat['final'][18][0][0][0]),
       'NSI3':int(mat['final'][19][0][0][0]),
       'NSI4':int(mat['final'][20][0][0][0]),
       'NSI5':int(mat['final'][21][0][0][0]),
       'NSI6':int(mat['final'][22][0][0][0]),
       'NSI7':int(mat['final'][23][0][0][0]),
       'NSI8':int(mat['final'][24][0][0][0]),
       'NSI9':int(mat['final'][25][0][0][0]),
       'NSI10':int(mat['final'][26][0][0][0]),
       'NSI11':int(mat['final'][27][0][0][0]),
       'NSI12':int(mat['final'][28][0][0][0]),
       'NSI13':int(mat['final'][29][0][0][0]),
       'NSI14':int(mat['final'][30][0][0][0]),
       'NSI15':int(mat['final'][31][0][0][0]),
       'NSI16':int(mat['final'][32][0][0][0]),
       'NSI17':int(mat['final'][33][0][0][0]),
       'NSI18':int(mat['final'][34][0][0][0]),
       'NSI19':int(mat['final'][35][0][0][0]),
       'NSI20':int(mat['final'][36][0][0][0]),
       'NSI21':int(mat['final'][37][0][0][0]),
       'NSI22':int(mat['final'][38][0][0][0]),
       'NSITOTAL':int(mat['final'][39][0][0][0]),
       'BOSSize':int(mat['final'][40][0][0][0]),
       'cause_of_trauma':mat['final'][41][0][0],
       'number_of_previous_traumas':int(mat['final'][42][0][0][0]),
       'time_first_trauma':int(mat['final'][43][0][0][0]),
       'time_last_trauma':int(mat['final'][44][0][0][0]),
       'BEOAREA':mat['final'][45][0][0][0],
       'BEOSPEEDAP':mat['final'][46][0][0][0],
       'BEOSPEEDML':mat['final'][47][0][0][0],
       'BEORANGEAP':int(mat['final'][48][0][0][0]),
       'BEORANGEML':int(mat['final'][49][0][0][0]),
       'BEORMSAP':int(mat['final'][50][0][0][0]),
       'BEORMSML':int(mat['final'][51][0][0][0]),
       'BEOF50AP':int(mat['final'][52][0][0][0]),
       'BEOF50ML':int(mat['final'][53][0][0][0]),
       'BEOF80AP':int(mat['final'][54][0][0][0]),
       'BEOSENTAP':int(mat['final'][55][0][0][0]),
       'BEOSENTML':int(mat['final'][56][0][0][0]),
       'BEOCROSSSENT':int(mat['final'][57][0][0][0]),
       'BECAREA':mat['final'][58][0][0][0],
       'BECSPEEDAP':mat['final'][59][0][0][0],
       'BECSPEEDML':mat['final'][60][0][0][0],
       'BECRANGEAP':int(mat['final'][61][0][0][0]),
       'BECRANGEML':int(mat['final'][62][0][0][0]),
       'BECRMSAP':int(mat['final'][63][0][0][0]),
       'BECRMSML':int(mat['final'][64][0][0][0]),
       'BECF50AP':int(mat['final'][65][0][0][0]),
       'BECF50ML':int(mat['final'][66][0][0][0]),
       'BECF80AP':int(mat['final'][67][0][0][0]),
       'BECSENTAP':int(mat['final'][68][0][0][0]),
       'BECSENTML':int(mat['final'][69][0][0][0]),
       'BECCROSSSENT':int(mat['final'][70][0][0][0]),
       'UEOAREA':mat['final'][71][0][0][0],
       'UEOSPEEDAP':mat['final'][72][0][0][0],
       'UEOSPEEDML':mat['final'][73][0][0][0],
       'UEORANGEAP':mat['final'][74][0][0][0],
       'UEORANGEML':int(mat['final'][75][0][0][0]),
       'UEORMSAP':int(mat['final'][76][0][0][0]),
       'UEORMSML':int(mat['final'][77][0][0][0]),
       'UEOF50AP':int(mat['final'][78][0][0][0]),
       'UEOF50ML':int(mat['final'][79][0][0][0]),
       'UEOF80AP':int(mat['final'][80][0][0][0]),
       'UEOSENTAP':int(mat['final'][81][0][0][0]),
       'UEOSENTML':int(mat['final'][82][0][0][0]),
       'UEOCROSSSENT':int(mat['final'][83][0][0][0]),
       'UECAREA':int(mat['final'][84][0][0][0]),
       'UECSPEEDAP':mat['final'][85][0][0][0],
       'UECSPEEDML':mat['final'][86][0][0][0],
       'UECRANGEAP':int(mat['final'][87][0][0][0]),
       'UECRANGEML':int(mat['final'][88][0][0][0]),
       'UECRMSAP':int(mat['final'][89][0][0][0]),
       'UECRMSML':int(mat['final'][90][0][0][0]),
       'UECF50AP':int(mat['final'][91][0][0][0]),
       'UECF50ML':int(mat['final'][92][0][0][0]),
       'UECF80AP':int(mat['final'][93][0][0][0]),
       'UECSENTAP':int(mat['final'][94][0][0][0]),
       'UECSENTML':int(mat['final'][95][0][0][0]),
       'UECCROSSSENT':int(mat['final'][96][0][0][0]),
       'BNDRANGEAP':int(mat['final'][97][0][0][0]),
       'BNDRANGEML':int(mat['final'][98][0][0][0]),
       'BNDAREA':int(mat['final'][99][0][0][0]),
       'BEO_COPAP_PROFILE':(mat['final'][100][0][0]).tolist(),
       'BEO_COPml_Profile':(mat['final'][101][0][0]).tolist(),
       'BEO_freq_profile':(mat['final'][102][0][0]).tolist(),
       'BEO_psd_profile':(mat['final'][103][0][0]).tolist(),
       'BEC_COPAP_PROFILE':(mat['final'][104][0][0]).tolist(),
       'BEC_COPml_Profile':(mat['final'][105][0][0]).tolist(),
       'BEC_freq_profile':(mat['final'][106][0][0]).tolist(),
       'BEC_psd_profile':(mat['final'][107][0][0]).tolist(),
       'UEO_COPAP_PROFILE':(mat['final'][108][0][0]).tolist(),
       'UEO_COPml_Profile':(mat['final'][109][0][0]).tolist(),
       'UEO_freq_profile':(mat['final'][110][0][0]).tolist(),
       'UEO_psd_profile':(mat['final'][111][0][0]).tolist(),
       'UEC_COPAP_PROFILE':(mat['final'][112][0][0]).tolist(),
       'UEC_COPml_Profile':(mat['final'][113][0][0]).tolist(),
       'UEC_freq_profile':(mat['final'][114][0][0]).tolist(),
       'UEC_psd_profile':(mat['final'][115][0][0]).tolist(),
       'BND_COPAP_Profile':(mat['final'][116][0][0]).tolist(),
       'BND_COPML_PROFILE':(mat['final'][117][0][0]).tolist(),
       'search_word_6':mat['final'][118][0][0],
       'search_word_7':(mat['final'][119][0][0]).tolist(),
       'search_word_8':mat['final'][120][0][0],
       'search_word_9':mat['final'][121][0][0],
       'search_word_10':mat['final'][122][0][0],
        }


    return record_doc

def handle_uploaded_file(file, filename):
    if not os.path.exists('upload/'):
        os.mkdir('upload/')

    with open('upload/' + filename,'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    #setup mongoDB connection
    client = MongoClient('mongodb://localhost:27017/')
    db = client.test_db
    col = db.test_collection

     #read .mat file contents into a dictionary
    rec = loadFile('upload/' + filename)

    # insert record into mongoDB
    result = col.insert_one(rec)
    return result.acknowledged

def upload(request):
    if request.method =='POST':
        result = handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))

    if result == True:
        messages.info(request, 'Insert succeeded')
    else:
        messages.info(request, 'Insert failed')
    return render(request,'upload_page.html')


@login_required()
def selector(request):
    return render(request,'bLab/selector.html', {})

@login_required()
def single_patient_search(request):
    return render(request,'bLab/single_patient_search.html', {})

@login_required()
def single_patient_BR(request):
    return render(request,'bLab/single_patient_BR.html', {})

@login_required()
def group_compar(request):
    return render(request,'bLab/group_compar.html', {})

@login_required()
def group_report(request):
    return render(request,'bLab/group_report.html', {})


def single_query(request, first_name, last_name, gender, age1, age2, search_word_1, search_word_2, search_word_3, search_word_4, search_word_5):

    print(request)
    print(first_name, last_name, gender, age1, age2, search_word_1, search_word_2, search_word_3, search_word_4, search_word_5)
    #build pymongo query


    # build pymongo query
    selectionCriteria = '{'
    if first_name != '':
        selectionCriteria += "'first_name': " + '"' + first_name + '"' + ', '
    if last_name != '':
        selectionCriteria += "'last_name': " + '"' + str(last_name) + '"' + ', '

    if selectionCriteria != '':
        selectionCriteria += '}'
    else:
        selectionCriteria += '}'

    selectionCriteriaDict = ast.literal_eval(selectionCriteria)
    print("selectionCriteria1:", selectionCriteriaDict)


    selectionCriteria2 ='{'
    #if first_name !='':
        #selectionCriteria2 += "'first_name': " +'"' + str(first_name) +'"' +','
    #if last_name !='':
        #selectionCriteria2 += "'last_name': " +'"' + str(last_name) +'"' +','
    if gender !='':
        selectionCriteria2 += "'gender': " +'"' + str(gender) +'"' +','
    if age1 !='' and age2 !='':
        selectionCriteria2 +='"age": {"$gte":' + age1 +', "$lte":' + age2 +'},'
    if age1 !='' and age2 =='':
        selectionCriteria2 +='"age": {"$gte":' + age1 +'},'
    if age1 =='' and age2 !='':
        selectionCriteria2 +='"age": {"$lte":' + age2 +'},'
    if search_word_1 !='':
        selectionCriteria2 += "'search_word_1': " +'"' + str(search_word_1) +'"' +','
    if search_word_2 !='':
        selectionCriteria2 += "'search_word_2': " +'"' + str(search_word_2) +'"' +','
    if search_word_3 !='':
        selectionCriteria2 += "'search_word_3': " +'"' + str(search_word_3) +'"' +','
    if search_word_4 !='':
        selectionCriteria2 += "'search_word_4': " +'"' + str(search_word_4) +'"' +','
    if search_word_5 !='':
        selectionCriteria2 += "'search_word_5': " +'"' + str(search_word_5) +'"'
    if selectionCriteria2 !='':
        selectionCriteria2 +='}'
    else:
        selectionCriteria2 +='}'


    selectionCriteriaDict2 = ast.literal_eval(selectionCriteria2)


    print("selectionCriteria2:", selectionCriteriaDict2)

    #run pymongo single query
    client = MongoClient('mongodb://localhost:27017/')
    db = client.test_db
    col = db.test_collection
    #{'first_name':'1st Name','last_name':'Last Name','gender':'gender','age': {'$gte': 12},'search_word_1':'search_word1','search_word_3':'search_word3'}

    finalQueryDict1 = col.find_one(selectionCriteriaDict, {"_id": 0, "header": 0, "Platform": 0, "Created on": 0})
    finalQueryDict2 = col.find(selectionCriteriaDict2, {"_id": 0, "header": 0, "Platform": 0, "Created on": 0})
    finalQueryList2 = list(finalQueryDict2)
    finalQueryDf2 = pd.DataFrame(finalQueryList2)

    print(finalQueryDf2)

    '''
    data = {'first_name':'first_name',
            'last_name':'last_name',
            'gender':'gender',
            'age':12,
            'address':'address',
            'city':'city',
            'state':'state',
            'BEOTime':6,
            'BECTime':16,
            'UEOTime':7,
            'UECTime':17,
            'phone':'phone'
            }
    '''
    ctrlNum = len(finalQueryDf2)
    maleCount = finalQueryDf2.gender.value_counts()['gender']
    femaleCount = finalQueryDf2.gender.value_counts()['gender']
    ageMin = finalQueryDf2.age.min()
    ageMax = finalQueryDf2.age.max()



    data3 = {'ctrlNum':ctrlNum,
             'femaleCount':femaleCount,
             'maleCount': maleCount,
             'ageMin':ageMin,
             'ageMax':ageMax
             }



    #print(type(data))

    #run pymongo group query


    table_data = [
        {'row_name':'Area',       'BEO_pt':0.0,'BEO_ctrls':0.0,'BEO_Pcnt':0.0,'BEC_pt':0.0,'BEC_ctrls':0.0,'BEC_Pcnt':0.0,'UEO_pt':0.0,'UEO_ctrls':0.0,'UEO_Pcnt':0.0,'UEC_pt':0.0,'UEC_ctrls':0.0,'UEC_Pcnt':0.0,'BND_pt':0.0,'BND_ctrls':0.0,'BND_Pcnt':0.0},
        {'row_name':'Range AP',   'BEO_pt':0.0,'BEO_ctrls':0.0,'BEO_Pcnt':0.0,'BEC_pt':0.0,'BEC_ctrls':0.0,'BEC_Pcnt':0.0,'UEO_pt':0.0,'UEO_ctrls':0.0,'UEO_Pcnt':0.0,'UEC_pt':0.0,'UEC_ctrls':0.0,'UEC_Pcnt':0.0,'BND_pt':0.0,'BND_ctrls':0.0,'BND_Pcnt':0.0},
        {'row_name':'Range ML',   'BEO_pt':0.0,'BEO_ctrls':0.0,'BEO_Pcnt':0.0,'BEC_pt':0.0,'BEC_ctrls':0.0,'BEC_Pcnt':0.0,'UEO_pt':0.0,'UEO_ctrls':0.0,'UEO_Pcnt':0.0,'UEC_pt':0.0,'UEC_ctrls':0.0,'UEC_Pcnt':0.0,'BND_pt':0.0,'BND_ctrls':0.0,'BND_Pcnt':0.0},
        {'row_name':'MV AP',      'BEO_pt':0.0,'BEO_ctrls':0.0,'BEO_Pcnt':0.0,'BEC_pt':0.0,'BEC_ctrls':0.0,'BEC_Pcnt':0.0,'UEO_pt':0.0,'UEO_ctrls':0.0,'UEO_Pcnt':0.0,'UEC_pt':0.0,'UEC_ctrls':0.0,'UEC_Pcnt':0.0,'BND_pt':0.0,'BND_ctrls':0.0,'BND_Pcnt':0.0},
        {'row_name':'MV ML',      'BEO_pt':0.0,'BEO_ctrls':0.0,'BEO_Pcnt':0.0,'BEC_pt':0.0,'BEC_ctrls':0.0,'BEC_Pcnt':0.0,'UEO_pt':0.0,'UEO_ctrls':0.0,'UEO_Pcnt':0.0,'UEC_pt':0.0,'UEC_ctrls':0.0,'UEC_Pcnt':0.0,'BND_pt':0.0,'BND_ctrls':0.0,'BND_Pcnt':0.0},
        {'row_name':'RMS AP',     'BEO_pt':0.0,'BEO_ctrls':0.0,'BEO_Pcnt':0.0,'BEC_pt':0.0,'BEC_ctrls':0.0,'BEC_Pcnt':0.0,'UEO_pt':0.0,'UEO_ctrls':0.0,'UEO_Pcnt':0.0,'UEC_pt':0.0,'UEC_ctrls':0.0,'UEC_Pcnt':0.0,'BND_pt':0.0,'BND_ctrls':0.0,'BND_Pcnt':0.0},
        {'row_name':'RMS ML',     'BEO_pt':0.0,'BEO_ctrls':0.0,'BEO_Pcnt':0.0,'BEC_pt':0.0,'BEC_ctrls':0.0,'BEC_Pcnt':0.0,'UEO_pt':0.0,'UEO_ctrls':0.0,'UEO_Pcnt':0.0,'UEC_pt':0.0,'UEC_ctrls':0.0,'UEC_Pcnt':0.0,'BND_pt':0.0,'BND_ctrls':0.0,'BND_Pcnt':0.0},
        {'row_name':'F80 AP (Hz)','BEO_pt':0.0,'BEO_ctrls':0.0,'BEO_Pcnt':0.0,'BEC_pt':0.0,'BEC_ctrls':0.0,'BEC_Pcnt':0.0,'UEO_pt':0.0,'UEO_ctrls':0.0,'UEO_Pcnt':0.0,'UEC_pt':0.0,'UEC_ctrls':0.0,'UEC_Pcnt':0.0,'BND_pt':0.0,'BND_ctrls':0.0,'BND_Pcnt':0.0},
        {'row_name':'F80 ML (Hz)','BEO_pt':0.0,'BEO_ctrls':0.0,'BEO_Pcnt':0.0,'BEC_pt':0.0,'BEC_ctrls':0.0,'BEC_Pcnt':0.0,'UEO_pt':0.0,'UEO_ctrls':0.0,'UEO_Pcnt':0.0,'UEC_pt':0.0,'UEC_ctrls':0.0,'UEC_Pcnt':0.0,'BND_pt':0.0,'BND_ctrls':0.0,'BND_Pcnt':0.0},
        {'row_name':'Sent AP',    'BEO_pt':0.0,'BEO_ctrls':0.0,'BEO_Pcnt':0.0,'BEC_pt':0.0,'BEC_ctrls':0.0,'BEC_Pcnt':0.0,'UEO_pt':0.0,'UEO_ctrls':0.0,'UEO_Pcnt':0.0,'UEC_pt':0.0,'UEC_ctrls':0.0,'UEC_Pcnt':0.0,'BND_pt':0.0,'BND_ctrls':0.0,'BND_Pcnt':0.0},
        {'row_name':'Sent ML',    'BEO_pt':0.0,'BEO_ctrls':0.0,'BEO_Pcnt':0.0,'BEC_pt':0.0,'BEC_ctrls':0.0,'BEC_Pcnt':0.0,'UEO_pt':0.0,'UEO_ctrls':0.0,'UEO_Pcnt':0.0,'UEC_pt':0.0,'UEC_ctrls':0.0,'UEC_Pcnt':0.0,'BND_pt':0.0,'BND_ctrls':0.0,'BND_Pcnt':0.0},
        {'row_name':'CrossEnt',   'BEO_pt':0.0,'BEO_ctrls':0.0,'BEO_Pcnt':0.0,'BEC_pt':0.0,'BEC_ctrls':0.0,'BEC_Pcnt':0.0,'UEO_pt':0.0,'UEO_ctrls':0.0,'UEO_Pcnt':0.0,'UEC_pt':0.0,'UEC_ctrls':0.0,'UEC_Pcnt':0.0,'BND_pt':0.0,'BND_ctrls':0.0,'BND_Pcnt':0.0},
    ]

    table = single_patient_response_table(table_data)
    table.show_header = True


    #chart 1
    x1 = [3, 5, 8,11,11,13,12,9,6,3]
    y1 = [8, 11,4,11, 7, 4, 2,3,3,8]
    plot1 = figure(title='BEO',
                  x_axis_label='X-Axis',
                  y_axis_label='Y-Axis',
                  plot_width=200,
                  plot_height=200)
    plot1.line(x1, y1, line_width=2)
    plot1.toolbar_location = None
    script1, div1 = components(plot1)

    #chart 2
    x2 = [3, 5,8,11,11,13,12,9,6,3]
    y2 = [8,11,4,11, 7, 4, 2,3,3,8]
    plot2 = figure(title='BEC',
                  x_axis_label='X-Axis',
                  y_axis_label='Y-Axis',
                  plot_width=200,
                  plot_height=200)
    plot2.line(x2, y2, line_width=2)
    plot2.toolbar_location = None
    script2, div2 = components(plot2)

    # chart 3
    x3 = [3, 5, 8,11,11,14,12,9,6,3]
    y3 = [8,11,12,11, 7, 6, 2,4,3,8]
    plot3 = figure(title='BND',
                   x_axis_label='X-Axis',
                   y_axis_label='Y-Axis',
                   plot_width=400,
                   plot_height=400)
    plot3.line(x3, y3, line_width=2)
    plot3.toolbar_location = None
    script3, div3 = components(plot3)

    # chart 4
    x4 = [3, 5, 8, 11, 11, 13, 12, 9, 6, 3]
    y4 = [8, 11,4, 11,  7,  4,  2, 3, 3, 8]
    plot4 = figure(title='UEO',
                   x_axis_label='X-Axis',
                   y_axis_label='Y-Axis',
                   plot_width=200,
                   plot_height=200)

    plot4.line(x4, y4, line_width=2)
    plot4.toolbar_location = None
    script4, div4 = components(plot4)

    # chart 5
    x5 = [3, 5, 8, 11, 11, 13, 12, 9, 6, 3]
    y5 = [8, 11, 4, 11, 7, 4, 2, 3, 3, 8]
    plot5 = figure(title='UEC',
                   x_axis_label='X-Axis',
                   y_axis_label='Y-Axis',
                   plot_width=200,
                   plot_height=200)
    plot5.line(x5, y5, line_width=2)
    plot5.toolbar_location = None
    script5, div5 = components(plot5)

    return render(request,'bLab/single_patient_BR.html',
                  {'sd':finalQueryDict1,
                   'sd2':data3,
                   'st':table,
                   'script1': script1, 'div1': div1,
                   'script2': script2, 'div2': div2,
                   'script3': script3, 'div3': div3,
                   'script4': script4, 'div4': div4,
                   'script5': script5, 'div5': div5
                   })

