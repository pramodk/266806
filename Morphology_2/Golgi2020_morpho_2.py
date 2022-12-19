from neuron import h
import math
import numpy as np
from Synapses import Synapse_py3

class Golgi_morpho_2():
    def __init__(self):
        
        h.load_file('stdlib.hoc')
        h.load_file('import3d.hoc')
        
        cell = h.Import3d_Neurolucida3()
        cell.input('morphology/pair-140514-C2-1_split_2.asc')
            
        
        i3d = h.Import3d_GUI(cell,0)
        i3d.instantiate(self)
        
        conductvalues = np.genfromtxt("Optimization_result.txt")
      
#Soma

        self.soma[0].nseg = 1 + (2 * int(self.soma[0].L / 40))
        self.soma[0].Ra = 122
        self.soma[0].cm = 1 
        
        self.soma[0].insert('Leak')
        self.soma[0].gmax_Leak = 0.00003
        self.soma[0].e_Leak = -55
        
        self.soma[0].insert('Nav1_6')
        self.soma[0].gbar_Nav1_6 = conductvalues[9]
        self.soma[0].ena = 60
	
        self.soma[0].insert('Kv1_1')
        self.soma[0].gbar_Kv1_1 = conductvalues[10]
	
        self.soma[0].insert('Kv3_4')
        self.soma[0].gkbar_Kv3_4 = conductvalues[11]
        
        self.soma[0].insert('Kv4_3')
        self.soma[0].gkbar_Kv4_3 = conductvalues[12]	
	  
        self.soma[0].insert('Kca1_1')
        self.soma[0].gbar_Kca1_1 = conductvalues[13]
	  
        self.soma[0].insert('Kca3_1')
        self.soma[0].gkbar_Kca3_1 = conductvalues[14]
        
        self.soma[0].insert('GRC_CA')
        self.soma[0].gcabar_GRC_CA = conductvalues[15]
	
        self.soma[0].insert('Cav3_1')
        self.soma[0].pcabar_Cav3_1 = conductvalues[16]
        
        self.soma[0].ek = -80
        
        self.soma[0].insert('cdp5StCmod')
        self.soma[0].TotalPump_cdp5StCmod = 1e-7
        
        self.soma[0].eca = 137

	
        self.whatami = "golgi2020"
      
	  
##dend #to be redone
	
        self.dendbasal = []
        self.dendapical = []
        
        for en_index, d_sec in enumerate(self.dend):
            if en_index == 0 or en_index == 75 or en_index >= 103 and en_index <= 125 or en_index >= 153 and en_index <= 167:
                self.dendbasal.append(d_sec)
        
            if en_index >= 1 and en_index <= 74 or en_index >= 76 and en_index <= 102 or en_index >= 126 and en_index <= 152:
                self.dendapical.append(d_sec)              
                    
	
        #Dend apical	    
        for r in self.dendapical:
                r.nseg = 1 + (2 * int(r.L / 40))
                r.Ra = 122
                r.cm = 2.5
                
                r.insert('Leak')
                r.gmax_Leak = 0.00003
                r.e_Leak = -55
                
                r.insert('Nav1_6')
                r.gbar_Nav1_6 = conductvalues[0]
                r.ena = 60
                
                r.insert('Kca1_1')
                r.gbar_Kca1_1 = conductvalues[1]
                
                r.insert('Kca2_2')
                r.gkbar_Kca2_2 = conductvalues[2]
                r.ek = -80
                
                r.insert('Cav2_3')
                r.gcabar_Cav2_3 = conductvalues[3]
                
                r.insert('Cav3_1')
                r.pcabar_Cav3_1 = conductvalues[4]
                
                r.insert('cdp5StCmod')
                r.TotalPump_cdp5StCmod = 5e-9
                
                r.push()
                r.eca = 137
                h.pop_section()   
	
	
        #Dend basal	    
        for i in self.dendbasal:
                i.nseg = 1 + (2 * int(i.L / 40))
                i.Ra = 122
                i.cm = 2.5
                
                i.insert('Leak')
                i.gmax_Leak = 0.00003
                i.e_Leak = -55	
                
                i.insert('Nav1_6')
                i.gbar_Nav1_6 = conductvalues[5]
                i.ena = 60
                
                i.insert('Kca1_1')
                i.gbar_Kca1_1 = conductvalues[6]
                
                i.insert('Kca2_2')
                i.gkbar_Kca2_2 = conductvalues[7]
                i.ek = -80

                i.insert('GRC_CA')
                i.gcabar_GRC_CA = conductvalues[8]
                
                i.insert('cdp5StCmod')
                i.TotalPump_cdp5StCmod = 2e-9
                
                i.push()
                i.eca = 137
                h.pop_section()   
                    
	  

	  
	  
