import numpy

amplitude = numpy.pi/4
frequency = 60
phaseOffset = numpy.pi/3

sleepTime = 0.0001

targetAngles = numpy.linspace(-numpy.pi, numpy.pi, 1000)

numberOfGenerations = 12
populationSize = 12

numSensorNeurons = 9
numMotorNeurons = 8

motorJointRange = 0.2