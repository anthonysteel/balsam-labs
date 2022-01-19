import mujoco_py
import numpy as np
import os
xml_path = './Adroit_hand.xml'
model = mujoco_py.load_model_from_path(xml_path)
sim = mujoco_py.MjSim(model)
viewer = mujoco_py.MjViewer(sim)

sim_state = sim.get_state()

#print(sim.data.ctrl)
#print(len(sim.data.ctrl))
while True:
    new_dat = sim.data.sensordata
    for i in range(0, 10):
        sim.data.ctrl[0] = sim.data.ctrl[0] + i * 10000
        sim.data.ctrl[1] = sim.data.ctrl[1] + i * 10000
        sim.data.ctrl[2] = sim.data.ctrl[2] + i * 10000
        sim.step()
        print(sim.data.sensordata)
        viewer.render()
    for i in range(0, 10):
        sim.data.ctrl[0] = sim.data.ctrl[0] - i * 10000
        sim.data.ctrl[1] = sim.data.ctrl[1] - i * 10000
        sim.data.ctrl[2] = sim.data.ctrl[2] - i * 10000
        sim.step()
        print(sim.data.sensordata)
        viewer.render()
