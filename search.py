import os
from hillclimber import HILL_CLIMBER

# for x in range(5):
#     os.system("python3 generate.py")
#     os.system("python3 simulate.py")

hc = HILL_CLIMBER()
hc.Evolve()