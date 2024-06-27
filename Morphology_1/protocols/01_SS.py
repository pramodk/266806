# 01 - Spontaneuons firing
# This protocol tests the Spontaneuons generation of the action potentials

#import matplotlib as mpl
#mpl.use('tkagg')
#import matplotlib.pyplot as plt

from neuron import h,gui 
from Golgi2020_morpho_1 import Golgi_morpho_1
import multiprocessing
import numpy as np
import sys
import os

mycpu = multiprocessing.cpu_count()
mycpu = int(os.environ['NRN_THREADS']) if 'NRN_THREADS' in os.environ else mycpu

#Instantiation of the cell template
#cell = [Golgi_morpho_1() for _ in range(24)]
cell = [Golgi_morpho_1()]

#fixed time step only
Fixed_step = h.CVode()
Fixed_step.active(0)

h.load_file("parcom.hoc")
p = h.ParallelComputeTool()
if mycpu > 1.0:
    p.change_nthread(mycpu,1)
    p.multisplit(1)

#Voltage graph
h('load_file("vm.ses")')

#Neuron control menu
h.nrncontrolmenu()

#Basic properties of the simulation. dt, temperature, sim duration and initial voltage
h.dt = 0.025
h.celsius = 32
h.tstop = 100
h.v_init = -65

pc = h.ParallelContext()
for i, c in enumerate(cell):
    pc.set_gid2node(i, 0)
    pc.cell(i, c.nc_spike)

pc.set_maxstep(10)


#Initialization 
def run():
    import time
    h.stdinit()
    t0 = time.time()
    pc.psolve(h.tstop)
    t1 = time.time()
    print("NEURON RUN with %d threads took %f " % (mycpu, t1-t0))

run()
h.quit()

'''
#Save the results into an image
fig, ax = plt.subplots()
ax.plot(np.array(cell.time_vector), np.array(cell.vm), 'b', label='spikes')

legend = ax.legend(loc='upper right', shadow=True)

frame = legend.get_frame()
frame.set_facecolor('0.90')

plt.xlabel("time (ms)")
plt.ylabel("membrane voltage (mv) ")


plt.savefig('01_SS_trace.eps')
plt.close()
'''
