# 03 - Negative current injections

import matplotlib as mpl
mpl.use('tkagg')   
import matplotlib.pyplot as plt
from neuron import h,gui 
from Golgi2020_morpho_2 import Golgi_morpho_2
import multiprocessing
import numpy as np

#Instantiation of the cell template
cell = Golgi_morpho_2()

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

#Neuron control menu and Voltage graph
h('load_file("vm.ses")')
h.nrncontrolmenu()

stimdata = dict()

#Basic properties of the simulation. dt, temperature, sim duration and initial voltage
h.dt = 0.025
h.celsius = 32
h.tstop = 3000
h.v_init = -65

for i in range(0,3):
    if i == 0:
        stimdata['stim0del'] = 1000
        stimdata['stim0dur'] = 1000
        stimdata['stim0amp'] = -0.1

    elif i == 1:
        stimdata['stim1del'] = 1000
        stimdata['stim1dur'] = 1000
        stimdata['stim1amp'] = -0.2
        
    elif i == 2:
        stimdata['stim2del'] = 1000
        stimdata['stim2dur'] = 1000
        stimdata['stim2amp'] = -0.3

    stim = [h.IClamp(0.5,sec=cell.soma[0])]

    if i == 0:
        stim[0].delay = stimdata['stim0del']
        stim[0].dur = stimdata['stim0dur']
        stim[0].amp = stimdata['stim0amp'] 

    elif i == 1:
        stim[0].delay = stimdata['stim1del']
        stim[0].dur = stimdata['stim1dur']
        stim[0].amp = stimdata['stim1amp'] 

    elif i == 2:
        stim[0].delay = stimdata['stim2del']
        stim[0].dur = stimdata['stim2dur']
        stim[0].amp = stimdata['stim2amp']    

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


    plt.savefig('03_Negative_current_trace_n_'+ str(i) + '.eps')
    plt.close()
    

quit()
