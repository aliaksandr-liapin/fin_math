import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['font.family'] = 'serif'

# Option strike
K = 8000

# Graphical output
S = np.linspace(7000, 9000, 100)
h = np.maximum(S - K, 0)

plt.figure()
plt.plot(S, h, lw=2.5)
plt.xlabel('index level $S_t$ at maturity')
plt.ylabel('inner value of call option')
plt.grid(True)
plt.show()