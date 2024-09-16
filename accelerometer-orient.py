import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = "accelerometer-orient.csv"
df = pd.read_csv(data)
dataset = df.to_numpy()
t, ax, ay, az, amag = dataset.T

g = 9.88 # absolute mean acceleration 
pitch = [0]
roll = [0]
yaw = [0]

for i in np.arange(len(t)-1):
    pitch = np.arcsin(ax/g)
    roll = np.arctan(ay/az)

from vpython import *
plane = triangle(pos=vector(0,0,0), length = 0.10, thickness = 0.01, color=color.white, make_trail=False)

for i in range(len(t)):
    sleep(0.01)
    rotate(plane, axis=(1,0,0), angle=pitch[t[i+1]]-pitch[t[i]], origin=vec(0,0,0))
    rotate(plane, axis=(0,1,0), angle=roll[t[i+1]]-roll[t[i]], origin=vec(0,0,0))
    while True: 
        pass