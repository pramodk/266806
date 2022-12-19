from neuron import h

class Synapse_py3:
    def __init__(self,source,target,section,weight = 1):
		
        self.input = h.NetStim(0.5)
        self.input.start = -10
        self.input.number = 1
        self.input.interval = 1e9
        self.weight = weight


        self.postsyns = {}

        if (type(source) == type('s')):
            sourcetype = source
           
                
#GOLGI
        if sourcetype == 'PF':
            if target.whatami == 'golgi2020':
                # Make a parallel fiber synapse onto a Golgi cell
                # Use deterministic synapses
                self.whatami = "syn_PF2GoC_det"
                self.postsyns['AMPA'] = [h.Golgi_PF_syn(0.5, sec=section)]
                self.postsyns['AMPA'][0].tau_facil=10.8*5
                self.postsyns['AMPA'][0].tau_rec=35.1
                self.postsyns['AMPA'][0].tau_1=30
                self.postsyns['AMPA'][0].gmax = 1200
                self.postsyns['AMPA'][0].U=0.4

                self.nc_syn = [h.NetCon(self.input,receptor[0],0,0.1,1) for receptor in self.postsyns.values()]


        elif sourcetype == 'MF':
            if target.whatami == 'golgi2020':
                # Make a mossy fiber synapse onto a Golgi cell
                # Use deterministic synapses
                self.whatami = "syn_MF2GoC_det"
                self.postsyns['AMPA'] = [h.Golgi_MF_syn(0.5, sec=section)]
                self.postsyns['AMPA'][0].tau_facil=8
                self.postsyns['AMPA'][0].tau_rec=5
                self.postsyns['AMPA'][0].tau_1=1
                self.postsyns['AMPA'][0].gmax = 1200
                self.postsyns['AMPA'][0].U = 0.43

                self.nc_syn = [h.NetCon(self.input,receptor[0],0,0.1,1) for receptor in self.postsyns.values()]
            
        elif sourcetype == 'MF_nmda_B':
            if target.whatami == 'golgi2020':
                # Make a  mossy fiber NMDAB onto a Golgi cell
                # Use deterministic synapses*
                self.whatami = "syn_MFB2GoC_det"
                self.postsyns['NMDA'] = [h.PC_NMDA_NR2B(0.5, sec=section)]
                self.postsyns['NMDA'][0].tau_facil=5
                self.postsyns['NMDA'][0].tau_rec=8
                self.postsyns['NMDA'][0].tau_1=1
                self.postsyns['NMDA'][0].gmax = 10000  
                self.postsyns['NMDA'][0].U=0.43
                #print 'nmda'
                self.nc_syn = [h.NetCon(self.input,receptor[0],0,0.1,1) for receptor in self.postsyns.values()]	
                
        elif sourcetype == 'AA': 
            if target.whatami == 'golgi2020':
                # Make a AA synapse onto a Golgi cell
                # Use deterministic synapses*
                self.whatami = "syn_AA2GoC_det"
                self.postsyns['AMPA'] = [h.Golgi_PF_syn(0.7, sec=section)]
                self.postsyns['AMPA'][0].tau_facil=54
                self.postsyns['AMPA'][0].tau_rec=35.1
                self.postsyns['AMPA'][0].tau_1=30
                self.postsyns['AMPA'][0].gmax = 1200 
                self.postsyns['AMPA'][0].U=0.4

                self.nc_syn = [h.NetCon(self.input,receptor[0],0,0.1,1) for receptor in self.postsyns.values()]

            
            
            
        
        else:
            print('SOURCE TYPE DOES NOT EXIST SOMETHING WRONG!!!!!!!!!')
            