#axon
        for i,d in enumerate(self.axon):
            if i == 0:
                #AIS
                self.axon[i].nseg = 1 + (2 * int(self.axon[i].L / 40))
                self.axon[i].Ra = 122
                self.axon[i].cm = 1
                
                self.axon[i].insert('Leak')
                self.axon[i].gmax_Leak = 0.00003
                self.axon[i].e_Leak = -55
                
                self.axon[i].insert('HCN1')
                self.axon[i].gbar_HCN1 = conductvalues[17]
                
                self.axon[i].insert('HCN2')
                self.axon[i].gbar_HCN2 = conductvalues[18]
            
                self.axon[i].insert('Nav1_6')
                self.axon[i].gbar_Nav1_6 = conductvalues[19]
                self.axon[i].ena = 60
            
                self.axon[i].insert('GRC_KM')
                self.axon[i].gkbar_GRC_KM = conductvalues[20]
                
                self.axon[i].insert('Kca1_1')
                self.axon[i].gbar_Kca1_1 = conductvalues[21]               

                self.axon[i].insert('GRC_CA')
                self.axon[i].gcabar_GRC_CA = conductvalues[22]

                self.axon[i].ek = -80                 
                self.axon[i].insert('cdp5StCmod')	
                self.axon[i].TotalPump_cdp5StCmod = 1e-8
                
                self.axon[i].push()
                self.axon[i].eca = 137
                h.pop_section()  
                    
            elif i >= 1:
                #axon
                self.axon[i].nseg = 1 + (2 * int(self.axon[i].L / 40))
                self.axon[i].cm = 1
                self.axon[i].Ra = 122
                
                self.axon[i].insert('Leak')
                self.axon[i].e_Leak = -55
                self.axon[i].gmax_Leak = 0.000001

                self.axon[i].insert('Nav1_6')
                self.axon[i].gbar_Nav1_6 = conductvalues[23] 
                self.axon[i].ena = 60

                self.axon[i].insert('Kv3_4')
                self.axon[i].gkbar_Kv3_4 = conductvalues[24]
                self.axon[i].ek = -80  
                

                self.axon[i].insert('cdp5StCmod')	    
                self.axon[i].TotalPump_cdp5StCmod = 1e-8
                
                self.axon[i].push()
                self.axon[i].eca = 137
                h.pop_section()   
        
        #Code to record everything.
        
        self.nc_spike = h.NetCon(self.soma[0](1)._ref_v, None,-20,0.1,1, sec = self.soma[0])
        
        self.time_vector = h.Vector()
        self.time_vector.record(h._ref_t)

        self.vm = h.Vector()
        self.vm.record(self.soma[0](0.5)._ref_v)
        

    def createsyn(self, pf_n, mf_n, aa_n, inib_n):	
#pf       
        self.L_PF = []
        self.dend_pf = []
        
        #the list self.dend_pf is the same as self.dendapical... so....
        for sec_index, sec_sec in enumerate(self.dend):
            if sec_index >= 1 and sec_index <= 74 or sec_index >= 76 and sec_index <= 102 or sec_index >= 126 and sec_index <= 152:
                self.dend_pf.append(sec_sec)   

        #To increase the number of synpases for each seaction
        self.dend_pf = self.dend_pf *1

        print('self.dend_pf', len(self.dend_pf))
        
#PF location
        for i in range(0, pf_n):
            self.L_PF.append(Synapse_py3('PF',self,self.dend_pf[i])) 
                
        #self.L_PF = self.L_PF #* 82       
        print('pf_list_list', self.L_PF)
                
#mossy        
        self.L_MF = []
        self.L_MF_NMDA_B = []
        self.dend_mf = []
        self.dend_aa = []
        
        for sec_index, sec_sec in enumerate(self.dend):
             if sec_index >= 105 and sec_index <= 107 or sec_index >= 110 and sec_index <= 113 or sec_index >= 115 and sec_index <= 119 or sec_index >= 123 and sec_index <= 124 or sec_index >= 154 and sec_index <= 160 or sec_index >= 162 and sec_index <= 167:
                self.dend_mf.append(sec_sec)   
                self.dend_aa.append(sec_sec) 

        print('self.dend_mf', len(self.dend_mf))
        
#MF location      
        for i in range(0, mf_n):
            self.L_MF.append(Synapse_py3('MF',self,self.dend_mf[i])) 
            self.L_MF_NMDA_B.append(Synapse_py3('MF_nmda_B',self,self.dend_mf[i])) 

#AA 
        self.L_AA = [] 
        self.L_AA_NMDA_B = []
        
        for i in range(0, aa_n):
                self.L_AA.append(Synapse_py3('AA',self,self.dend_aa[i])) 
                self.L_AA_NMDA_B.append(Synapse_py3('MF_nmda_B',self,self.dend_aa[i])) 

