import pybullet as p
import time
import pybullet_data
from salt.modules.sysfs import target

import pyrosim.pyrosim as pyrosim
import numpy
import random

from analyze import targetAnglesValues

amplitude = numpy.pi/4
frequency = 1
phaseOffset = 0

physicsClient = p.connect(p.GUI)
p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8,physicsClient)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

targetAngles = numpy.sin(numpy.linspace(0, (numpy.pi*2), 1000)) * (numpy.pi/4)
#numpy.save('data/ta.npy', targetAngles)

for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    pyrosim.Set_Motor_For_Joint(
        bodyIndex= robotId,
        jointName= b'Torso_BackLeg',
        controlMode= p.POSITION_CONTROL,
        targetPosition= targetAngles[i],
        maxForce= 30)

    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName=b'Torso_FrontLeg',
        controlMode=p.POSITION_CONTROL,
        targetPosition= targetAngles[i],
        maxForce=30)

    time.sleep(0.01)

numpy.save('data/blsv.npy', backLegSensorValues)
numpy.save('data/flsv.npy', frontLegSensorValues)

p.disconnect()

print(backLegSensorValues)