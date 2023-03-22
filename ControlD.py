import fuzzy
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-1, 1, 0.01)

FMem_P_G = fuzzy.gaussmf(x, [0.1,0])
FMem_P_L = fuzzy.sigmf(x, [30, 0.3])
FMem_P_H = fuzzy.sigmf(x, [-30, -0.3])

FMem_I_G = fuzzy.gaussmf(x, [0.1,0])
FMem_I_L = fuzzy.sigmf(x, [30, 0.3])
FMem_I_H = fuzzy.sigmf(x, [-30, -0.3])

FMem_D_G = fuzzy.gaussmf(x, [0.1,0])
FMem_D_L = fuzzy.sigmf(x, [30, 0.3])
FMem_D_H = fuzzy.sigmf(x, [-30, -0.3])


fig, ax = plt.subplots(3, 4, sharey = True)
ax[0, 0].plot(x, FMem_P_G)
ax[0, 1].plot(x, FMem_P_L)
ax[0, 2].plot(x, FMem_P_H)
ax[0, 3].plot(x, FMem_P_G)
ax[0, 3].plot(x, FMem_P_L)
ax[0, 3].plot(x, FMem_P_H)

ax[1, 0].plot(x, FMem_I_G)
ax[1, 1].plot(x, FMem_I_L)
ax[1, 2].plot(x, FMem_I_H)
ax[1, 3].plot(x, FMem_I_G)
ax[1, 3].plot(x, FMem_I_L)
ax[1, 3].plot(x, FMem_I_H)

ax[2, 0].plot(x, FMem_D_G)
ax[2, 1].plot(x, FMem_D_L)
ax[2, 2].plot(x, FMem_D_H)
ax[2, 3].plot(x, FMem_D_G)
ax[2, 3].plot(x, FMem_D_L)
ax[2, 3].plot(x, FMem_D_H)

plt.show()