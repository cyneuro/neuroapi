import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import shutil
import os

def load_neuron():
    from neuron import h
    h.load_file('stdrun.hoc')

def build_cell(diam,cm,el,gl,gna,gh,gk,tstop,dur,amp,mhalf,hhalf,mk,hk,nhalf,kn,multiply,multiply1,multiply2,seg1,seg2,seg3):
    load_neuron()
    
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



#Just a testing platform
def return_params(params):
    return params

