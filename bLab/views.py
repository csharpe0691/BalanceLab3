from django.contrib.auth.decorators import login_required
from django.contrib import messages

import os
import scipy.io
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
#from jchart import Chart
#from jchart.config import Axes, DataSet
import ast
import django_tables2 as tables
import pandas as pd
import numpy as np

from bokeh.plotting import figure
from bokeh.embed import components


from pymongo import MongoClient

'''class LineChart1(Chart):
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


    '''
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



class groups_response_table(tables.Table):
    class Meta:
        attrs = {'width': '80%'}

    row_name = tables.Column(verbose_name='')
    BEO_G1 = tables.Column(verbose_name='BEO G1')
    BEO_G2 = tables.Column(verbose_name='BEO G2')
    BEO_G3 = tables.Column(verbose_name='BEO G3')
    BEC_G1 = tables.Column(verbose_name='BEC G1')
    BEC_G2 = tables.Column(verbose_name='BEC G2')
    BEC_G3 = tables.Column(verbose_name='BEC G3')
    UEO_G1 = tables.Column(verbose_name='UEO G1')
    UEO_G2 = tables.Column(verbose_name='UEO G2')
    UEO_G3 = tables.Column(verbose_name='UEO G3')
    UEC_G1 = tables.Column(verbose_name='UEC G1')
    UEC_G2 = tables.Column(verbose_name='UEC G2')
    UEC_G3 = tables.Column(verbose_name='UEC G3')
    BND_G1 = tables.Column(verbose_name='BND G1')
    BND_G2 = tables.Column(verbose_name='BND G2')
    BND_G3 = tables.Column(verbose_name='BND G3')


#class SingleResultsView(PandasSimpleView):
    #def get_data(self, request, *args, **kwargs):
        #return singleResultsdf

@login_required(login_url="login/")
def home(request):
    return render(request,"home.html")

@login_required()
def uploadPage(request):
    return render(request,'upload_page.html', {'what':'BalanceLab File Upload'})


def fixMat(mat):
    if mat['final'][9][0].size == 0:  # search_word 1
        mat['final'][9][0] = np.asarray(['-'])
    if mat['final'][10][0].size == 0:  # search_word 2
        mat['final'][10][0] = np.asarray(['-'])
    if mat['final'][11][0].size == 0:  # search_word 3
        mat['final'][11][0] = np.asarray(['-'])
    if mat['final'][12][0].size == 0:  # search_word 4
        mat['final'][12][0] = np.asarray(['-'])
    if mat['final'][13][0].size == 0:  # search_word 5
        mat['final'][13][0] = np.asarray(['-'])
    if mat['final'][118][0].size == 0:  # search_word 6
        mat['final'][118][0] = np.asarray(['-'])
    if mat['final'][119][0].size == 0:  # search_word 7
        mat['final'][119][0] = np.asarray(['-'])
    if mat['final'][120][0].size == 0:  # search_word 8
        mat['final'][120][0] = np.asarray(['-'])
    if mat['final'][121][0].size == 0:  # search_word 9
        mat['final'][121][0] = np.asarray(['-'])
    if mat['final'][122][0].size == 0:  # search_word 10
        mat['final'][122][0] = np.asarray(['-'])

    if mat['final'][41][0].size == 0:  # Cause of Trauma
        mat['final'][41][0] = np.asarray(['-'])

    if mat['final'][58][0][0].size == 0:  # BECAREA
        mat['final'][58][0][0] = np.asarray([0])
    if mat['final'][59][0][0].size == 0:  # BECSPEEDAP
        mat['final'][59][0][0] = np.asarray([0])
    if mat['final'][60][0][0].size == 0:  # BECSPEEDML
        mat['final'][60][0][0] = np.asarray([0])
    if mat['final'][61][0][0].size == 0:  # BECRANGEAP
        mat['final'][61][0][0] = np.asarray([0])
    if mat['final'][62][0][0].size == 0:  # BECRANGEML
        mat['final'][62][0][0] = np.asarray([0])
    if mat['final'][63][0][0].size == 0:  # BECRMSAP
        mat['final'][63][0][0] = np.asarray([0])
    if mat['final'][64][0][0].size == 0:  # BECRMSML
        mat['final'][64][0][0] = np.asarray([0])
    if mat['final'][65][0][0].size == 0:  # BECF50AP
        mat['final'][65][0][0] = np.asarray([0])
    if mat['final'][66][0][0].size == 0:  # BECF50ML
        mat['final'][66][0][0] = np.asarray([0])
    if mat['final'][67][0][0].size == 0:  # BECF80AP
        mat['final'][67][0][0] = np.asarray([0])
    if mat['final'][68][0][0].size == 0:  # BECSENTAP
        mat['final'][68][0][0] = np.asarray([0])
    if mat['final'][69][0][0].size == 0:  # BECSENTML
        mat['final'][69][0][0] = np.asarray([0])
    if mat['final'][70][0][0].size == 0:  # BECCROSSSENT
        mat['final'][70][0][0] = np.asarray([0])
    if mat['final'][71][0][0].size == 0:  # UEOAREA
        mat['final'][71][0][0] = np.asarray([0])
    if mat['final'][72][0][0].size == 0:  # UEOSPEEDAP
        mat['final'][72][0][0] = np.asarray([0])
    if mat['final'][73][0][0].size == 0:  # UEOSPEEDML
        mat['final'][73][0][0] = np.asarray([0])
    if mat['final'][74][0][0].size == 0:  # UEORANGEAP
        mat['final'][74][0][0] = np.asarray([0])
    if mat['final'][75][0][0].size == 0:  # UEORANGEML
        mat['final'][75][0][0] = np.asarray([0])
    if mat['final'][76][0][0].size == 0:  # UEORMSAP
        mat['final'][76][0][0] = np.asarray([0])
    if mat['final'][77][0][0].size == 0:  # UEORMSML
        mat['final'][77][0][0] = np.asarray([0])
    if mat['final'][78][0][0].size == 0:  # UEOF50AP
        mat['final'][78][0][0] = np.asarray([0])
    if mat['final'][79][0][0].size == 0:  # UEOF50ML
        mat['final'][79][0][0] = np.asarray([0])
    if mat['final'][80][0][0].size == 0:  # UEOF80AP
        mat['final'][80][0][0] = np.asarray([0])
    if mat['final'][81][0][0].size == 0:  # UEOSENTAP
        mat['final'][81][0][0] = np.asarray([0])
    if mat['final'][82][0][0].size == 0:  # UEOSENTML
        mat['final'][82][0][0] = np.asarray([0])
    if mat['final'][83][0][0].size == 0:  # UEOCROSSSENT
        mat['final'][83][0][0] = np.asarray([0])
    if mat['final'][84][0][0].size == 0:  # UECAREA
        mat['final'][84][0][0] = np.asarray([0])
    if mat['final'][85][0][0].size == 0:  # UECSPEEDAP
        mat['final'][85][0][0] = np.asarray([0])
    if mat['final'][86][0][0].size == 0:  # UECSPEEDML
        mat['final'][86][0][0] = np.asarray([0])
    if mat['final'][87][0][0].size == 0:  # UECRANGEAP
        mat['final'][87][0][0] = np.asarray([0])
    if mat['final'][88][0][0].size == 0:  # UECRANGEML
        mat['final'][88][0][0] = np.asarray([0])
    if mat['final'][89][0][0].size == 0:  # UECRMSAP
        mat['final'][89][0][0] = np.asarray([0])
    if mat['final'][90][0][0].size == 0:  # UECRMSML
        mat['final'][90][0][0] = np.asarray([0])
    if mat['final'][91][0][0].size == 0:  # UECF50AP
        mat['final'][91][0][0] = np.asarray([0])
    if mat['final'][92][0][0].size == 0:  # UECF50ML
        mat['final'][92][0][0] = np.asarray([0])
    if mat['final'][93][0][0].size == 0:  # UECF80AP
        mat['final'][93][0][0] = np.asarray([0])
    if mat['final'][94][0][0].size == 0:  # UECSENTAP
        mat['final'][94][0][0] = np.asarray([0])
    if mat['final'][95][0][0].size == 0:  # UECSENTML
        mat['final'][95][0][0] = np.asarray([0])
    if mat['final'][96][0][0].size == 0:  # UECCROSSSENT
        mat['final'][96][0][0] = np.asarray([0])

    if mat['final'][104][0].size == 0:  # BEC_COPAP_PROFILE
        mat['final'][104][0] = np.asarray([0])
    if mat['final'][105][0].size == 0:  # BEC_COPml_Profile
        mat['final'][105][0][0] = np.asarray([0])
    if mat['final'][106][0].size == 0:  # BEC_freq_profile
        mat['final'][106][0] = np.asarray([0])
    if mat['final'][107][0].size == 0:  # BEC_psd_profile
        mat['final'][107][0][0] = np.asarray([0])
    if mat['final'][108][0].size == 0:  # UEO_COPAP_PROFILE
        mat['final'][108][0] = np.asarray([0])
    if mat['final'][109][0].size == 0:  # UEO_COPml_Profile
        mat['final'][109][0][0] = np.asarray([0])
    if mat['final'][110][0].size == 0:  # UEO_freq_profile
        mat['final'][110][0] = np.asarray([0])
    if mat['final'][111][0].size == 0:  # UEO_psd_profile
        mat['final'][111][0][0] = np.asarray([0])
    if mat['final'][112][0].size == 0:  # UEC_COPAP_PROFILE
        mat['final'][112][0] = np.asarray([0])
    if mat['final'][113][0].size == 0:  # UEC_COPml_Profile
        mat['final'][113][0][0] = np.asarray([0])
    if mat['final'][114][0].size == 0:  # UEC_freq_profile
        mat['final'][114][0] = np.asarray([0])
    if mat['final'][115][0].size == 0:  # UEC_psd_profile
        mat['final'][115][0][0] = np.asarray([0])

    if mat['final'][124][0][0].size == 0:  # BECTime
        mat['final'][124][0][0] = np.asarray([0])
    if mat['final'][125][0][0].size == 0:  # UEOTime
        mat['final'][125][0][0] = np.asarray([0])
    if mat['final'][126][0][0].size == 0:  # UECTime
        mat['final'][126][0][0] = np.asarray([0])

    return mat


