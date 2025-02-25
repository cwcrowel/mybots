from sensor import SENSOR
from motor import MOTOR
import pybullet as p
import time
import pybullet_data

import pyrosim.pyrosim as pyrosim
import numpy
import constants as c

class ROBOT:
    def __init__(self, server):
        self.robotId = p.loadURDF("body.urdf")

    def Prepare_To_Sense(self):
        self.sensors = {}

        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for i in self.sensors:
            self.values = self.sensors.get(i).Get_Value(t)

    def Prepare_To_Act(self):
        self.motors = {}

        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)


    def Act(self, robotId, t):
        for i in self.motors:
            self.motorValues = self.motors.get(i).Set_Value(robotId, t)
        print(self.motors)