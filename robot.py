
import numpy
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import constants as c
import pybullet as p
import pybullet_data
from sensor import SENSOR

class ROBOT: #names class
    def __init__(self): # defines constructor for class
        self.motors = {}
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()

    def Prepare_to_Sense(self):
        self.sensor = {}
        for link in pyrosim.linkNamestoIndices:
            self.sensors[linkName] = SENSOR(linkname)
    
    # def Sense(self):
    #     for i,sensor in enumerate(self.sensors):