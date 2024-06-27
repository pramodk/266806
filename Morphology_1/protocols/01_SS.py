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

#import itt
#itt.pause()


#this code discover the number of cores available in a CPU and activate the multisplit to use them all.
mycpu = multiprocessing.cpu_count()
# for benchmarking
import os
mycpu = int(os.environ['NRN_THREADS']) if 'NRN_THREADS' in os.environ else 1

#Instantiation of the cell template
cell = [Golgi_morpho_1() for _ in range(24)]

#fixed time step only
Fixed_step = h.CVode()
Fixed_step.active(0)

h.load_file("parcom.hoc")
p = h.ParallelComputeTool()
if mycpu > 1.0:
    p.change_nthread(mycpu,1)
    #p.multisplit(1)

#Voltage graph
h('load_file("vm.ses")')

#Neuron control menu
h.nrncontrolmenu()

#Basic properties of the simulation. dt, temperature, sim duration and initial voltage
h.dt = 0.025
h.celsius = 32
h.tstop = 10
h.v_init = -65

pc = h.ParallelContext()
for i, c in enumerate(cell):
    pc.set_gid2node(i, 0)
    pc.cell(i, c.nc_spike)

pc.set_maxstep(10)


#Initialization 
def initialize(enable_coreneuron):

    from neuron import coreneuron
    coreneuron.enable = enable_coreneuron
    coreneuron.file_mode = 0

    h.finitialize(-65)
    import time
    t0 = time.time()
    print("Starting Run CN: #ccores active: %d" % mycpu)
    #itt.resume()
    #h.run()
#    h.stdinit()
    pc.psolve(h.tstop)
    #itt.pause()
    t1 = time.time()
    print("NEURON RUN with %d threads took %f " % (mycpu, t1-t0))

initialize(False)
#initialize(True)

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
