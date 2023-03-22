import fuzzylab as fl

import fuzzy
from fuzzy import *
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 1, 0.1)
FMem_P = fuzzy.gaussmf(x, 0)
#A2 = fuzzy.trimf(x, [20, 30, 40])
#B1 = fuzzy.trimf(x, [40, 50, 60])
#B2 = fuzzy.trimf(x, [50, 60, 70])
#Ap = fuzzy.sigmf(x, [0.5, 50])

#print(float(fl.gaussmf(2, [10, 30])))

#plt.plot(x,A)
#plt.title('trimf, P = [3, 6, 8]')
#plt.xlabel('x')
#plt.ylabel('Degree of Membership')
#plt.ylim([-0.05, 1.05])
#plt.show()

Ac = fuzzy.cut(50, A1)
print(Ac)

#merge = fuzzy.union([A, B])
#defuzzA = fuzzy.defuzz(x, merge, 'centroid')
#print(defuzzA)


fig, ax = plt.subplots(2, 2, sharey = True)
ax[0, 0].plot(x, A1)
ax[0, 1].plot(x, B1, color = 'tab:orange')
ax[1, 0].plot(x, A1)
ax[1, 1].plot(x, Ap, color = 'tab:orange')
plt.show()