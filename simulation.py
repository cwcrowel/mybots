import pybullet as p
import time
import pybullet_data

import pyrosim.pyrosim as pyrosim
import numpy
import constants as c

from world import WORLD
from robot import ROBOT

class SIMULATION:
    def __init__(self):

        self.physicsClient = p.connect(p.GUI)
        p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        p.setGravity(0,0,-9.8,self.physicsClient)

        self.world = WORLD()
        self.robot = ROBOT(p)

        pyrosim.Prepare_To_Simulate(self.robot.robotId)
        self.robot.Prepare_To_Sense()
        self.robot.Prepare_To_Act()

    def Run(self):
        for t in range(1000):
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Think()
            self.robot.Act(t)

            time.sleep(0.01)
            #print(t)

    def __del__(self):
        p.disconnect()