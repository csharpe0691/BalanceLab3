from django.shortcuts import render, render_to_response
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
from django.contrib.auth.decorators import login_required
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon


@login_required(login_url="login/")
def home(request):
    #print('in home')
    return render(request,"home.html")


class filePicker(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 file dialogs - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #self.openFileNameDialog()

        #self.show()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;MATLAB Files (*.mat)", options=options)
        if fileName:
            #print(fileName)
            #sys.exit(app.exec_())
            return fileName
        else:
            return ''

def loadFile(pickedFile):
    #parse the file and write the data into mongoDB
    print(pickedFile)

def pickFile():
    print('foo')
    app = QApplication(sys.argv)
    ex = filePicker()
    pickedFile = ex.openFileNameDialog()
    print('picked file:', pickedFile)
    if pickedFile != '':
       loadFile(pickedFile)


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


from django.shortcuts import render, render_to_response

from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
from bokeh.resources import INLINE

def samplePlot(request):
    print('in samplePlot')
    x = [1, 3, 5, 7, 9, 11, 13]
    y = [1, 2, 3, 4, 5, 6, 7]
    title = 'y = f(x)'

    plot = figure(title=title,
                  x_axis_label='X-Axis',
                  y_axis_label='Y-Axis',
                  plot_width=100,
                  plot_height=100)
    print('in samplePlot 2')
    plot.line(x, y, legend='f(x)', line_width=2)
    # Store components
    script, div = components(plot) #, INLINE)

    # Feed them to the Django template.
    return HttpResponse(script+div)



from django.http import HttpResponse



import scipy.io
import pymongo
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