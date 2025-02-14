import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random

physicsClient = p.connect(p.GUI)
p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8,physicsClient)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(10000)
frontLegSensorValues = numpy.zeros(10000)

for i in range(10000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    pyrosim.Set_Motor_For_Joint(
        bodyIndex= robotId,
        jointName= b'Torso_BackLeg',
        controlMode= p.POSITION_CONTROL,
        targetPosition= -numpy.pi/6.0,
        maxForce= 500)

    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName=b'Torso_FrontLeg',
        controlMode=p.POSITION_CONTROL,
        targetPosition= numpy.pi/6.0,
        maxForce=500)

    time.sleep(0.05)

numpy.save('data/blsv.npy', backLegSensorValues)
numpy.save('data/flsv.npy', frontLegSensorValues)
p.disconnect()

print(backLegSensorValues)