def loadFile(filename):
    rawMat = scipy.io.loadmat(filename)
    mat = fixMat(rawMat)
    # print("rawMat: ",rawMat)
    # print(type(mat))
    # print("keys:", mat.keys())
    # print("mat:", mat)

    record_doc = {
        'header': mat['__header__'],
        'version': mat['__version__'],
        'globals': mat['__globals__'],
        'patient_id': mat['final'][0][0][0],
        'first_name': mat['final'][1][0][0],
        'last_name': mat['final'][2][0][0],
        'address': mat['final'][3][0][0],
        'city': mat['final'][4][0][0],
        'state': mat['final'][5][0][0],
        'phone': mat['final'][6][0][0],
        'age': int(mat['final'][7][0][0]),
        'gender': mat['final'][8][0][0],
        'search_word_1': mat['final'][9][0][0],
        'search_word_2': mat['final'][10][0][0],
        'search_word_3': mat['final'][11][0][0],
        'search_word_4': mat['final'][12][0][0],
        'search_word_5': mat['final'][13][0][0],
        'feet_size': int(mat['final'][14][0]),
        'height': int(mat['final'][15][0][0][0]),
        'weight': int(mat['final'][16][0][0][0]),
        'NSI1': int(mat['final'][17][0][0][0]),
        'NSI2': int(mat['final'][18][0][0][0]),
        'NSI3': int(mat['final'][19][0][0][0]),
        'NSI4': int(mat['final'][20][0][0][0]),
        'NSI5': int(mat['final'][21][0][0][0]),
        'NSI6': int(mat['final'][22][0][0][0]),
        'NSI7': int(mat['final'][23][0][0][0]),
        'NSI8': int(mat['final'][24][0][0][0]),
        'NSI9': int(mat['final'][25][0][0][0]),
        'NSI10': int(mat['final'][26][0][0][0]),
        'NSI11': int(mat['final'][27][0][0][0]),
        'NSI12': int(mat['final'][28][0][0][0]),
        'NSI13': int(mat['final'][29][0][0][0]),
        'NSI14': int(mat['final'][30][0][0][0]),
        'NSI15': int(mat['final'][31][0][0][0]),
        'NSI16': int(mat['final'][32][0][0][0]),
        'NSI17': int(mat['final'][33][0][0][0]),
        'NSI18': int(mat['final'][34][0][0][0]),
        'NSI19': int(mat['final'][35][0][0][0]),
        'NSI20': int(mat['final'][36][0][0][0]),
        'NSI21': int(mat['final'][37][0][0][0]),
        'NSI22': int(mat['final'][38][0][0][0]),
        'NSITOTAL': int(mat['final'][39][0][0][0]),
        'BOSSize': int(mat['final'][40][0][0][0]),
        'cause_of_trauma': mat['final'][41][0][0],
        'number_of_previous_traumas': int(mat['final'][42][0][0]),
        'time_first_trauma': int(mat['final'][43][0][0][0]),
        'time_last_trauma': int(mat['final'][44][0][0][0]),
        'BEOAREA': mat['final'][45][0][0][0],
        'BEOSPEEDAP': mat['final'][46][0][0][0],
        'BEOSPEEDML': mat['final'][47][0][0][0],
        'BEORANGEAP': int(mat['final'][48][0][0][0]),
        'BEORANGEML': int(mat['final'][49][0][0][0]),
        'BEORMSAP': int(mat['final'][50][0][0][0]),
        'BEORMSML': int(mat['final'][51][0][0][0]),
        'BEOF50AP': int(mat['final'][52][0][0][0]),
        'BEOF50ML': int(mat['final'][53][0][0][0]),
        'BEOF80AP': int(mat['final'][54][0][0][0]),
        'BEOSENTAP': int(mat['final'][55][0][0][0]),
        'BEOSENTML': int(mat['final'][56][0][0][0]),
        'BEOCROSSSENT': int(mat['final'][57][0][0][0]),
        'BECAREA': mat['final'][58][0][0][0],
        'BECSPEEDAP': mat['final'][59][0][0][0],
        'BECSPEEDML': mat['final'][60][0][0][0],
        'BECRANGEAP': int(mat['final'][61][0][0][0]),
        'BECRANGEML': int(mat['final'][62][0][0][0]),
        'BECRMSAP': int(mat['final'][63][0][0][0]),
        'BECRMSML': int(mat['final'][64][0][0][0]),
        'BECF50AP': int(mat['final'][65][0][0][0]),
        'BECF50ML': int(mat['final'][66][0][0][0]),
        'BECF80AP': int(mat['final'][67][0][0][0]),
        'BECSENTAP': int(mat['final'][68][0][0][0]),
        'BECSENTML': int(mat['final'][69][0][0][0]),
        'BECCROSSSENT': int(mat['final'][70][0][0][0]),
        'UEOAREA': mat['final'][71][0][0][0],
        'UEOSPEEDAP': mat['final'][72][0][0][0],
        'UEOSPEEDML': mat['final'][73][0][0][0],
        'UEORANGEAP': int(mat['final'][74][0][0][0]),
        'UEORANGEML': int(mat['final'][75][0][0][0]),
        'UEORMSAP': int(mat['final'][76][0][0][0]),
        'UEORMSML': int(mat['final'][77][0][0][0]),
        'UEOF50AP': int(mat['final'][78][0][0][0]),
        'UEOF50ML': int(mat['final'][79][0][0][0]),
        'UEOF80AP': int(mat['final'][80][0][0][0]),
        'UEOSENTAP': int(mat['final'][81][0][0][0]),
        'UEOSENTML': int(mat['final'][82][0][0][0]),
        'UEOCROSSSENT': int(mat['final'][83][0][0][0]),
        'UECAREA': int(mat['final'][84][0][0][0]),
        'UECSPEEDAP': mat['final'][85][0][0][0],
        'UECSPEEDML': mat['final'][86][0][0][0],
        'UECRANGEAP': int(mat['final'][87][0][0][0]),
        'UECRANGEML': int(mat['final'][88][0][0][0]),
        'UECRMSAP': int(mat['final'][89][0][0][0]),
        'UECRMSML': int(mat['final'][90][0][0][0]),
        'UECF50AP': int(mat['final'][91][0][0][0]),
        'UECF50ML': int(mat['final'][92][0][0][0]),
        'UECF80AP': int(mat['final'][93][0][0][0]),
        'UECSENTAP': int(mat['final'][94][0][0][0]),
        'UECSENTML': int(mat['final'][95][0][0][0]),
        'UECCROSSSENT': int(mat['final'][96][0][0][0]),
        'BNDRANGEAP': int(mat['final'][97][0][0][0]),
        'BNDRANGEML': int(mat['final'][98][0][0][0]),
        'BNDAREA': int(mat['final'][99][0][0][0]),
        'BEO_COPAP_PROFILE': (mat['final'][100][0]).tolist(),
        'BEO_COPml_Profile': (mat['final'][101][0]).tolist(),
        'BEO_freq_profile': (mat['final'][102][0]).tolist(),
        'BEO_psd_profile': (mat['final'][103][0][0]).tolist(),
        'BEC_COPAP_PROFILE': (mat['final'][104][0]).tolist(),
        'BEC_COPml_Profile': (mat['final'][105][0]).tolist(),
        'BEC_freq_profile': (mat['final'][106][0]).tolist(),
        'BEC_psd_profile': (mat['final'][107][0][0]).tolist(),
        'UEO_COPAP_PROFILE': (mat['final'][108][0]).tolist(),
        'UEO_COPml_Profile': (mat['final'][109][0]).tolist(),
        'UEO_freq_profile': (mat['final'][110][0]).tolist(),
        'UEO_psd_profile': (mat['final'][111][0][0]).tolist(),
        'UEC_COPAP_PROFILE': (mat['final'][112][0]).tolist(),
        'UEC_COPml_Profile': (mat['final'][113][0]).tolist(),
        'UEC_freq_profile': (mat['final'][114][0]).tolist(),
        'UEC_psd_profile': (mat['final'][115][0][0]).tolist(),
        'BND_COPAP_Profile': (mat['final'][116][0]).tolist(),
        'BND_COPML_PROFILE': (mat['final'][117][0]).tolist(),
        'search_word_6': mat['final'][118][0][0],
        'search_word_7': (mat['final'][119][0][0]).tolist(),
        'search_word_8': mat['final'][120][0][0],
        'search_word_9': mat['final'][121][0][0],
        'search_word_10': mat['final'][122][0][0],
        'BEOTime': int(mat['final'][123][0][0]),
        'BECTime': int(mat['final'][124][0][0]),
        'UEOTime': int(mat['final'][125][0][0]),
        'UECTime': int(mat['final'][126][0][0]),
    }
    return record_doc

