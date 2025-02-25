import pybullet as p
import time
import pybullet_data

import pyrosim.pyrosim as pyrosim
import numpy
import constants as c

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()
        #self.motorValues = numpy.zeros(1000)

    def Prepare_To_Act(self):
        self.amplitude = c.amplitude
        self.frequency = c.frequency
        self.offset = c.phaseOffset

        if self.jointName != "Torso_BackLeg":
            self.frequency = self.frequency/2

        self.motorValues = self.amplitude * numpy.sin(self.frequency * c.targetAngles + self.offset)


    def Set_Value(self, robotID, t):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robotID,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=self.motorValues[t],
            maxForce=30)

        #print(self.motorValues[t])

    def Save_Values(self):
        numpy.save('data/mv.npy', self.motorValues)