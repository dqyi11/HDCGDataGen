'''
Created on Feb 19, 2016

@author: walter
'''

from MapViewWindow import *
from PyQt4 import QtGui, QtCore
import sys

if __name__ == '__main__':
    
    app = QtGui.QApplication(sys.argv)
    window = MapViewWindow()
    sys.exit(app.exec_())