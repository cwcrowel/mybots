import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load('data/blsv.npy')
frontLegSensorValues = numpy.load('data/flsv.npy')
x = list(range(1, 101))
matplotlib.pyplot.plot(backLegSensorValues, label = "Back Leg", linewidth = 2)
matplotlib.pyplot.plot(frontLegSensorValues, label = "Front Leg")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()

