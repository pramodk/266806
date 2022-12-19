# 01 - Spontaneuons firing
# This protocol tests the Spontaneuons generation of the action potentials

import matplotlib as mpl
mpl.use('tkagg')   
import matplotlib.pyplot as plt
from neuron import h,gui 
from Golgi2020_morpho_1 import Golgi_morpho_1
import multiprocessing
import numpy as np
import sys

#Instantiation of the cell template
cell = Golgi_morpho_1()

#fixed time step only
Fixed_step = h.CVode()
Fixed_step.active(0)

#this code discover the number of cores available in a CPU and activate the multisplit to use them all.
cpu = multiprocessing.cpu_count()
h.load_file("parcom.hoc")
p = h.ParallelComputeTool()
p.change_nthread(cpu,1)
p.multisplit(1)
print(cpu)

#Voltage graph
h('load_file("vm.ses")')

#Neuron control menu
h.nrncontrolmenu()

#Basic properties of the simulation. dt, temperature, sim duration and initial voltage
h.dt = 0.025
h.celsius = 32
h.tstop = 1000
h.v_init = -65

#Initialization 
def initialize():
    h.finitialize()
    h.run()

initialize()

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

