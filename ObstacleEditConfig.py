'''
Created on Feb 19, 2016

@author: walter
'''

from PyQt4 import QtGui, QtCore
from Obstacle import *

class ObstacleEditConfig(QtGui.QDialog):


    def __init__(self):
        super(QtGui.QDialog, self).__init__()
        self.obstacle = None
        self.initUI()
        self.hide()
        
    def initUI(self):
        
        self.obstacleNameLabel = QtGui.QLabel("Name")
        self.obstacleNameEdit = QtGui.QLineEdit()
        self.obstacleNameEdit.setText("")
        
        self.btnOK = QtGui.QPushButton("OK")
        self.btnOK.clicked.connect(self.ok)
        self.btnCancel = QtGui.QPushButton("Cancel")
        self.btnCancel.clicked.connect(self.cancel)
        
        self.okShortcut = QtGui.QShortcut(self)
        self.okShortcut.setKey(QtCore.Qt.Key_Enter)
        self.okShortcut.activated.connect(self.ok)
        
        self.grid = QtGui.QGridLayout()
        self.grid.setSpacing(10)
        self.grid.addWidget(self.obstacleNameLabel, 0, 0)
        self.grid.addWidget(self.obstacleNameEdit, 0, 1)
        self.grid.addWidget(self.btnOK, 1, 0)
        self.grid.addWidget(self.btnCancel, 1, 1)
        
        self.setLayout(self.grid)
        
        
    def setObstacle(self, obstacle):
        self.obstacle = obstacle
        self.obstacleNameEdit.setText( QtCore.QString( self.obstacle.name ) )
        
    def ok(self):
        self.obstacle.name = str( self.obstacleNameEdit.displayText() )
        self.hide()
        
    def cancel(self):
        self.hide()