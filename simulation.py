import numpy
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import random
import constants as c
import pybullet as p
class SIMULATION: #names class
    def __init__(self): # defines constructor for class
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.planeId = p.loadURDF("plane.urdf")
        self.worldId = p.loadSDF("world.sdf")
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(robotId)
        self.world = WORLD()
        self.robot = ROBOT()
    def Run(self):
        for i in range(c.iterations):
            p.stepSimulation()
            time.sleep(c.sleep)
    def __del__(self):
        p.disconnect