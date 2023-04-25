# Author: Suraj Powar. 
# Date: 04/20/2023
# Image 1 for Algebra Review Paper.

import scipy as sp
import matplotlib.pyplot as plt
import numpy as np
import sympy as smp
from scipy.integrate import quad
from scipy.integrate import cumulative_trapezoid
from scipy.special import factorial
# Increasing the resolution of the plot
plt.figure(dpi=100)

# Activating text rendering by LaTex
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "monospace",
    "font.monospace": 'Computer Modern Typewriter'
})


asn_array = []
for n in range(0,10):
    t = smp.symbols('t', real = True)
    f = smp.exp(-t)* ((t**n - t)/(t - 1))
    inte = (smp.integrate(f, (t, 1, smp.oo)))
    Asn = (smp.exp(1) * inte) - n + 2
    asn_array.append(Asn)
    #print(asn_array)

fact_array = []
for i in range(0, 10):
    fact = factorial(i, exact = True)
    fact_array.append(fact)
    #print(fact_array)

final_array = []
for j in range(0,10):
    final = asn_array[j]/fact_array[j]
    final_array.append(final)


plt.plot(fact_array, final_array)
plt.xlabel('n')
plt.ylabel('fraction of Symmetric groups')
plt.title(r'$Plot \hspace{0.5cm} of \hspace{0.5cm} | A_{S_n}/ S_{n}| \hspace{0.5cm} vs \hspace{0.5cm} n $', fontsize = 25)
plt.show()
