import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1
x = 0
y = 0
z = 0.5

pyrosim.Start_SDF("boxes.sdf")
for i in range(10):
    pyrosim.Send_Cube(name="Box", pos=[x+i, y, z] , size=[length, width, height])
    # Reposition
    length = length * 0.9
    width = width * 0.9
    height = height * 0.9
    # Resize
    x = x - 1
    y = y
    z = z + 1

pyrosim.End()