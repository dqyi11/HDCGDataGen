'''
Created on Feb 19, 2016

@author: walter
'''

from PyQt4 import QtGui, QtCore
from MapViewer import *
from ObstacleEditConfig import *

class MapViewWindow(QtGui.QMainWindow):

    def __init__(self):
        super(QtGui.QMainWindow, self).__init__()
        self.initUI()
        
    def initUI(self):
        
        self.setWindowTitle("HDCG Data Gen")
        openAction = QtGui.QAction('Open', self)
        openAction.triggered.connect(self.openMap)
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openAction)
        
        self.view = MapViewer(self)
        self.setCentralWidget(self.view)
        
        self.obsConfig = ObstacleEditConfig()
        
        self.show()
        
    def openMap(self):
        
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file')
        if fname != None:
            self.view.openMap( str(fname) )
        
    def mousePressEvent(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            x_pos = e.pos().x()
            y_pos = e.pos().y()
            for obs in self.view.obstacles:
                if obs.contains( [x_pos, y_pos] ):
                    print obs.name    
                    self.obsConfig.setObstacle(obs)
                    self.obsConfig.show()