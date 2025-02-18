import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load('data/blsv.npy')
frontLegSensorValues = numpy.load('data/flsv.npy')
targetAnglesValues = numpy.load('data/ta.npy')
backLegSineValues = numpy.load('data/blsv2.npy')
frontLegSineValues = numpy.load('data/flsv2.npy')
x = list(range(1, 101))
#matplotlib.pyplot.plot(backLegSensorValues, label = "Back Leg", linewidth = 2)
#matplotlib.pyplot.plot(frontLegSensorValues, label = "Front Leg")
#matplotlib.pyplot.legend()
#matplotlib.pyplot.show()

#matplotlib.pyplot.plot(targetAnglesValues, label = "Target Angles", linewidth = 2)
matplotlib.pyplot.plot(backLegSineValues, label = "Target Angles", linewidth = 2)
matplotlib.pyplot.plot(frontLegSineValues, label = "Target Angles", linewidth = 2)
matplotlib.pyplot.title("Motor Commands")
matplotlib.pyplot.xlabel('Steps')
matplotlib.pyplot.ylabel('Value in Radians')
matplotlib.pyplot.axis('tight')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
