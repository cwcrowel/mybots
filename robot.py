from sensor import SENSOR
from motor import MOTOR
import pybullet as p

import pyrosim.pyrosim as pyrosim
import numpy
import constants as c
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os

class ROBOT:
    def __init__(self, server, solutionID):
        self.robotId = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK((f"brain{solutionID}.nndf"))
        os.system(f"rm brain{solutionID}.nndf")
        self.heights = []

    def Prepare_To_Sense(self):
        self.sensors = {}

        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for i in self.sensors:
            self.values = self.sensors.get(i).Get_Value(t)

        # Get robot height
        position, temp = p.getBasePositionAndOrientation(self.robotId)
        height = position[2]
        self.heights.append(height)

    def Prepare_To_Act(self):
        self.motors = {}

        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)


    def Act(self, desiredAngle):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName).encode("utf-8")
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                self.motors[jointName].Set_Value(self.robotId, desiredAngle)


    def Think(self):
        self.nn.Update()
        #self.nn.Print()

    def Get_Fitness(self, solutionID):
        #stateOfLinkZero = p.getLinkState(self.robotId, 0)
        #positionOfLinkZero = stateOfLinkZero[0]
        #xCoordinateOfLinkZero = positionOfLinkZero[0]

        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
        basePosition = basePositionAndOrientation[0]
        xCoordinateOfLinkZero = basePosition[0]

        lower_leg_sensors = ["FrontLowerLeg", "BackLowerLeg", "LeftLowerLeg", "RightLowerLeg"]
        fll_sensor_values = []
        bll_sensor_values = []
        lll_sensor_values = []
        rll_sensor_values = []

        for sensorName in lower_leg_sensors:
            if sensorName == "FrontLowerLeg":
                fll_sensor_values.append(self.sensors.get(sensorName).values)
            elif sensorName == "BackLowerLeg":
                bll_sensor_values.append(self.sensors.get(sensorName).values)
            elif sensorName == "LeftLowerLeg":
                lll_sensor_values.append(self.sensors.get(sensorName).values)
            elif sensorName == "RightLowerLeg":
                rll_sensor_values.append(self.sensors.get(sensorName).values)

        fll_sensor_values = numpy.concatenate(fll_sensor_values).tolist() if fll_sensor_values else []
        bll_sensor_values = numpy.concatenate(bll_sensor_values).tolist() if bll_sensor_values else []
        lll_sensor_values = numpy.concatenate(lll_sensor_values).tolist() if lll_sensor_values else []
        rll_sensor_values = numpy.concatenate(rll_sensor_values).tolist() if rll_sensor_values else []
        min_length = min(len(fll_sensor_values), len(bll_sensor_values), len(lll_sensor_values), len(rll_sensor_values))
        air = 0
        ground = 0

        for i in range(min_length):
            if (fll_sensor_values[i] == -1.0) and (bll_sensor_values[i] == -1.0) and (lll_sensor_values[i] == -1.0) and (rll_sensor_values[i] == -1.0):
                air += 1
            elif (fll_sensor_values[i] == 1.0) and (bll_sensor_values[i] == 1.0) and (lll_sensor_values[i] == 1.0) and (rll_sensor_values[i] == 1.0):
                ground += 1
            else:
                pass

        avg_height = sum(self.heights) / len(self.heights)

        with open(f'tmp{solutionID}.txt', 'w') as f:
            f.write(f'\n# of time steps where all touch sensors = -1: {air}\n# of time steps where all touch sensors = +1: {ground}\nAverage Height: {avg_height:.3f}')

        os.rename("tmp"+str(solutionID)+".txt" , "fitness"+str(solutionID)+".txt")

