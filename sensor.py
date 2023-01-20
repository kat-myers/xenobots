class SENSOR: #names class
    def __init__(self, linkName): # defines constructor for class
        self.linkName = linkNameself.values = np.zeros(num_iters)

    def Get_Value(self,t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        if t == c.num_iters - 1:
            print(self.values)

    def Save_Values(self):
        np.save('data/sensorValues.npy', self.values)