import numpy
import time
import pybullet_data
import pyrosim as pyrosim
import random
import constants as c
import pybullet as p
import time

class SIMULATION: #names class
    def __init__(self): # defines constructor for class
        self.world = WORLD()
        self.robot = ROBOT()
    
    def Run(self):
        for i in range(c.inum_iters):
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Act(t)
            time.sleep(c.sleep_time)
    
    def __del__(self):
        p.disconnect