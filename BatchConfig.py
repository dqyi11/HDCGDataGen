'''
Created on Feb 21, 2016

@author: hcmi
'''
from PyQt4 import QtGui, QtCore

class BatchInfo(object):
    
    def __init__(self):
        self.batch_num = 10

class BatchConfig(QtGui.QDialog):

    def __init__(self, batch_info):
        super(QtGui.QDialog, self).__init__()
        self.batch_info = batch_info
        self.initUI()
        self.show()
        
    def initUI(self):
        
        self.batchNumLabel = QtGui.QLabel("Batch Num")
        self.batchNumEdit = QtGui.QLineEdit()
        self.batchNumEdit.setText(str(self.batch_info.batch_num))
        
        self.btnOK = QtGui.QPushButton("OK")
        self.btnOK.clicked.connect(self.ok)
        
        self.grid = QtGui.QGridLayout()
        self.grid.setSpacing(10)
        self.grid.addWidget(self.batchNumLabel, 0, 0)
        self.grid.addWidget(self.batchNumEdit, 0, 1)
        self.grid.addWidget(self.btnOK, 1, 0)
        
        self.setLayout(self.grid)
        
    def ok(self):
        self.batch_info.batch_num = int(self.batchNumEdit.text())
        self.hide()
        
        
        