def handle_uploaded_file(file, filename):
    if not os.path.exists('upload/'):
        os.mkdir('upload/')

    with open('upload/' + filename,'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    #setup mongoDB connection
    client = MongoClient('mongodb://blqwuser:balanceLabWQ@gbbmongo.business.umt.edu')
    db = client.BalanceLab
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

def create_dummy_data():
    return {'first_name': '',
                'last_name': '',
                'gender': '',
                'age': 0,
                'address': '',
                'city': '',
                'state': '',
                'BEOTime': 0,
                'BECTime': 0,
                'UEOTime': 0,
                'UECTime': 0,
                'phone': ''
                }

def create_dummy_table_data():
    return [
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
    client = MongoClient('mongodb://blquser:balanceLabQ@gbbmongo.business.umt.edu')
    db = client.BalanceLab
    col = db.test_collection
    #{'first_name':'1st Name','last_name':'Last Name','gender':'gender','age': {'$gte': 12},'search_word_1':'search_word1','search_word_3':'search_word3'}





    doc = col.find_one(selectionCriteriaDict, {"_id": 0, "header": 0, "Platform": 0, "Created on": 0})
    if doc == None:
        print('no matches')
        queryStatus = 'no matched patient'
        # create a dummy empty doc here so the tags on the template still work
        data = {'first_name': '',
                'last_name': '',
                'gender': '',
                'age': 0,
                'address': '',
                'city': '',
                'state': '',
                'BEOTime': 0,
                'BECTime': 0,
                'UEOTime': 0,
                'UECTime': 0,
                'phone': ''
                }
        BECAREA = 0.0

    else:
        print('at least one match')
        queryStatus = 'matched patient'
        BECAREA = doc['BECAREA']

    print(type(doc))
    print(doc)

    #finalQueryDict2 = col.find(selectionCriteriaDict2, {"_id": 0, "header": 0, "Platform": 0, "Created on": 0})
    #finalQueryList2 = list(finalQueryDict2)
    #finalQueryDf2 = pd.DataFrame(finalQueryList2)
    #----------------------------------
    '''
    #finalQueryDict1 = col.find_one(selectionCriteriaDict, {"_id": 0, "header": 0, "Platform": 0, "Created on": 0})
    finalQueryDict1 = col.find(selectionCriteriaDict, {"_id": 0, "header": 0, "Platform": 0, "Created on": 0}).limit(1)
    finalQueryList1 = list(finalQueryDict1)
    finalQueryDf1 = pd.DataFrame(finalQueryList1)
    
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

    finalQueryDict1 = col.find(selectionCriteriaDict, {"_id": 0, "header": 0, "Platform": 0, "Created on": 0}).limit(2)

    if finalQueryDict1.count() == 0:
        print('no matches')
        queryStatus = 'no matched patient'
        messages.info(request, 'no matched patient')
        return render(request, 'bLab/single_patient_search.html')

    elif finalQueryDict1.count() > 1:
        print('multiple matches, please be more specific')
        queryStatus = str(finalQueryDict1.count()) + ' matched patients'

    else:
        #exactly one match
        print(type(finalQueryDict1))
        finalQueryDf1 = pd.DataFrame.from_records(finalQueryDict1).round(2)
        print(finalQueryDf1)
        query1SingleRow = finalQueryDf1.loc[0]
        print(query1SingleRow)



    if (finalQueryDict1.count() == 1):
        #query 1 worked so run query 2
        finalQueryDict2 = col.find(selectionCriteriaDict2, {"_id": 0, "header": 0, "Platform": 0, "Created on": 0})

        if (finalQueryDict2.count() == 0):
            messages.info(request, 'no matches for group search')
            return render(request, 'bLab/single_patient_search.html')
        else:
            #matched at least one record
            finalQueryList2 = list(finalQueryDict2)

            finalQueryDF2raw = pd.DataFrame(finalQueryList2)
            finalQueryDf2 = finalQueryDF2raw.round(2)




            #put values into table
            table_data = [
                {'row_name': 'Area', 'BEO_pt': query1SingleRow['BEOAREA'], 'BEO_ctrls': round(finalQueryDf2['BEOAREA'].mean(),2), 'BEO_Pcnt': round(query1SingleRow['BEOAREA']/finalQueryDf2['BEOAREA'].mean(),2), 'BEC_pt': query1SingleRow['BECAREA'], 'BEC_ctrls': round(finalQueryDf2['BECAREA'].mean(),2), 'BEC_Pcnt': round(query1SingleRow['BECAREA']/finalQueryDf2['BECAREA'].mean(),2), 'UEO_pt': query1SingleRow['UEOAREA'], 'UEO_ctrls': round(finalQueryDf2['UEOAREA'].mean(),2), 'UEO_Pcnt': round(query1SingleRow['UEOAREA']/finalQueryDf2['UEOAREA'].mean(),2), 'UEC_pt': query1SingleRow['UECAREA'], 'UEC_ctrls': round(finalQueryDf2['UECAREA'].mean(),2), 'UEC_Pcnt': round(query1SingleRow['UECAREA']/finalQueryDf2['UECAREA'].mean(),2), 'BND_pt': query1SingleRow['BNDAREA'], 'BND_ctrls': round(finalQueryDf2['BNDAREA'].mean(),2), 'BND_Pcnt': round(query1SingleRow['BNDAREA']/finalQueryDf2['BNDAREA'].mean(),2)},
                {'row_name': 'Range AP', 'BEO_pt': query1SingleRow['BEORANGEAP'], 'BEO_ctrls': round(finalQueryDf2['BEORANGEAP'].mean(),2), 'BEO_Pcnt': round(query1SingleRow['BEORANGEAP']/finalQueryDf2['BEORANGEAP'].mean(),2), 'BEC_pt': query1SingleRow['BECRANGEAP'], 'BEC_ctrls': round(finalQueryDf2['BECRANGEAP'].mean(),2), 'BEC_Pcnt': round(query1SingleRow['BECRANGEAP']/finalQueryDf2['BECRANGEAP'].mean(),2), 'UEO_pt': query1SingleRow['UEORANGEAP'], 'UEO_ctrls': round(finalQueryDf2['UEORANGEAP'].mean(),2), 'UEO_Pcnt': round(query1SingleRow['UEORANGEAP']/finalQueryDf2['UEORANGEAP'].mean(),2), 'UEC_pt': query1SingleRow['UECRANGEAP'], 'UEC_ctrls': round(finalQueryDf2['UECRANGEAP'].mean(),2), 'UEC_Pcnt': round(query1SingleRow['UECRANGEAP']/finalQueryDf2['UECRANGEAP'].mean(),2), 'BND_pt': query1SingleRow['BNDRANGEAP'], 'BND_ctrls': round(finalQueryDf2['BNDRANGEAP'].mean(),2), 'BND_Pcnt': round(query1SingleRow['BNDRANGEAP']/finalQueryDf2['BNDRANGEAP'].mean(),2)},
                {'row_name': 'Range ML', 'BEO_pt': query1SingleRow['BEORANGEML'], 'BEO_ctrls': round(finalQueryDf2['BEORANGEML'].mean(),2), 'BEO_Pcnt': round(query1SingleRow['BEORANGEML']/finalQueryDf2['BEORANGEML'].mean(),2), 'BEC_pt': query1SingleRow['BECRANGEML'], 'BEC_ctrls': round(finalQueryDf2['BEORANGEML'].mean(),2), 'BEC_Pcnt': round(query1SingleRow['BECRANGEML']/finalQueryDf2['BEORANGEML'].mean(),2), 'UEO_pt': query1SingleRow['UEORANGEML'], 'UEO_ctrls': round(finalQueryDf2['UEORANGEML'].mean(),2), 'UEO_Pcnt': round(query1SingleRow['UEORANGEML']/finalQueryDf2['UEORANGEML'].mean(),2), 'UEC_pt': query1SingleRow['UECRANGEML'], 'UEC_ctrls': round(finalQueryDf2['UECRANGEML'].mean(),2), 'UEC_Pcnt': round(query1SingleRow['UECRANGEML']/finalQueryDf2['UECRANGEML'].mean(),2), 'BND_pt': query1SingleRow['BNDRANGEML'], 'BND_ctrls': round(finalQueryDf2['BNDRANGEML'].mean(),2), 'BND_Pcnt': round(query1SingleRow['BNDRANGEML']/finalQueryDf2['BNDRANGEML'].mean(),2)},

                {'row_name': 'MV AP', 'BEO_pt': 0.0, 'BEO_ctrls': 0.0, 'BEO_Pcnt': 0.0, 'BEC_pt': 0.0, 'BEC_ctrls': 0.0, 'BEC_Pcnt': 0.0, 'UEO_pt': 0.0, 'UEO_ctrls': 0.0, 'UEO_Pcnt': 0.0, 'UEC_pt': 0.0, 'UEC_ctrls': 0.0, 'UEC_Pcnt': 0.0, 'BND_pt': '-', 'BND_ctrls': '-', 'BND_Pcnt': '-'},
                {'row_name': 'MV ML', 'BEO_pt': 0.0, 'BEO_ctrls': 0.0, 'BEO_Pcnt': 0.0, 'BEC_pt': 0.0, 'BEC_ctrls': 0.0, 'BEC_Pcnt': 0.0, 'UEO_pt': 0.0, 'UEO_ctrls': 0.0, 'UEO_Pcnt': 0.0, 'UEC_pt': 0.0, 'UEC_ctrls': 0.0, 'UEC_Pcnt': 0.0, 'BND_pt': '-', 'BND_ctrls': '-', 'BND_Pcnt': '-'},

                {'row_name': 'RMS AP', 'BEO_pt': query1SingleRow['BEORMSAP'], 'BEO_ctrls': round(finalQueryDf2['BEORMSAP'].mean(),2), 'BEO_Pcnt': round(query1SingleRow['BEORMSAP']/finalQueryDf2['BEORMSAP'].mean(),2), 'BEC_pt': query1SingleRow['BECRMSAP'], 'BEC_ctrls': round(finalQueryDf2['BECRMSAP'].mean(),2), 'BEC_Pcnt': round(query1SingleRow['BECRMSAP']/finalQueryDf2['BECRMSAP'].mean(),2), 'UEO_pt': query1SingleRow['UEORMSAP'], 'UEO_ctrls': round(finalQueryDf2['UEORMSAP'].mean(),2), 'UEO_Pcnt': round(query1SingleRow['UEORMSAP']/finalQueryDf2['UEORMSAP'].mean(),2), 'UEC_pt': query1SingleRow['UECRMSAP'], 'UEC_ctrls': round(finalQueryDf2['UECRMSAP'].mean(),2), 'UEC_Pcnt': round(query1SingleRow['UECRMSAP']/finalQueryDf2['UECRMSAP'].mean(),2), 'BND_pt': '-', 'BND_ctrls': '-', 'BND_Pcnt': '-'},
                {'row_name': 'RMS ML', 'BEO_pt': query1SingleRow['BEORMSML'], 'BEO_ctrls': round(finalQueryDf2['BEORMSML'].mean(),2), 'BEO_Pcnt': round(query1SingleRow['BEORMSML']/finalQueryDf2['BEORMSML'].mean(),2), 'BEC_pt': query1SingleRow['BECRMSML'], 'BEC_ctrls': round(finalQueryDf2['BECRMSML'].mean(),2), 'BEC_Pcnt': round(query1SingleRow['BECRMSML']/finalQueryDf2['BECRMSML'].mean(),2), 'UEO_pt': query1SingleRow['UEORMSML'], 'UEO_ctrls': round(finalQueryDf2['UEORMSML'].mean(),2), 'UEO_Pcnt': round(query1SingleRow['UEORMSML']/finalQueryDf2['UEORMSML'].mean(),2), 'UEC_pt': query1SingleRow['UECRMSML'], 'UEC_ctrls': round(finalQueryDf2['UECRMSML'].mean(),2), 'UEC_Pcnt': round(query1SingleRow['UECRMSML']/finalQueryDf2['UECRMSML'].mean(),2), 'BND_pt': '-', 'BND_ctrls': '-', 'BND_Pcnt': '-'},
                {'row_name': 'F80 AP (Hz)', 'BEO_pt': query1SingleRow['BEOF80AP'], 'BEO_ctrls': round(finalQueryDf2['BEOF80AP'].mean(),2), 'BEO_Pcnt': round(query1SingleRow['BEOF80AP']/finalQueryDf2['BEOF80AP'].mean(),2), 'BEC_pt': query1SingleRow['BECF80AP'], 'BEC_ctrls': round(finalQueryDf2['BECF80AP'].mean(),2), 'BEC_Pcnt': round(query1SingleRow['BECF80AP']/finalQueryDf2['BECF80AP'].mean(),2), 'UEO_pt': query1SingleRow['UEOF80AP'], 'UEO_ctrls': round(finalQueryDf2['UEOF80AP'].mean(),2), 'UEO_Pcnt': round(query1SingleRow['UEOF80AP']/finalQueryDf2['UEOF80AP'].mean(),2), 'UEC_pt': query1SingleRow['UECF80AP'], 'UEC_ctrls': round(finalQueryDf2['UECF80AP'].mean(),2), 'UEC_Pcnt': round(query1SingleRow['UECF80AP']/finalQueryDf2['UECF80AP'].mean(),2), 'BND_pt': '-', 'BND_ctrls': '-', 'BND_Pcnt': '-'},

                {'row_name': 'F80 ML (Hz)', 'BEO_pt': 0.0, 'BEO_ctrls': 0.0, 'BEO_Pcnt': 0.0, 'BEC_pt': 0.0, 'BEC_ctrls': 0.0, 'BEC_Pcnt': 0.0, 'UEO_pt': 0.0, 'UEO_ctrls': 0.0, 'UEO_Pcnt': 0.0, 'UEC_pt': 0.0, 'UEC_ctrls': 0.0, 'UEC_Pcnt': 0.0, 'BND_pt': '-', 'BND_ctrls': '-', 'BND_Pcnt': '-'},

                {'row_name': 'Sent AP', 'BEO_pt': query1SingleRow['BEOSENTAP'], 'BEO_ctrls': round(finalQueryDf2['BEOSENTAP'].mean(),2), 'BEO_Pcnt': round(query1SingleRow['BEOSENTAP']/finalQueryDf2['BEOSENTAP'].mean(),2), 'BEC_pt': query1SingleRow['BECSENTAP'], 'BEC_ctrls': round(finalQueryDf2['BECSENTAP'].mean(),2), 'BEC_Pcnt': round(query1SingleRow['BECSENTAP']/finalQueryDf2['BECSENTAP'].mean(),2), 'UEO_pt': query1SingleRow['UEOSENTAP'], 'UEO_ctrls': round(finalQueryDf2['UEOSENTAP'].mean(),2), 'UEO_Pcnt': round(query1SingleRow['UEOSENTAP']/finalQueryDf2['UEOSENTAP'].mean(),2), 'UEC_pt': query1SingleRow['UECSENTAP'], 'UEC_ctrls': round(finalQueryDf2['UECSENTAP'].mean(),2), 'UEC_Pcnt': round(query1SingleRow['UECSENTAP']/finalQueryDf2['UECSENTAP'].mean(),2), 'BND_pt': '-', 'BND_ctrls': '-', 'BND_Pcnt': '-'},
                {'row_name': 'Sent ML', 'BEO_pt': query1SingleRow['BEOSENTML'], 'BEO_ctrls': round(finalQueryDf2['BEOSENTML'].mean(),2), 'BEO_Pcnt': round(query1SingleRow['BEOSENTML']/finalQueryDf2['BEOSENTML'].mean(),2), 'BEC_pt': query1SingleRow['BECSENTML'], 'BEC_ctrls': round(finalQueryDf2['BECSENTML'].mean(),2), 'BEC_Pcnt': round(query1SingleRow['BECSENTML']/finalQueryDf2['BECSENTML'].mean(),2), 'UEO_pt': query1SingleRow['UEOSENTML'], 'UEO_ctrls': round(finalQueryDf2['UEOSENTML'].mean(),2), 'UEO_Pcnt': round(query1SingleRow['UEOSENTML']/finalQueryDf2['UEOSENTML'].mean(),2), 'UEC_pt': query1SingleRow['UECSENTML'], 'UEC_ctrls': round(finalQueryDf2['UECSENTML'].mean(),2), 'UEC_Pcnt': round(query1SingleRow['UECSENTML']/finalQueryDf2['UECSENTML'].mean(),2), 'BND_pt': '-', 'BND_ctrls': '-', 'BND_Pcnt': '-'},
                {'row_name': 'CrossSent', 'BEO_pt': query1SingleRow['BEOCROSSSENT'], 'BEO_ctrls': round(finalQueryDf2['BEOCROSSSENT'].mean(),2), 'BEO_Pcnt': round(query1SingleRow['BEOCROSSSENT']/finalQueryDf2['BEOCROSSSENT'].mean(),2), 'BEC_pt': query1SingleRow['BECCROSSSENT'], 'BEC_ctrls': round(finalQueryDf2['BECCROSSSENT'].mean(),2), 'BEC_Pcnt': round(query1SingleRow['BECCROSSSENT']/finalQueryDf2['BECCROSSSENT'].mean(),2), 'UEO_pt': query1SingleRow['UEOCROSSSENT'], 'UEO_ctrls': round(finalQueryDf2['UEOCROSSSENT'].mean(),2), 'UEO_Pcnt': round(query1SingleRow['UEOCROSSSENT']/finalQueryDf2['UEOCROSSSENT'].mean(),2), 'UEC_pt': query1SingleRow['UECCROSSSENT'], 'UEC_ctrls': round(finalQueryDf2['UECCROSSSENT'].mean(),2), 'UEC_Pcnt': round(query1SingleRow['UECCROSSSENT']/finalQueryDf2['UECCROSSSENT'].mean(),2), 'BND_pt': '-', 'BND_ctrls': '-', 'BND_Pcnt': '-'},
            ]





    ctrlNum = len(finalQueryDf2)
    maleCount = finalQueryDf2.gender.value_counts()['Male']
    femaleCount = finalQueryDf2.gender.value_counts()['Female']
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

    #----------------------------
    '''
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
    '''
    # the following code runs regardless of query status
    table = single_patient_response_table(table_data)
    table.show_header = True


    print(query1SingleRow['BEO_COPml_Profile'])
    #chart 1
    x1 = query1SingleRow['BEO_COPml_Profile']
    y1 = query1SingleRow['BEO_COPAP_PROFILE']
    plot1 = figure(title='BEO',
                  x_axis_label='X-Axis',
                  y_axis_label='Y-Axis',
                  plot_width=200,
                  plot_height=200,
                   x_range=(-6, 6),
                   y_range=(-6, 6))
    #plot1.line(x1, y1, line_width=2, line_color="LightSkyBlue")
    plot1.multi_line([query1SingleRow['BEO_COPml_Profile']],
                     [query1SingleRow['BEO_COPAP_PROFILE']],
                 color=["LightSkyBlue"], line_width=2)
    plot1.toolbar_location = None
    script1, div1 = components(plot1)

    #chart 2
    x2 = query1SingleRow['BEC_COPml_Profile']
    y2 = query1SingleRow['BEC_COPAP_PROFILE']
    plot2 = figure(title='BEC',
                  x_axis_label='X-Axis',
                  y_axis_label='Y-Axis',
                  plot_width=200,
                  plot_height=200,
                   x_range=(-6, 6),
                   y_range=(-6, 6))
    #plot2.line(x2, y2, line_width=2, line_color="MidnightBlue")
    plot2.multi_line([query1SingleRow['BEC_COPml_Profile']],
                     [query1SingleRow['BEC_COPAP_PROFILE']],
                 color=["MidnightBlue"], line_width=2)
    plot2.toolbar_location = None
    script2, div2 = components(plot2)

    # chart 3
    x3 = query1SingleRow['BND_COPML_PROFILE']
    y3 = query1SingleRow['BND_COPAP_Profile']
    plot3 = figure(title='BND',
                   x_axis_label='X-Axis',
                   y_axis_label='Y-Axis',
                   plot_width=200,
                   plot_height=200,
                   x_range=(-6, 6),
                   y_range=(-6, 6))
    #plot3.line(x3, y3, line_width=2, line_color="black")
    plot3.multi_line([query1SingleRow['BND_COPML_PROFILE']],
                     [query1SingleRow['BND_COPAP_Profile']],
                 color=["Black"], line_width=2)
    plot3.toolbar_location = None
    script3, div3 = components(plot3)

    # chart 4
    x4 = query1SingleRow['UEO_COPml_Profile']
    y4 = query1SingleRow['UEO_COPAP_PROFILE']
    plot4 = figure(title='UEO',
                   x_axis_label='X-Axis',
                   y_axis_label='Y-Axis',
                   plot_width=200,
                   plot_height=200,
                   x_range=(-6, 6),
                   y_range=(-6, 6))
    #plot4.line(x4, y4, line_width=2, line_color="LightSalmon")
    plot4.multi_line([query1SingleRow['UEO_COPml_Profile']],
                     [query1SingleRow['UEO_COPAP_PROFILE']],
                 color=["DarkOrange"], line_width=2)
    plot4.toolbar_location = None
    script4, div4 = components(plot4)

    # chart 5
    x5 = query1SingleRow['UEC_COPml_Profile']
    y5 = query1SingleRow['UEC_COPAP_PROFILE']
    plot5 = figure(title='UEC',
                   x_axis_label='X-Axis',
                   y_axis_label='Y-Axis',
                   plot_width=200,
                   plot_height=200,
                   x_range=(-6, 6),
                   y_range=(-6, 6))
    #plot5.line(x5, y5, line_width=2, color="DarkOrange")
    plot5.multi_line([query1SingleRow['UEC_COPml_Profile']],
                     [query1SingleRow['UEC_COPAP_PROFILE']],
                 color=["DarkOrange"], line_width=2)
    plot5.toolbar_location = None
    script5, div5 = components(plot5)


    dummyBigData = [[1, 3, 2], [3, 4, 6, 6]], [[2, 1, 4], [4, 7, 8, 5]]
    # chart 6
    plot6 = figure(title='COP Areas',
                   x_axis_label='X-Axis',
                   y_axis_label='Y-Axis',
                   plot_width=400,
                   plot_height=400,
                   x_range=(-6, 6),
                   y_range=(-6, 6))
    #plot6.multi_line([[1, 3, 2], [3, 4, 6, 6]], [[2, 1, 4], [4, 7, 8, 5]],
    plot6.multi_line([query1SingleRow['BEO_COPml_Profile'], query1SingleRow['BEC_COPml_Profile'],
                      query1SingleRow['UEO_COPml_Profile'], query1SingleRow['UEC_COPml_Profile']],
                     [query1SingleRow['BEO_COPAP_PROFILE'], query1SingleRow['BEC_COPAP_PROFILE'],
                      query1SingleRow['UEO_COPAP_PROFILE'], query1SingleRow['UEC_COPAP_PROFILE']],
                 color=["LightSkyBlue", "MidnightBlue", "LightSalmon", "DarkOrange"], line_width=2)
    plot6.toolbar_location = None
    script6, div6 = components(plot6)

    return render(request,'bLab/single_patient_BR.html',
                  {'sd':doc,
                   'sd2':data3,
                   'st':table,
                   'script1': script1, 'div1': div1,
                   'script2': script2, 'div2': div2,
                   'script3': script3, 'div3': div3,
                   'script4': script4, 'div4': div4,
                   'script5': script5, 'div5': div5,
                   'script6': script6, 'div6': div6,
                   'queryStatus': queryStatus
                   })



def create_dummy_table_dataG():
    return [
        {'row_name':'Area',       'BEO_G1':0.0,'BEO_G2':0.0,'BEO_G3':0.0,'BEC_G1':0.0,'BEC_G2':0.0,'BEC_G3':0.0,'UEO_G1':0.0,'UEO_G2':0.0,'UEO_G3':0.0,'UEC_G1':0.0,'UEC_G2':0.0,'UEC_G3':0.0,'BND_G1':0.0,'BND_G2':0.0,'BND_G3':0.0},
        {'row_name':'Range AP',   'BEO_G1':0.0,'BEO_G2':0.0,'BEO_G3':0.0,'BEC_G1':0.0,'BEC_G2':0.0,'BEC_G3':0.0,'UEO_G1':0.0,'UEO_G2':0.0,'UEO_G3':0.0,'UEC_G1':0.0,'UEC_G2':0.0,'UEC_G3':0.0,'BND_G1':0.0,'BND_G2':0.0,'BND_G3':0.0},
        {'row_name':'Range ML',   'BEO_G1':0.0,'BEO_G2':0.0,'BEO_G3':0.0,'BEC_G1':0.0,'BEC_G2':0.0,'BEC_G3':0.0,'UEO_G1':0.0,'UEO_G2':0.0,'UEO_G3':0.0,'UEC_G1':0.0,'UEC_G2':0.0,'UEC_G3':0.0,'BND_G1':0.0,'BND_G2':0.0,'BND_G3':0.0},
        {'row_name':'MV AP',      'BEO_G1':0.0,'BEO_G2':0.0,'BEO_G3':0.0,'BEC_G1':0.0,'BEC_G2':0.0,'BEC_G3':0.0,'UEO_G1':0.0,'UEO_G2':0.0,'UEO_G3':0.0,'UEC_G1':0.0,'UEC_G2':0.0,'UEC_G3':0.0,'BND_G1':0.0,'BND_G2':0.0,'BND_G3':0.0},
        {'row_name':'MV ML',      'BEO_G1':0.0,'BEO_G2':0.0,'BEO_G3':0.0,'BEC_G1':0.0,'BEC_G2':0.0,'BEC_G3':0.0,'UEO_G1':0.0,'UEO_G2':0.0,'UEO_G3':0.0,'UEC_G1':0.0,'UEC_G2':0.0,'UEC_G3':0.0,'BND_G1':0.0,'BND_G2':0.0,'BND_G3':0.0},
        {'row_name':'RMS AP',     'BEO_G1':0.0,'BEO_G2':0.0,'BEO_G3':0.0,'BEC_G1':0.0,'BEC_G2':0.0,'BEC_G3':0.0,'UEO_G1':0.0,'UEO_G2':0.0,'UEO_G3':0.0,'UEC_G1':0.0,'UEC_G2':0.0,'UEC_G3':0.0,'BND_G1':0.0,'BND_G2':0.0,'BND_G3':0.0},
        {'row_name':'RMS ML',     'BEO_G1':0.0,'BEO_G2':0.0,'BEO_G3':0.0,'BEC_G1':0.0,'BEC_G2':0.0,'BEC_G3':0.0,'UEO_G1':0.0,'UEO_G2':0.0,'UEO_G3':0.0,'UEC_G1':0.0,'UEC_G2':0.0,'UEC_G3':0.0,'BND_G1':0.0,'BND_G2':0.0,'BND_G3':0.0},
        {'row_name':'F80 AP (Hz)','BEO_G1':0.0,'BEO_G2':0.0,'BEO_G3':0.0,'BEC_G1':0.0,'BEC_G2':0.0,'BEC_G3':0.0,'UEO_G1':0.0,'UEO_G2':0.0,'UEO_G3':0.0,'UEC_G1':0.0,'UEC_G2':0.0,'UEC_G3':0.0,'BND_G1':0.0,'BND_G2':0.0,'BND_G3':0.0},
        {'row_name':'F80 ML (Hz)','BEO_G1':0.0,'BEO_G2':0.0,'BEO_G3':0.0,'BEC_G1':0.0,'BEC_G2':0.0,'BEC_G3':0.0,'UEO_G1':0.0,'UEO_G2':0.0,'UEO_G3':0.0,'UEC_G1':0.0,'UEC_G2':0.0,'UEC_G3':0.0,'BND_G1':0.0,'BND_G2':0.0,'BND_G3':0.0},
        {'row_name':'Sent AP',    'BEO_G1':0.0,'BEO_G2':0.0,'BEO_G3':0.0,'BEC_G1':0.0,'BEC_G2':0.0,'BEC_G3':0.0,'UEO_G1':0.0,'UEO_G2':0.0,'UEO_G3':0.0,'UEC_G1':0.0,'UEC_G2':0.0,'UEC_G3':0.0,'BND_G1':0.0,'BND_G2':0.0,'BND_G3':0.0},
        {'row_name':'Sent ML',    'BEO_G1':0.0,'BEO_G2':0.0,'BEO_G3':0.0,'BEC_G1':0.0,'BEC_G2':0.0,'BEC_G3':0.0,'UEO_G1':0.0,'UEO_G2':0.0,'UEO_G3':0.0,'UEC_G1':0.0,'UEC_G2':0.0,'UEC_G3':0.0,'BND_G1':0.0,'BND_G2':0.0,'BND_G3':0.0},
        {'row_name':'CrossEnt',   'BEO_G1':0.0,'BEO_G2':0.0,'BEO_G3':0.0,'BEC_G1':0.0,'BEC_G2':0.0,'BEC_G3':0.0,'UEO_G1':0.0,'UEO_G2':0.0,'UEO_G3':0.0,'UEC_G1':0.0,'UEC_G2':0.0,'UEC_G3':0.0,'BND_G1':0.0,'BND_G2':0.0,'BND_G3':0.0},
    ]



def groups_query(request, genderG1, age1G1, age2G1, key1G1, key2G1, key3G1, key4G1, key5G1, genderG2, age1G2, age2G2, key1G2, key2G2, key3G2, key4G2, key5G2, genderG3, age1G3, age2G3, key1G3, key2G3, key3G3, key4G3, key5G3):

    print(request)
    print(genderG1, age1G1, age2G1, key1G1, key2G1, key3G1, key4G1, key5G1, genderG2, age1G2, age2G2, key1G2, key2G2, key3G2, key4G2, key5G2, genderG3, age1G3, age2G3, key1G3, key2G3, key3G3, key4G3, key5G3)


    selectionCriteriaG1 ='{'
    #if first_name !='':
        #selectionCriteria2 += "'first_name': " +'"' + str(first_name) +'"' +','
    #if last_name !='':
        #selectionCriteria2 += "'last_name': " +'"' + str(last_name) +'"' +','
    if genderG1 !='':
        selectionCriteriaG1 += "'gender': " +'"' + str(genderG1) +'"' +','
    if age1G1 !='' and age2G1 !='':
        selectionCriteriaG1 +='"age": {"$gte":' + age1G1 +', "$lte":' + age2G1 +'},'
    if age1G1 !='' and age2G1 =='':
        selectionCriteriaG1 +='"age": {"$gte":' + age1G1 +'},'
    if age1G1 =='' and age2G1 !='':
        selectionCriteriaG1 +='"age": {"$lte":' + age2G1 +'},'
    if key1G1 !='':
        selectionCriteriaG1 += "'search_word_1': " +'"' + str(key1G1) +'"' +','
    if key2G1 !='':
        selectionCriteriaG1 += "'search_word_2': " +'"' + str(key2G1) +'"' +','
    if key3G1 !='':
        selectionCriteriaG1 += "'search_word_3': " +'"' + str(key3G1) +'"' +','
    if key4G1 !='':
        selectionCriteriaG1 += "'search_word_4': " +'"' + str(key4G1) +'"' +','
    if key5G1 !='':
        selectionCriteriaG1 += "'search_word_5': " +'"' + str(key5G1) +'"'
    if selectionCriteriaG1 !='':
        selectionCriteriaG1 +='}'
    else:
        selectionCriteriaG1 +='}'

    selectionCriteriaDictG1 = ast.literal_eval(selectionCriteriaG1)
    print("selectionCriteriaG1:", selectionCriteriaDictG1)


    selectionCriteriaG2 ='{'
    #if first_name !='':
        #selectionCriteria2 += "'first_name': " +'"' + str(first_name) +'"' +','
    #if last_name !='':
        #selectionCriteria2 += "'last_name': " +'"' + str(last_name) +'"' +','
    if genderG2 !='':
        selectionCriteriaG2 += "'gender': " +'"' + str(genderG2) +'"' +','
    if age1G2 !='' and age2G2 !='':
        selectionCriteriaG2 +='"age": {"$gte":' + age1G2 +', "$lte":' + age2G2 +'},'
    if age1G2 !='' and age2G2 =='':
        selectionCriteriaG2 +='"age": {"$gte":' + age1G2 +'},'
    if age1G2 =='' and age2G2 !='':
        selectionCriteriaG2 +='"age": {"$lte":' + age2G2 +'},'
    if key1G2 !='':
        selectionCriteriaG2 += "'search_word_1': " +'"' + str(key1G2) +'"' +','
    if key2G2 !='':
        selectionCriteriaG2 += "'search_word_2': " +'"' + str(key2G2) +'"' +','
    if key3G2 !='':
        selectionCriteriaG2 += "'search_word_3': " +'"' + str(key3G2) +'"' +','
    if key4G2 !='':
        selectionCriteriaG2 += "'search_word_4': " +'"' + str(key4G2) +'"' +','
    if key5G2 !='':
        selectionCriteriaG2 += "'search_word_5': " +'"' + str(key5G2) +'"'
    if selectionCriteriaG2 !='':
        selectionCriteriaG2 +='}'
    else:
        selectionCriteriaG2 +='}'

    selectionCriteriaDictG2 = ast.literal_eval(selectionCriteriaG2)
    print("selectionCriteriaG2:", selectionCriteriaDictG2)


    selectionCriteriaG3 ='{'
    #if first_name !='':
        #selectionCriteria2 += "'first_name': " +'"' + str(first_name) +'"' +','
    #if last_name !='':
        #selectionCriteria2 += "'last_name': " +'"' + str(last_name) +'"' +','
    if genderG3 !='':
        selectionCriteriaG3 += "'gender': " +'"' + str(genderG3) +'"' +','
    if age1G3 !='' and age2G3 !='':
        selectionCriteriaG3 +='"age": {"$gte":' + age1G3 +', "$lte":' + age2G3 +'},'
    if age1G3 !='' and age2G3 =='':
        selectionCriteriaG3 +='"age": {"$gte":' + age1G3 +'},'
    if age1G3 =='' and age2G3 !='':
        selectionCriteriaG3 +='"age": {"$lte":' + age2G3 +'},'
    if key1G3 !='':
        selectionCriteriaG3 += "'search_word_1': " +'"' + str(key1G3) +'"' +','
    if key2G3 !='':
        selectionCriteriaG3 += "'search_word_2': " +'"' + str(key2G3) +'"' +','
    if key3G3 !='':
        selectionCriteriaG3 += "'search_word_3': " +'"' + str(key3G3) +'"' +','
    if key4G3 !='':
        selectionCriteriaG3 += "'search_word_4': " +'"' + str(key4G3) +'"' +','
    if key5G3 !='':
        selectionCriteriaG3 += "'search_word_5': " +'"' + str(key5G3) +'"'
    if selectionCriteriaG3 !='':
        selectionCriteriaG3 +='}'
    else:
        selectionCriteriaG3 +='}'

    selectionCriteriaDictG3 = ast.literal_eval(selectionCriteriaG3)
    print("selectionCriteriaG3:", selectionCriteriaDictG3)

    #run pymongo single query
    client = MongoClient('mongodb://blquser:balanceLabQ@gbbmongo.business.umt.edu')
    db = client.BalanceLab
    col = db.test_collection

    finalQueryDictG1 = col.find(selectionCriteriaDictG1, {"_id": 0, "header": 0, "Platform": 0, "Created on": 0})

    if (finalQueryDictG1.count() == 0):
        table_data = create_dummy_table_dataG()
    else:
        # matched at least one record
        finalQueryListG1 = list(finalQueryDictG1)
        finalQueryDfG1 = pd.DataFrame(finalQueryListG1)

    finalQueryDictG2 = col.find(selectionCriteriaDictG2, {"_id": 0, "header": 0, "Platform": 0, "Created on": 0})
    finalQueryListG2 = list(finalQueryDictG2)
    finalQueryDfG2 = pd.DataFrame(finalQueryListG2)


    finalQueryDictG3 = col.find(selectionCriteriaDictG3, {"_id": 0, "header": 0, "Platform": 0, "Created on": 0})
    finalQueryListG3 = list(finalQueryDictG3)
    finalQueryDfG3 = pd.DataFrame(finalQueryListG3)

    table_dataG = [
        {'row_name': 'Area',        'BEO_G1': finalQueryDfG1['BEOAREA'].mean(), 'BEO_G2': finalQueryDfG2['BEOAREA'].mean(), 'BEO_G3': finalQueryDfG3['BEOAREA'].mean(), 'BEC_G1': finalQueryDfG1['BECAREA'].mean(), 'BEC_G2': finalQueryDfG2['BECAREA'].mean(), 'BEC_G3': finalQueryDfG3['BECAREA'].mean(), 'UEO_G1': finalQueryDfG1['UEOAREA'].mean(), 'UEO_G2': finalQueryDfG2['UEOAREA'].mean(),                                         'UEO_G3': finalQueryDfG3['UEOAREA'].mean(), 'UEC_G1': finalQueryDfG1['UECAREA'].mean(),                     'UEC_G2': finalQueryDfG2['UECAREA'].mean(), 'UEC_G3': finalQueryDfG3['UECAREA'].mean(), 'BND_G1': finalQueryDfG1['BNDAREA'].mean(), 'BND_G2': finalQueryDfG2['BNDAREA'].mean(), 'BND_G3': finalQueryDfG3['BNDAREA'].mean()},
        {'row_name': 'Range AP',    'BEO_G1': finalQueryDfG1['BEORANGEAP'].mean(), 'BEO_G2': finalQueryDfG2['BEORANGEAP'].mean(), 'BEO_G3': finalQueryDfG3['BEORANGEAP'].mean(), 'BEC_G1': finalQueryDfG1['BECRANGEAP'].mean(), 'BEC_G2': finalQueryDfG2['BECRANGEAP'].mean(), 'BEC_G3': finalQueryDfG3['BECRANGEAP'].mean(), 'UEO_G1': finalQueryDfG1['UEORANGEAP'].mean(), 'UEO_G2': finalQueryDfG2['UEORANGEAP'].mean(),                 'UEO_G3': finalQueryDfG3['UEORANGEAP'].mean(), 'UEC_G1': finalQueryDfG1['UECRANGEAP'].mean(),               'UEC_G2': finalQueryDfG2['UECRANGEAP'].mean(), 'UEC_G3': finalQueryDfG3['UECRANGEAP'].mean(), 'BND_G1': finalQueryDfG1['BNDRANGEAP'].mean(), 'BND_G2': finalQueryDfG2['BNDRANGEAP'].mean(), 'BND_G3': finalQueryDfG3['BNDRANGEAP'].mean()},
        {'row_name': 'Range ML',    'BEO_G1': finalQueryDfG1['BEORANGEML'].mean(), 'BEO_G2': finalQueryDfG2['BEORANGEML'].mean(), 'BEO_G3': finalQueryDfG3['BEORANGEML'].mean(), 'BEC_G1': finalQueryDfG1['BECRANGEML'].mean(), 'BEC_G2': finalQueryDfG2['BECRANGEML'].mean(), 'BEC_G3': finalQueryDfG3['BECRANGEML'].mean(), 'UEO_G1': finalQueryDfG1['UEORANGEML'].mean(), 'UEO_G2': finalQueryDfG2['UEORANGEML'].mean(),                 'UEO_G3': finalQueryDfG3['UEORANGEML'].mean(), 'UEC_G1': finalQueryDfG1['UECRANGEML'].mean(),               'UEC_G2': finalQueryDfG2['UECRANGEML'].mean(), 'UEC_G3': finalQueryDfG3['UECRANGEML'].mean(), 'BND_G1': finalQueryDfG1['BNDRANGEML'].mean(), 'BND_G2': finalQueryDfG2['BNDRANGEML'].mean(), 'BND_G3': finalQueryDfG3['BNDRANGEML'].mean()},
        #{'row_name': 'MV AP',       'BEO_G1': 0.0, 'BEO_G2': 0.0, 'BEO_G3': 0.0, 'BEC_G1': 0.0, 'BEC_G2': 0.0, 'BEC_G3': 0.0, 'UEO_G1': 0.0, 'UEO_G2': 0.0, 'UEO_G3': 0.0, 'UEC_G1': 0.0, 'UEC_G2': 0.0, 'UEC_G3': 0.0, 'BND_G1': 0.0, 'BND_G2': 0.0, 'BND_G3': 0.0},
        #{'row_name': 'MV ML',       'BEO_G1': 0.0, 'BEO_G2': 0.0, 'BEO_G3': 0.0, 'BEC_G1': 0.0, 'BEC_G2': 0.0, 'BEC_G3': 0.0, 'UEO_G1': 0.0, 'UEO_G2': 0.0, 'UEO_G3': 0.0, 'UEC_G1': 0.0, 'UEC_G2': 0.0, 'UEC_G3': 0.0, 'BND_G1': 0.0, 'BND_G2': 0.0, 'BND_G3': 0.0},
        {'row_name': 'RMS AP',      'BEO_G1': finalQueryDfG1['BEORMSAP'].mean(), 'BEO_G2': finalQueryDfG2['BEORMSAP'].mean(), 'BEO_G3': finalQueryDfG3['BEORMSAP'].mean(), 'BEC_G1': finalQueryDfG1['BECRMSAP'].mean(), 'BEC_G2': finalQueryDfG2['BECRMSAP'].mean(), 'BEC_G3': finalQueryDfG3['BECRMSAP'].mean(), 'UEO_G1': finalQueryDfG1['UEORMSAP'].mean(), 'UEO_G2': finalQueryDfG2['UEORMSAP'].mean(),                                 'UEO_G3': finalQueryDfG3['UEORMSAP'].mean(), 'UEC_G1': finalQueryDfG1['UECRMSAP'].mean(),                   'UEC_G2': finalQueryDfG2['UECRMSAP'].mean(), 'UEC_G3': finalQueryDfG3['UECRMSAP'].mean(), 'BND_G1': 0.0, 'BND_G2': 0.0, 'BND_G3': 0.0},
        {'row_name': 'RMS ML',      'BEO_G1': finalQueryDfG1['BEORMSML'].mean(), 'BEO_G2': finalQueryDfG2['BEORMSML'].mean(), 'BEO_G3': finalQueryDfG3['BEORMSML'].mean(), 'BEC_G1': finalQueryDfG1['BECRMSML'].mean(), 'BEC_G2': finalQueryDfG2['BECRMSML'].mean(), 'BEC_G3': finalQueryDfG3['BECRMSML'].mean(), 'UEO_G1': finalQueryDfG1['UEORMSML'].mean(), 'UEO_G2': finalQueryDfG2['UEORMSML'].mean(),                                 'UEO_G3': finalQueryDfG3['UEORMSML'].mean(), 'UEC_G1': finalQueryDfG1['UECRMSML'].mean(),                   'UEC_G2': finalQueryDfG2['UECRMSML'].mean(), 'UEC_G3': finalQueryDfG3['UECRMSML'].mean(), 'BND_G1': 0.0, 'BND_G2': 0.0, 'BND_G3': 0.0},
        {'row_name': 'F80 AP (Hz)', 'BEO_G1': finalQueryDfG1['BEOF80AP'].mean(), 'BEO_G2': finalQueryDfG2['BEOF80AP'].mean(), 'BEO_G3': finalQueryDfG3['BEOF80AP'].mean(), 'BEC_G1': finalQueryDfG1['BECF80AP'].mean(), 'BEC_G2': finalQueryDfG2['BECF80AP'].mean(), 'BEC_G3': finalQueryDfG3['BECF80AP'].mean(), 'UEO_G1': finalQueryDfG1['UEOF80AP'].mean(), 'UEO_G2': finalQueryDfG2['UEOF80AP'].mean(),                                 'UEO_G3': finalQueryDfG3['UEOF80AP'].mean(), 'UEC_G1': finalQueryDfG1['UECF80AP'].mean(),                   'UEC_G2': finalQueryDfG2['UECF80AP'].mean(), 'UEC_G3': finalQueryDfG3['UECF80AP'].mean(), 'BND_G1': 0.0, 'BND_G2': 0.0, 'BND_G3': 0.0},
        #{'row_name': 'F80 ML (Hz)', 'BEO_G1': 0.0, 'BEO_G2': 0.0, 'BEO_G3': 0.0, 'BEC_G1': 0.0, 'BEC_G2': 0.0, 'BEC_G3': 0.0, 'UEO_G1': 0.0, 'UEO_G2': 0.0, 'UEO_G3': 0.0, 'UEC_G1': 0.0, 'UEC_G2': 0.0, 'UEC_G3': 0.0, 'BND_G1': 0.0, 'BND_G2': 0.0, 'BND_G3': 0.0},
        {'row_name': 'Sent AP',     'BEO_G1': finalQueryDfG1['BEOSENTAP'].mean(), 'BEO_G2': finalQueryDfG2['BEOSENTAP'].mean(), 'BEO_G3': finalQueryDfG3['BEOSENTAP'].mean(), 'BEC_G1': finalQueryDfG1['BECSENTAP'].mean(), 'BEC_G2': finalQueryDfG2['BECSENTAP'].mean(), 'BEC_G3': finalQueryDfG3['BECSENTAP'].mean(), 'UEO_G1': finalQueryDfG1['UEOSENTAP'].mean(), 'UEO_G2': finalQueryDfG2['UEOSENTAP'].mean(),                         'UEO_G3': finalQueryDfG3['UEOSENTAP'].mean(), 'UEC_G1': finalQueryDfG1['UECSENTAP'].mean(),                 'UEC_G2': finalQueryDfG2['UECSENTAP'].mean(), 'UEC_G3': finalQueryDfG3['UECSENTAP'].mean(), 'BND_G1': 0.0, 'BND_G2': 0.0, 'BND_G3': 0.0},
        {'row_name': 'Sent ML',     'BEO_G1': finalQueryDfG1['BEOSENTML'].mean(), 'BEO_G2': finalQueryDfG2['BEOSENTML'].mean(), 'BEO_G3': finalQueryDfG3['BEOSENTML'].mean(), 'BEC_G1': finalQueryDfG1['BECSENTML'].mean(), 'BEC_G2': finalQueryDfG2['BECSENTML'].mean(), 'BEC_G3': finalQueryDfG3['BECSENTML'].mean(), 'UEO_G1': finalQueryDfG1['UEOSENTML'].mean(), 'UEO_G2': finalQueryDfG2['UEOSENTML'].mean(),                         'UEO_G3': finalQueryDfG3['UEOSENTML'].mean(), 'UEC_G1': finalQueryDfG1['UECSENTML'].mean(),                 'UEC_G2': finalQueryDfG2['UECSENTML'].mean(), 'UEC_G3': finalQueryDfG3['UECSENTML'].mean(), 'BND_G1': 0.0, 'BND_G2': 0.0, 'BND_G3': 0.0},
        {'row_name': 'CrossSent',    'BEO_G1': finalQueryDfG1['BEOCROSSSENT'].mean(), 'BEO_G2': finalQueryDfG2['BEOCROSSSENT'].mean(), 'BEO_G3': finalQueryDfG3['BEOCROSSSENT'].mean(), 'BEC_G1': finalQueryDfG1['BECCROSSSENT'].mean(), 'BEC_G2': finalQueryDfG2['BECCROSSSENT'].mean(), 'BEC_G3': finalQueryDfG3['BECCROSSSENT'].mean(), 'UEO_G1': finalQueryDfG1['UEOCROSSSENT'].mean(), 'UEO_G2': finalQueryDfG2['UEOCROSSSENT'].mean(), 'UEO_G3': finalQueryDfG3['UEOCROSSSENT'].mean(), 'UEC_G1': finalQueryDfG1['UECCROSSSENT'].mean(),          'UEC_G2': finalQueryDfG2['UECCROSSSENT'].mean(), 'UEC_G3': finalQueryDfG3['UECCROSSSENT'].mean(), 'BND_G1': 0.0, 'BND_G2': 0.0, 'BND_G3': 0.0},
    ]

    tableG = groups_response_table(table_dataG)
    tableG.show_header = True

    return render(request,'bLab/group_report.html',
                  {'stG':tableG})