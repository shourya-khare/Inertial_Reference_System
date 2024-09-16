import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = "accelerometer.csv"
df = pd.read_csv(data)
dataset = df.to_numpy()
t, ax, ay, az, amag = dataset.T

dt = t[1]-t[0]          # time interval b/w sensor readouts (varies slightly)
vx = [0]
vy = [0]
vz = [0]

for i in np.arange(len(t)-1):
    vx = vx + [vx[-1] + ax[i]*(t[i+1]-t[i])]
    vy = vy + [vy[-1] + ay[i]*(t[i+1]-t[i])]
    vz = vz + [vz[-1] + (az[i]-9.8)*(t[i+1]-t[i])]

x = [0]
y = [0]
z = [0]

for i in np.arange(len(t)-1):
    x = x + [x[-1] + vx[i]*(t[i+1]-t[i])]
    y = y + [y[-1] + vy[i]*(t[i+1]-t[i])]
    z = z + [z[-1] + (vz[i])*(t[i+1]-t[i])]

from vpython import *
ball = sphere(pos=vector(0,0,0), radius = 0.1, color=color.white, make_trail=True)

for i in range(len(t)):
    sleep(0.01)
    ball.pos = vector(y[i], z[i], x[i])
    pass
