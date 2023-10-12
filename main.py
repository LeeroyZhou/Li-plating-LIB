# Li Plating in LIB Anode
# Vaviables: xi: phase-field    zeta: concentration of Li+    phi: electric potential

# ------ Initialize ------
from parameters import *



# ------- Evolve ------
step = 0
cur = 0
nxt = 1
while step < N_step:
    d_xi_t = 123 #...
    xi[nxt] = xi[cur] + d_xi_t
    zeta[nxt] = zeta[cur] + ... + d_xi_t * C_ms / C_0
    phi[nxt] = ...

    step += 1
    (cur, nxt) = (nxt, cur)

# ------ output ------
import matplotlib.pyplot as plt
fig = plt.plot()

