import pybullet as p
import time
import pybullet_data

import pyrosim.pyrosim as pyrosim
import numpy
import constants as c

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        #self.motorValues = numpy.zeros(1000)

    def Set_Value(self, robotID, desiredAngle):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robotID,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=desiredAngle,
            maxForce=200)

        #print(self.motorValues[desiredAngle])
