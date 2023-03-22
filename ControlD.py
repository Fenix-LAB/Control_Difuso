#Librerias
import fuzzy
import matplotlib.pyplot as plt
import numpy as np

# Universos
x = np.arange(-1, 1, 0.01)
x_out = np.arange(0, 2, 0.01)

######################################## Funciones de Membresia ##########################################

# Funcion de membresia para la cte Proporcional ERROR
FMem_P_Z = fuzzy.gaussmf(x, [0.1,0])
FMem_P_P = fuzzy.sigmf(x, [30, 0.3])
FMem_P_N = fuzzy.sigmf(x, [-30, -0.3])
 
# Funcion de membresia para la cte Integral ERROR
FMem_I_Z = fuzzy.gaussmf(x, [0.1,0])
FMem_I_P = fuzzy.sigmf(x, [30, 0.3])
FMem_I_N = fuzzy.sigmf(x, [-30, -0.3])


# Funcion de membresia para la cte Derivativa ERROR
FMem_D_Z = fuzzy.gaussmf(x, [0.1,0])
FMem_D_P = fuzzy.sigmf(x, [30, 0.3])
FMem_D_N = fuzzy.sigmf(x, [-30, -0.3])


# Salida
Out_Z = fuzzy.gaussmf(x_out, [0.1,1])
Out_P = fuzzy.sigmf(x_out, [30, 1.3])
Out_N = fuzzy.sigmf(x_out, [-30, 0.7])

############################################ Reglas #################################################

# 1 Si el error(P) es N, y error(D) es N, y error(I) es N, entonces CONTROL es N
# 2 Si el error(P) es N, y error(D) es N, y error(I) es Z, entonces CONTROL es N
# 3 Si el error(P) es N, y error(D) es N, y error(I) es P, entonces CONTROL es N
# 4 Si el error(P) es N, y error(D) es Z, y error(I) es N, entonces CONTROL es N
# 5 Si el error(P) es N, y error(D) es Z, y error(I) es Z, entonces CONTROL es N
# 6 Si el error(P) es N, y error(D) es Z, y error(I) es P, entonces CONTROL es N
# 7 Si el error(P) es N, y error(D) es P, y error(I) es N, entonces CONTROL es N
# 8 Si el error(P) es N, y error(D) es P, y error(I) es Z, entonces CONTROL es N
# 9 Si el error(P) es N, y error(D) es P, y error(I) es P, entonces CONTROL es N

# 10 Si el error(P) es Z, y error(D) es N, y error(I) es N, entonces CONTROL es Z
# 11 Si el error(P) es Z, y error(D) es N, y error(I) es Z, entonces CONTROL es Z
# 12 Si el error(P) es Z, y error(D) es N, y error(I) es P, entonces CONTROL es Z
# 13 Si el error(P) es Z, y error(D) es Z, y error(I) es N, entonces CONTROL es Z
# 14 Si el error(P) es Z, y error(D) es Z, y error(I) es Z, entonces CONTROL es Z
# 15 Si el error(P) es Z, y error(D) es Z, y error(I) es P, entonces CONTROL es Z
# 16 Si el error(P) es Z, y error(D) es P, y error(I) es N, entonces CONTROL es Z
# 17 Si el error(P) es Z, y error(D) es P, y error(I) es Z, entonces CONTROL es Z
# 18 Si el error(P) es Z, y error(D) es P, y error(I) es P, entonces CONTROL es Z

# 19 Si el error(P) es P, y error(D) es N, y error(I) es N, entonces CONTROL es P
# 20 Si el error(P) es P, y error(D) es N, y error(I) es Z, entonces CONTROL es P
# 21 Si el error(P) es P, y error(D) es N, y error(I) es P, entonces CONTROL es P
# 22 Si el error(P) es P, y error(D) es Z, y error(I) es N, entonces CONTROL es P
# 23 Si el error(P) es P, y error(D) es Z, y error(I) es Z, entonces CONTROL es P
# 24 Si el error(P) es P, y error(D) es Z, y error(I) es P, entonces CONTROL es P
# 25 Si el error(P) es P, y error(D) es P, y error(I) es N, entonces CONTROL es P
# 26 Si el error(P) es P, y error(D) es P, y error(I) es Z, entonces CONTROL es P
# 27 Si el error(P) es P, y error(D) es P, y error(I) es P, entonces CONTROL es P





########################################### Graficas ###############################################
fig, ax = plt.subplots(3, 4, sharey = True)
fig2, ax2 = plt.subplots(1, 4, sharey = True)
ax[0, 0].plot(x, FMem_P_Z)
ax[0, 1].plot(x, FMem_P_P)
ax[0, 2].plot(x, FMem_P_N)
ax[0, 3].plot(x, FMem_P_Z)
ax[0, 3].plot(x, FMem_P_P)
ax[0, 3].plot(x, FMem_P_N)

ax[1, 0].plot(x, FMem_I_Z)
ax[1, 1].plot(x, FMem_I_P)
ax[1, 2].plot(x, FMem_I_N)
ax[1, 3].plot(x, FMem_I_Z)
ax[1, 3].plot(x, FMem_I_P)
ax[1, 3].plot(x, FMem_I_N)

ax[2, 0].plot(x, FMem_D_Z)
ax[2, 1].plot(x, FMem_D_P)
ax[2, 2].plot(x, FMem_D_N)
ax[2, 3].plot(x, FMem_D_Z)
ax[2, 3].plot(x, FMem_D_P)
ax[2, 3].plot(x, FMem_D_N)

ax2[0].plot(x_out, Out_Z)
ax2[1].plot(x_out, Out_P)
ax2[2].plot(x_out, Out_N)
ax2[3].plot(x_out, Out_Z)
ax2[3].plot(x_out, Out_P)
ax2[3].plot(x_out, Out_N)

plt.show()