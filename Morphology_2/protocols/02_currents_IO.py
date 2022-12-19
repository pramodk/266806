# 02 - Positive current injections from 0.1 to 0.6nA.

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
h.tstop = 4000
h.v_init = -65
   
for i in range(0,6):
    if i == 0:
        stimdata['stim0del'] = 2000
        stimdata['stim0dur'] = 900 
        stimdata['stim0amp'] = 0.1 

    elif i == 1:
        stimdata['stim1del'] = 2000
        stimdata['stim1dur'] = 900 
        stimdata['stim1amp'] = 0.2
        
    elif i == 2:
        stimdata['stim2del'] = 2000
        stimdata['stim2dur'] = 900 
        stimdata['stim2amp'] = 0.3
        
    elif i == 3:
        stimdata['stim3del'] = 2000
        stimdata['stim3dur'] = 900 
        stimdata['stim3amp'] = 0.4 

    elif i == 4:
        stimdata['stim4del'] = 2000
        stimdata['stim4dur'] = 900 
        stimdata['stim4amp'] = 0.5
        
    elif i == 5:
        stimdata['stim5del'] = 2000
        stimdata['stim5dur'] = 900
        stimdata['stim5amp'] = 0.6 

    

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

    elif i == 3:
        stim[0].delay = stimdata['stim3del']
        stim[0].dur = stimdata['stim3dur']
        stim[0].amp = stimdata['stim3amp'] 

    elif i == 4:
        stim[0].delay = stimdata['stim4del']
        stim[0].dur = stimdata['stim4dur']
        stim[0].amp = stimdata['stim4amp'] 

    elif i == 5:
        stim[0].delay = stimdata['stim5del']
        stim[0].dur = stimdata['stim5dur']
        stim[0].amp = stimdata['stim5amp']    

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


    plt.savefig('02_Positive_current_trace_n_'+ str(i) + '.eps')
    plt.close()

quit()
