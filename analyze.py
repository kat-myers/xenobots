import numpy as np
import matplotlib.pyplot as plt
frontLegSensorValues = np.load('frontsensorvalues.npy')
plt.plot(frontLegSensorValues)
backLegSensorValues = np.load('backsensorvalues.npy')
plt.plot(frontLegSensorValues, linewidth = .5, label = 'Front Leg')
plt.plot(backLegSensorValues, linewidth = .5, label = 'Back Leg')
# sinwave = np.load('sinwave.npy')
# plt.plot(sinwave)
plt.legend()
plt.show()