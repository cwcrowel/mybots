import pybullet as p
import time
import pybullet_data

import pyrosim.pyrosim as pyrosim
import numpy
#import random



BackLeg_amplitude = numpy.pi/4
BackLeg_frequency = 20
BackLeg_phaseOffset = numpy.pi
FrontLeg_amplitude = numpy.pi/4
FrontLeg_frequency = 20
FrontLeg_phaseOffset = numpy.pi/3

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

targetAngles = numpy.linspace(-numpy.pi, numpy.pi, 1000)
BackLeg_out_array = BackLeg_amplitude * numpy.sin(BackLeg_frequency * targetAngles + BackLeg_phaseOffset)
FrontLeg_out_array = FrontLeg_amplitude * numpy.sin(FrontLeg_frequency * targetAngles + FrontLeg_phaseOffset)

#numpy.save('data/blsv2.npy', BackLeg_out_array)
#numpy.save('data/flsv2.npy', FrontLeg_out_array)
#exit()

for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    pyrosim.Set_Motor_For_Joint(
        bodyIndex= robotId,
        jointName= b'Torso_BackLeg',
        controlMode= p.POSITION_CONTROL,
        targetPosition= BackLeg_out_array[i],
        maxForce= 30)

    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName=b'Torso_FrontLeg',
        controlMode=p.POSITION_CONTROL,
        targetPosition= FrontLeg_out_array[i],
        maxForce=30)

    time.sleep(0.01)

numpy.save('data/blsv.npy', backLegSensorValues)
numpy.save('data/flsv.npy', frontLegSensorValues)

p.disconnect()

print(backLegSensorValues)