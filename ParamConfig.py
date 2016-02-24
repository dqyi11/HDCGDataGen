'''
Created on Feb 21, 2016

@author: hcmi
'''
from PyQt4 import QtGui, QtCore

class ParamConfig(QtGui.QDialog):


    def __init__(self, path_plan_info):
        super(QtGui.QDialog, self).__init__()
        self.path_plan_info = path_plan_info
        self.initUI()
        self.hide()
        
    def initUI(self):
        
        self.objFileLabel = QtGui.QLabel("Objective")
        self.objFileEdit = QtGui.QLineEdit()
        self.objFileEdit.setText(self.path_plan_info.costmap_file)
        self.objFileOpenBtn = QtGui.QPushButton("open")
        self.objFileOpenBtn.clicked.connect(self.openObjFile)
        
        self.maxIterationLabel = QtGui.QLabel("Max Iteration Num")
        self.maxIterationEdit = QtGui.QLineEdit()
        self.maxIterationEdit.setText(str(self.path_plan_info.iteration_num))
        
        self.segmentLabel = QtGui.QLabel("Segment Length")
        self.segmentEdit = QtGui.QLineEdit()
        self.segmentEdit.setText(str(self.path_plan_info.segment_length))
        
        self.btnOK = QtGui.QPushButton("OK")
        self.btnOK.clicked.connect(self.ok)
        self.btnCancel = QtGui.QPushButton("Cancel")
        self.btnCancel.clicked.connect(self.cancel)
        
        self.grid = QtGui.QGridLayout()
        self.grid.setSpacing(10)
        self.grid.addWidget(self.objFileLabel, 0, 0)
        self.grid.addWidget(self.objFileEdit, 0, 1)
        self.grid.addWidget(self.objFileOpenBtn, 0, 2)
        self.grid.addWidget(self.maxIterationLabel, 1, 0)
        self.grid.addWidget(self.maxIterationEdit, 1, 1)
        self.grid.addWidget(self.segmentLabel, 2, 0)
        self.grid.addWidget(self.segmentEdit, 2, 1)
        self.grid.addWidget(self.btnOK, 3, 0)
        self.grid.addWidget(self.btnCancel, 3, 1)
        
        self.setLayout(self.grid)
        
    def openObjFile(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file')
        if fname != None:
            self.objFileEdit.setText(fname)
            self.repaint()
        
        
    def ok(self):
        self.path_plan_info.costmap_file = self.objFileEdit.text()
        self.path_plan_info.segment_length = int(self.segmentEdit.text())
        self.path_plan_info.iteration_num = int(self.maxIterationEdit.text())
        self.hide()
        
    def cancel(self):
        self.hide()
        