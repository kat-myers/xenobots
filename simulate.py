import pybullet as p
import numpy
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)

planeId = p.loadURDF("plane.urdf")
worldId = p.loadSDF("world.sdf")
robotId = p.loadURDF("body.urdf")
pyrosim.Prepare_To_Simulate(robotId)
frontLegSensorValues = numpy.zeros(1000)

for x in range(1000):
    p.stepSimulation()
    frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    time.sleep(1/60)
p.disconnect()