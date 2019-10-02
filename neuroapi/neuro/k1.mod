TITLE K-DR channel
: from Klee Ficker and Heinemann
: modified to account for Dax et al.
: M.Migliore 1997

UNITS {
	(mA) = (milliamp)
	(mV) = (millivolt)

}

PARAMETER {

	v (mV)
        ek (mV)		: must be explicitely def. in hoc
	celsius		(degC)
	gbar=.003 (mho/cm2)
        vhalfn = -15: 13 : -25  : -20  (mV)
        a0n=0.02      (/ms)
        zetan=-3    (1)
        gmn=0.7  (1)
	nmax=2  (1)
	qt=1
    	kn = 11
	flag = 0
	multiply = 1
	seg_value1 = -61
	: cut_off = vhalfn-3*kn
}


NEURON {
	SUFFIX k1
	USEION k READ ek WRITE ik
        RANGE gkdr, i, gbar
	RANGE ninf,taun,vhalfn,kn,flag,multiply,seg_value1
}

STATE {
	n
}

ASSIGNED {
	ik (mA/cm2)
	i  (mA/cm2)
        ninf
        gkdr
        taun
	:an
}

BREAKPOINT {
	SOLVE states METHOD cnexp
	gkdr = gbar*n
	ik = gkdr*(v-ek)
	i = ik

}

INITIAL {
	rates(v)
	n=ninf
}


FUNCTION alpn(v(mV),vhalfn) {
  alpn = exp(1.e-3*(-3)*(v-vhalfn)*9.648e4/(8.315*(273.16+celsius)))
  :alpn = 0.01*(10-v)/(exp((10-v)/10)-1) 
}

FUNCTION betn(v(mV),vhalfn) {
  betn = exp(1.e-3*(-3)*(0.7)*(v-vhalfn)*9.648e4/(8.315*(273.16+celsius))) 
  :betn = 0.125*exp(-v/80)
}

DERIVATIVE states {     : exact when v held constant; integrates over dt step
        rates(v)
        n' = (ninf - n)/taun
}
PROCEDURE rates(v (mV)) { :callable from hoc
        LOCAL a
        a = alpn(v,vhalfn)
	if (flag == 0){
		if (v < seg_value1 ) {              ::::::::::::::::::::   -55
		ninf =0
		} 
		else{ninf = 1 / ( 1 + exp( ( vhalfn - v ) / kn) )}
	}else{ninf = 1 / ( 1 + exp( ( vhalfn - v ) / kn) )}
		
		taun = (betn(v,vhalfn)/(qt*(0.02)*(1+a)))*multiply
		:taun = 1/(betn(v,vhalfn)+a)

	if (taun<nmax) {taun=nmax}
}