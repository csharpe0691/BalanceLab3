from django.contrib.auth.decorators import login_required

@login_required(login_url="login/")
def home(request):
    #print('in home')
    return render(request,"home.html")

# Create your views here.

# this login required decorator is to not allow to any
# view without authenticating

@login_required()
def selector(request):
    return render(request, 'bLab/selector.html', {})

@login_required()
def initialize(request):
    # setup mongoDB connection
    print('about to connect to pymongo')

    client = MongoClient('mongodb://localhost:27017/')
    db = client.test_db
    col = db.test_collection

    print('pymongo connection created')

    return render(request, 'bLab/selection.html', {})

@login_required()
def single_patient_search(request):
    return render(request, 'bLab/single_patient_search.html', {})

@login_required()
def single_patient_BR(request):
    return render(request, 'bLab/single_patient_BR.html', {})

@login_required()
def group_compar(request):
    return render(request, 'bLab/group_compar.html', {})

@login_required()
def group_report(request):
    return render(request, 'bLab/group_report.html', {})


from django.shortcuts import render

from jchart import Chart
from jchart.config import Axes, DataSet

class LineChart(Chart):
    chart_type = 'bubble'
    legend = {
        'display' : False
    }

    def get_datasets(self, **kwargs):
        data = [{'y': 8, 'x': 3, 'r': 2},
                 {'y': 11, 'x': 5, 'r': 2},
                 {'y': 12, 'x': 8, 'r': 2},
                 {'y': 11, 'x': 11, 'r': 2},
                 {'y': 7, 'x': 11, 'r': 2},
                 {'y': 6, 'x': 14, 'r': 2},
                 {'y': 2, 'x': 12, 'r': 2},
                 {'y': 4, 'x': 9, 'r': 2},
                 {'y': 3, 'x': 6, 'r': 2},
                {'y': 8, 'x': 3, 'r': 2}]
        scales = {
            'xAxes': [Axes(type='linear', position='bottom')],
        }
        return [
            DataSet(type='line',
                    label='Line',
                    borderColor='red',
                    data=data)
        ]

def some_view(request):
    render(request, 'single_patient_BR.html', {
        'line_chart': LineChart(),
    })

import scipy.io
from pymongo import *

@login_required()
def loadFile(filename):
    mat = scipy.io.loadmat(filename)

    # print(type(mat))
    # print(mat.keys())

    record_doc = {
        'header': mat['__header__'],
        'version': mat['__version__'],
        'globals': mat['__globals__'],
        'patient_id': mat['final'][0][0][0],
        'first_name': mat['final'][1][0][0],
        'last_name': mat['final'][2][0][0]}
    return record_doc