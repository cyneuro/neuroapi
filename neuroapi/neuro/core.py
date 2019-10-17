import matplotlib
matplotlib.use('pdf') #https://stackoverflow.com/questions/19518352/tkinter-tclerror-couldnt-connect-to-display-localhost18-0
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
from io import BytesIO
import base64

import neuron
from neuron import h
h.load_file('stdrun.hoc')

def run_cell(diam,cm,el,gl,gna,gh,gk,tstop,dur,amp,mhalf,hhalf,mk,hk,nhalf,kn,multiply,multiply1,multiply2,seg1,seg2,seg3):
    #Load the mechanisms in the current directory
    neuron.load_mechanisms(os.path.dirname(os.path.abspath(__file__)))

    Passive = [1,-1,-65]
    soma = h.Section(name='soma')
    soma.L = 100 # um
    soma.insert('hh')
    
    v0_vec = h.Vector()
    t_vec = h.Vector()
    
    v0_vec.record(soma(0.5)._ref_v)
    t_vec.record(h._ref_t)
    
    soma.insert('na1')
    soma.insert('k1')
    soma.insert('hd')

    m_na = h.Vector()
    h_hd = h.Vector()
    n_k = h.Vector()
    tau_m = h.Vector()
    tau_h = h.Vector()
    tau_n = h.Vector()
    
    m_na.record(soma(0.5)._ref_minf_na1)
    h_hd.record(soma(0.5)._ref_linf_hd)
    n_k.record(soma(0.5)._ref_ninf_k1)
    tau_m.record(soma(0.5)._ref_mtau_na1)
    tau_h.record(soma(0.5)._ref_taul_hd)
    tau_n.record(soma(0.5)._ref_taun_k1)

    soma.diam = diam
    soma.cm = cm*1.4884e-4/6.2832e-4
    soma.gbar_na1 = gna*1e-3
    soma.gbar_k1 = gk*1e-3
    soma.gl_hh = gl*1e-6
    soma.ghdbar_hd = gh*1e-4
    soma.el_hh = el
    soma.mhalf_na1 = mhalf
    soma.vhalfl_hd = hhalf
    soma.mk_na1 = mk
    soma.kl_hd = hk
    soma.vhalfn_k1 = nhalf
    soma.kn_k1 = kn
    soma.multiply1_na1 = multiply1
    soma.multiply2_na1 = multiply2
    soma.multiply_k1 = multiply
    soma.seg_value1_k1 = seg1
    soma.seg_value2_na1 = seg2
    soma.seg_value3_hd = seg3
        
    Source = h.IClamp(soma(0.5))
    Source.delay = dur[0]
    Source.dur = dur[1]-dur[0]
    Source.amp = amp
    
    h.tstop = tstop
    h.v_init = el
    
    nc = h.NetCon(soma(0.5)._ref_v,None,sec=soma)
    nc.threshold = 0
    spvec = h.Vector()
    nc.record(spvec)
    if Source.amp < 0:
        h.run()
        print('number of spikes:',len(spvec))
        
        R_in_1 = 1/(soma.gl_hh*1000)
        tau_1 = soma.cm*R_in_1
        V_rest_1 = v0_vec[int(tstop)-20]
        
        R_in_2 = Passive[1]
        tau_2 = Passive[0]
        V_rest_2 = Passive[2]
    
        df1 = pd.DataFrame([[tau_1],[V_rest_1],[R_in_1],[tau_2],[V_rest_2],[R_in_2]],
        columns=['value  '],
        index = ['tau_seg  ', 'Vrest_seg  ', 'Rin_seg  ','tau_ori  ', 'Vrest_ori  ', 'Rin_ori  '])
        print (df1)
        plt.figure(figsize=(10,6))
        plt.plot(t_vec, v0_vec,'b')
        plt.xlim(0, tstop)
        plt.ylabel('mV')
    
    frequency =["all"]
    amplitude =["all"]  
    # FIR Curve

    freq1 = []
    I1 = []
    freq2 = []
    I2 = []
    if (Source.amp > 0):
        for Source.amp in np.arange(amp,amp+1,0.1):
            h.run()
            freq1.append(len(spvec)*1000/Source.dur)
            I1.append(Source.amp)
        plt.figure(figsize=(16,14))
        plt.subplot(4,1,1)
        plt.plot(t_vec, v0_vec,'b')
        plt.xlim(0, tstop)
        plt.ylabel('mV')
        plt.subplot(4,1,2)
        plt.plot(amplitude,frequency,'bo')
        plt.plot(I1,freq1,'yo')
        #plt.legend([soma.flag_k1,1-soma.flag_k1])
        plt.xlabel('Injected current (nA)')
        plt.ylabel('frequency') 
        plt.subplot(4,1,3)
        plt.plot(v0_vec, m_na,'r.')
        plt.plot(v0_vec, h_hd,'b.')
        plt.plot(v0_vec, n_k, 'g.')
        #plt.xlim(0, tstop)
        plt.xlabel('voltage (mV)')
        plt.ylabel('Probability')
        plt.legend(['minf','hinf','ninf'])
        plt.subplot(4,1,4)
        plt.plot(v0_vec, tau_m,'r.')
        plt.plot(v0_vec, tau_h,'b.')
        plt.plot(v0_vec, tau_n, 'g.')
        plt.xlabel('voltage (mV)')
        plt.ylabel('tau')
        plt.legend(['minf','hinf','ninf'])
    image = BytesIO()
    #plt.show()
    plt.savefig(image, format='png')
    ret = base64.b64encode(image.getvalue())
    return str(ret)


#Just a testing platform
def return_params(params):
    return params

