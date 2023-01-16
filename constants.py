import pybullet as p
import numpy
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import random

bl_amplitude = numpy.pi/4
bl_frequency = 20
bl_phaseOffset = 0

fl_amplitude = numpy.pi/4
fl_frequency = 20
fl_phaseOffset = -10

iterations = 1000
sleep = 1/60