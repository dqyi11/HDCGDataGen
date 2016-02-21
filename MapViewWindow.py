'''
Created on Feb 19, 2016

@author: walter
'''

from PyQt4 import QtGui, QtCore
from MapViewer import *
from ObstacleEditConfig import *
from ParamConfig import *
from BatchConfig import *
from PathPlanningInfo import *
import os

class MapViewWindow(QtGui.QMainWindow):

    def __init__(self):
        super(QtGui.QMainWindow, self).__init__()
        self.initUI()
        
    def initUI(self):
        
        self.setWindowTitle("HDCG Data Gen")
        openAction = QtGui.QAction('Open', self)
        openAction.triggered.connect(self.openMap)
        
        exportAction = QtGui.QAction('Export', self)
        exportAction.triggered.connect(self.exportXML)
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openAction)
        fileMenu.addAction(exportAction)
        
        configAction = QtGui.QAction('Config', self)
        configAction.triggered.connect(self.openConfig)
        randomAction = QtGui.QAction('Random', self)
        randomAction.triggered.connect(self.randomMap)
        sampleSpatialRelationAction = QtGui.QAction('Random Spatial Relation', self)
        sampleSpatialRelationAction.triggered.connect(self.sampleSpatialRelation)
        batchAction = QtGui.QAction('Batch', self)
        batchAction.triggered.connect(self.batchGen)
        
        toolMenu = menubar.addMenu('&Tool')
        toolMenu.addAction(configAction)
        toolMenu.addAction(randomAction)
        toolMenu.addAction(sampleSpatialRelationAction)
        toolMenu.addAction(batchAction)
        
        self.view = MapViewer(self)
        self.setCentralWidget(self.view)
        
        self.obsConfig = ObstacleEditConfig()
        self.paramConfig = None
        
        self.show()
        
    def openMap(self):
        
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file')
        if fname != None:
            self.view.openMap( str(fname) )
            self.setWindowTitle( self.view.world.name )
            self.path_plan_info = PathPlanningInfo( self.view.world )
            self.paramConfig = ParamConfig(self.path_plan_info)
            
    def openConfig(self):
        if self.path_plan_info != None:
            self.paramConfig.show()
            
        
    def mousePressEvent(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            x_pos = e.pos().x()
            y_pos = e.pos().y()
            for obs in self.view.world.obstacles:
                if obs.contains( [x_pos, y_pos] ):
                    print obs.name    
                    self.obsConfig.setObstacle(obs)
                    self.obsConfig.show()
                
    def randomMap(self):
        print "random map"
        self.view.world.start = self.view.world.samplePoint()
        self.view.world.goal = self.view.world.samplePoint()
        self.repaint()
        
    def sampleSpatialRelation(self, show_message = True):
        self.path_plan_info.randomSpatialRelation()
        if show_message == True:
            QtGui.QMessageBox.about( self, "Spatial Relation", str( self.path_plan_info.spatial_relations[0] ) )
        
    def exportXML(self):
        
        fname = QtGui.QFileDialog.getSaveFileName(self, 'Save file')
        if fname != None:
            self.path_plan_info.write_to_xml(str(fname))
            
    def batchGen(self):
        batch_info = BatchInfo()
        batch_config = BatchConfig(batch_info)
        batch_config.exec_()
        
        for i in range(batch_info.batch_num):
            self.randomMap()
            self.sampleSpatialRelation(False)
            self.path_plan_info.path_output_file = self.path_plan_info.world.name + "-" + str(i)
            fname = batch_info.workspace + "/" + self.path_plan_info.path_output_file + ".xml"
            self.path_plan_info.write_to_xml(fname)
            
            cmd = batch_info.workspace + "/h2p-harrts-demo"
            os.system(cmd + " " + fname)
        
        return
                    
                    