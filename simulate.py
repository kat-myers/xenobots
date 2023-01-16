from simulation import SIMULATION
simulation = SIMULATION()
simulation.Run()

# planeId = p.loadURDF("plane.urdf")
# worldId = p.loadSDF("world.sdf")
# robotId = p.loadURDF("body.urdf")
# pyrosim.Prepare_To_Simulate(robotId)
# frontLegSensorValues = numpy.zeros(1000)
# backLegSensorValues = numpy.zeros(1000)
# #targetAngles = numpy.sin(numpy.linspace(-numpy.pi/4, numpy.pi/4, 1000))
# # values for motor angle vectors
# targetAngles = []

# # motor angle vectors
# angle_range = numpy.linspace(0, 2*numpy.pi, 1000)
# targetAngles_BackLeg = c.bl_amplitude * numpy.sin(c.bl_frequency * angle_range + c.bl_phaseOffset)
# targetAngles_FrontLeg = c.fl_amplitude * numpy.sin(c.fl_frequency * angle_range + c.fl_phaseOffset)
# for x in range(1000):
#     p.stepSimulation()
#     frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
#     backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex = robotId,
#         jointName = b'Torso_BackLeg',
#         controlMode = p.POSITION_CONTROL,
#         targetPosition = targetAngles_BackLeg[x],
#         maxForce = 400)
    
#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex = robotId,
#         jointName = b'Torso_FrontLeg',
#         controlMode = p.POSITION_CONTROL,
#         targetPosition = targetAngles_FrontLeg[x],
#         maxForce = 400)
#     time.sleep(1/60)
# with open('frontsensorvalues.npy', 'wb') as f:
#     numpy.save(f, frontLegSensorValues, allow_pickle=True, fix_imports=True)
# with open('backsensorvalues.npy', 'wb') as f:
#     numpy.save(f, backLegSensorValues, allow_pickle=True, fix_imports=True)
# # with open('sinwave.npy', 'wb') as f:
# #     numpy.save(f, targetAngles, allow_pickle=True, fix_imports=True)
# p.disconnect()
