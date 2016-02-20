'''
Created on Feb 19, 2016

@author: walter
'''
from PyQt4 import QtCore, QtGui
import shapely.geometry as shpgeo

class Obstacle(object):

    def __init__(self, points, idx, centroid):
        self.points = points
        self.idx = idx
        self.name = "OBS" + str(idx)
        self.centroid = centroid
        point_list = []
        for p in self.points:
            point_list.append( QtCore.QPoint( p[0], p[1] ) )
        self.viz_polygon = QtGui.QPolygon(point_list)
        self.polygon = shpgeo.Polygon(self.points)
        
    def contains(self, point):
        return self.polygon.contains(shpgeo.Point(point[0], point[1]))
    
        