# -*- coding: utf-8 -*-

import math as mt
from scipy import integrate
#x2 = lambda x: x**2
#erf =  lambda x: 2.*mt.exp(-x**2) / mt.sqrt(mt.pi)
#print(integrate.quad(erf, 0, 1))
I = lambda x: mt.log(x)/(1.-x)
I1 = lambda x: mt.log(mt.sin(x))
#print(integrate.quad(I1, 0, mt.pi))


import numpy as np
import scipy
#print mt.ceil(np.e**(1./np.pi))
print 'mt.ceil(scipy.special.zetac(1.5)) = ', mt.ceil(scipy.special.zetac(1.5))
print 'mt.ceil(scipy.special.zetac(2.)) = ', mt.ceil(scipy.special.zetac(2.))



























