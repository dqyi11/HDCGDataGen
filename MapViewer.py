'''
Created on Feb 19, 2016

@author: walter
'''

from PyQt4 import QtGui, QtCore
import cv, cv2
import os.path
from Obstacle import *
from World import *

class MapViewer(QtGui.QLabel):

    def __init__(self, parent):
        super(MapViewer, self).__init__(parent)
        self.world = World()
        
    def openMap(self, filename):
        img = cv2.imread(filename, cv2.CV_LOAD_IMAGE_GRAYSCALE)
        self.world.width = img.shape[1]
        self.world.height = img.shape[0]
        ret, im_bw = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(im_bw,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        obs_idx = 0
        for i in range(1, len(contours)):
            cont = contours[i]
            obs_points = []
            for p in cont:
                obs_points.append([p[0,0], p[0,1]])
            x,y,w,h = cv2.boundingRect(cont)    
            obs = Obstacle(obs_points, obs_idx, [x+w/2, y+h/2])
            obs_idx += 1
            self.world.obstacles.append(obs)
        pix = QtGui.QPixmap(img.shape[1], img.shape[0])
        pix.fill(QtGui.QColor(255,255,255))
        self.setPixmap(pix)
        
        self.world.fullpath = filename
        self.world.filename = os.path.basename(filename)
        self.world.name = os.path.splitext(self.world.filename)[0]
        
        
    def paintEvent(self, e):
        super(MapViewer, self).paintEvent(e)
        
        qp = QtGui.QPainter()
        qp.begin(self)
        
        qp.setPen(QtGui.QPen(QtGui.QColor(125,125,125)))
        #qp.setBrush(QtGui.QBrush(QtGui.QColor(0,0,0)))
        for obs in self.world.obstacles:
            qp.drawPolygon( obs.viz_polygon )
        
        qp.setPen(QtGui.QPen(QtGui.QColor(125,125,125)))
        for obs in self.world.obstacles:
            qp.drawText(obs.centroid[0], obs.centroid[1], obs.name)
        
        qp.setBrush(QtGui.QBrush(QtGui.QColor(255,0,0)))
        if self.world.start != None:
            qp.drawRect(self.world.start[0], self.world.start[1],4,4)
        
        qp.setBrush(QtGui.QColor(QtGui.QColor(0,0,255)))
        if self.world.goal != None:
            qp.drawRect(self.world.goal[0], self.world.goal[1],4,4)
        
        qp.end()
        

            
            
        