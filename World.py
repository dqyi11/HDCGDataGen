'''
Created on Feb 20, 2016

@author: hcmi
'''

import numpy as np

class World(object):


    def __init__(self):
        self.width = 0
        self.height = 0
        self.obstacles = []
        self.start = None
        self.goal = None
        self.fullpath = ""
        self.filename = ""
        self.name = ""
        
    def samplePoint(self):
        
        while True:
            x = np.random.randint(self.width)
            y = np.random.randint(self.height)
            if False==self.inObstacle(x, y):
                return [x,y]
            
    def inObstacle(self, x, y):
        for obs in self.obstacles:
            if obs.contains([x, y]):
                return True
        return False
        