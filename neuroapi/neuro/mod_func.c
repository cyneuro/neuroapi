#include <stdio.h>
#include "hocdec.h"
#define IMPORT extern __declspec(dllimport)
IMPORT int nrnmpi_myid, nrn_nobanner_;

extern void _h_reg();
extern void _k1_reg();
extern void _na1_reg();

modl_reg(){
	//nrn_mswindll_stdio(stdin, stdout, stderr);
    if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
	fprintf(stderr, "Additional mechanisms from files\n");

fprintf(stderr," h.mod");
fprintf(stderr," k1.mod");
fprintf(stderr," na1.mod");
fprintf(stderr, "\n");
    }
_h_reg();
_k1_reg();
_na1_reg();
}
