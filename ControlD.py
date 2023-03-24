#Librerias
import matplotlib.pyplot as plt
import fuzzy
import numpy as np
import skfuzzy as fuzz

# Universos
x = np.arange(-1, 1, 0.01)
x_out = np.arange(0, 2, 0.01)

# Entradas
input_E_P = 0.2
input_E_I = -0.9
input_E_D = 0.7

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

############################################ Fuzificacion ##################################################

val_P_Z = fuzz.interp_membership(x, FMem_P_Z, input_E_P)
val_P_N = fuzz.interp_membership(x, FMem_P_N, input_E_P)
val_P_P = fuzz.interp_membership(x, FMem_P_P, input_E_P)
print("Valores de pertenencia del error proporcional")
print("Valor de pertenencia Z=", val_P_Z, "Valor de pertenencia N=", val_P_N, "Valor de pertencia P=", val_P_P)

val_I_Z = fuzz.interp_membership(x, FMem_I_Z, input_E_I)
val_I_N = fuzz.interp_membership(x, FMem_I_N, input_E_I)
val_I_P = fuzz.interp_membership(x, FMem_I_P, input_E_I)
print("Valores de pertenencia del error integral")
print("Valor de pertenencia Z=", val_I_Z, "Valor de pertenencia N=", val_I_N, "Valor de pertencia P=", val_I_P)

val_D_Z = fuzz.interp_membership(x, FMem_D_Z, input_E_D)
val_D_N = fuzz.interp_membership(x, FMem_D_N, input_E_D)
val_D_P = fuzz.interp_membership(x, FMem_D_P, input_E_D)
print("Valores de pertenencia del error derivativo")
print("Valor de pertenencia Z=", val_D_Z, "Valor de pertenencia N=", val_D_N, "Valor de pertencia P=", val_D_P)

############################################ Reglas #################################################

# 1 Si el error(P) es N, y error(D) es N, y error(I) es N, entonces CONTROL es N
rule1 = np.fmin(np.fmin(np.fmin(val_P_N, val_D_N), val_I_N), Out_N)
# 2 Si el error(P) es N, y error(D) es N, y error(I) es Z, entonces CONTROL es N
rule2 = np.fmin(np.fmin(np.fmin(val_P_N, val_D_N), val_I_Z), Out_N)
# 3 Si el error(P) es N, y error(D) es N, y error(I) es P, entonces CONTROL es N
rule3 = np.fmin(np.fmin(np.fmin(val_P_N, val_D_N), val_I_P), Out_N)
# 4 Si el error(P) es N, y error(D) es Z, y error(I) es N, entonces CONTROL es N
rule4 = np.fmin(np.fmin(np.fmin(val_P_N, val_D_Z), val_I_N), Out_N)
# 5 Si el error(P) es N, y error(D) es Z, y error(I) es Z, entonces CONTROL es N
rule5 = np.fmin(np.fmin(np.fmin(val_P_N, val_D_Z), val_I_Z), Out_N)
# 6 Si el error(P) es N, y error(D) es Z, y error(I) es P, entonces CONTROL es N
rule6 = np.fmin(np.fmin(np.fmin(val_P_N, val_D_Z), val_I_P), Out_N)
# 7 Si el error(P) es N, y error(D) es P, y error(I) es N, entonces CONTROL es N
rule7 = np.fmin(np.fmin(np.fmin(val_P_N, val_D_P), val_I_N), Out_N)
# 8 Si el error(P) es N, y error(D) es P, y error(I) es Z, entonces CONTROL es N
rule8 = np.fmin(np.fmin(np.fmin(val_P_N, val_D_P), val_I_Z), Out_N)
# 9 Si el error(P) es N, y error(D) es P, y error(I) es P, entonces CONTROL es N
rule9 = np.fmin(np.fmin(np.fmin(val_P_N, val_D_P), val_I_P), Out_N)

# 10 Si el error(P) es Z, y error(D) es N, y error(I) es N, entonces CONTROL es Z
rule10 = np.fmin(np.fmin(np.fmin(val_P_Z, val_D_N), val_I_N), Out_Z)
# 11 Si el error(P) es Z, y error(D) es N, y error(I) es Z, entonces CONTROL es Z
rule11 = np.fmin(np.fmin(np.fmin(val_P_Z, val_D_N), val_I_Z), Out_Z)
# 12 Si el error(P) es Z, y error(D) es N, y error(I) es P, entonces CONTROL es Z
rule12 = np.fmin(np.fmin(np.fmin(val_P_Z, val_D_N), val_I_P), Out_Z)
# 13 Si el error(P) es Z, y error(D) es Z, y error(I) es N, entonces CONTROL es Z
rule13 = np.fmin(np.fmin(np.fmin(val_P_Z, val_D_Z), val_I_N), Out_Z)
# 14 Si el error(P) es Z, y error(D) es Z, y error(I) es Z, entonces CONTROL es Z
rule14 = np.fmin(np.fmin(np.fmin(val_P_Z, val_D_Z), val_I_Z), Out_Z)
# 15 Si el error(P) es Z, y error(D) es Z, y error(I) es P, entonces CONTROL es Z
rule15 = np.fmin(np.fmin(np.fmin(val_P_Z, val_D_Z), val_I_P), Out_Z)
# 16 Si el error(P) es Z, y error(D) es P, y error(I) es N, entonces CONTROL es Z
rule16 = np.fmin(np.fmin(np.fmin(val_P_Z, val_D_P), val_I_N), Out_Z)
# 17 Si el error(P) es Z, y error(D) es P, y error(I) es Z, entonces CONTROL es Z
rule17 = np.fmin(np.fmin(np.fmin(val_P_Z, val_D_P), val_I_Z), Out_Z)
# 18 Si el error(P) es Z, y error(D) es P, y error(I) es P, entonces CONTROL es Z
rule18 = np.fmin(np.fmin(np.fmin(val_P_Z, val_D_P), val_I_P), Out_Z)

# 19 Si el error(P) es P, y error(D) es N, y error(I) es N, entonces CONTROL es P
rule19 = np.fmin(np.fmin(np.fmin(val_P_P, val_D_N), val_I_N), Out_P)
# 20 Si el error(P) es P, y error(D) es N, y error(I) es Z, entonces CONTROL es P
rule20 = np.fmin(np.fmin(np.fmin(val_P_P, val_D_N), val_I_Z), Out_P)
# 21 Si el error(P) es P, y error(D) es N, y error(I) es P, entonces CONTROL es P
rule21 = np.fmin(np.fmin(np.fmin(val_P_P, val_D_N), val_I_P), Out_P)
# 22 Si el error(P) es P, y error(D) es Z, y error(I) es N, entonces CONTROL es P
rule22 = np.fmin(np.fmin(np.fmin(val_P_P, val_D_Z), val_I_N), Out_P)
# 23 Si el error(P) es P, y error(D) es Z, y error(I) es Z, entonces CONTROL es P
rule23 = np.fmin(np.fmin(np.fmin(val_P_P, val_D_Z), val_I_Z), Out_P)
# 24 Si el error(P) es P, y error(D) es Z, y error(I) es P, entonces CONTROL es P
rule24 = np.fmin(np.fmin(np.fmin(val_P_P, val_D_Z), val_I_P), Out_P)
# 25 Si el error(P) es P, y error(D) es P, y error(I) es N, entonces CONTROL es P
rule25 = np.fmin(np.fmin(np.fmin(val_P_P, val_D_P), val_I_N), Out_P)
# 26 Si el error(P) es P, y error(D) es P, y error(I) es Z, entonces CONTROL es P
rule26 = np.fmin(np.fmin(np.fmin(val_P_P, val_D_P), val_I_Z), Out_P)
# 27 Si el error(P) es P, y error(D) es P, y error(I) es P, entonces CONTROL es P
rule27 = np.fmin(np.fmin(np.fmin(val_P_P, val_D_P), val_I_P), Out_P)

#print(rule1)
############################################ Prueba ################################################

Out_KZ = np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(rule10,rule11),rule12),rule13),rule14),rule15),rule16),rule17),rule18)
Out_KN= np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(rule1,rule2),rule3),rule4),rule5),rule6),rule7),rule8),rule9)
Out_KP = np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(rule19,rule20),rule21),rule22),rule23),rule24),rule25),rule26),rule27)

# cut_P_Z = fuzzy.cut(val_P_Z, FMem_P_Z)
# cut_P_N = fuzzy.cut(val_P_N, FMem_P_N)
# cut_P_P = fuzzy.cut(val_P_P, FMem_P_P)

# cut_I_Z = fuzzy.cut(val_I_Z, FMem_P_Z)
# cut_I_N = fuzzy.cut(val_I_N, FMem_P_N)
# cut_I_P = fuzzy.cut(val_I_P, FMem_P_P)

# cut_D_Z = fuzzy.cut(val_D_Z, FMem_P_Z)
# cut_D_N = fuzzy.cut(val_D_N, FMem_P_N)
# cut_D_P = fuzzy.cut(val_D_P, FMem_P_P)

########################################## Defuzificacion #############################################

out = np.fmax(np.fmax(Out_KN, Out_KZ), Out_KP)
defuzzified  = fuzz.defuzz(x_out, out, 'centroid')
print(defuzzified)

######################################### Funciones ################################################
def gaussmf(x, param):
    #param = [sig, x0]
    # sig > 0
    sig = param[0]
    x0 = param[1]
    if (sig > 0):
        if (type(x) is int) or (type(x) is float) or (type(x) is np.float64):     
            m = np.exp(-0.5*((x - x0)/sig)**2)
        else: 
            m = np.zeros(x.size)
            for i in range(x.size):
                m[i] = np.exp(-0.5*((x[i] - x0)/sig)**2)
        return m
    else:
        return -1

def defuzz(y, mf, option):
    if option == 'centroid':
        num = 0
        den = 0
        for i in range(y.size):
            num = num + y[i]*mf[i]
            den = den + mf[i]
        y0 = num/den
        return y0
    
def sigmf(x, param):
    # param = [a, x0]
    a = param[0]
    x0 = param[1]
    if (type(x) is int) or (type(x) is float) or (type(x) is np.float64):    
        m = 1/(1+np.exp(-a*(x - x0)))
    else: 
        m = np.zeros(x.size)
        for i in range(x.size):
            m[i] = 1/(1+np.exp(-a*(x[i] - x0)))
    return m
########################################### Graficas ###############################################
fig, ax = plt.subplots(3, 4, sharey = True)
fig2, ax2 = plt.subplots(1, 4, sharey = True)
fig3, ax3 = plt.subplots(1, 3, sharey = True)
fig4, ax4 = plt.subplots(1, 4, sharey = True)

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

ax3[0].plot(x, Out_KZ)
ax3[1].plot(x, Out_KN)
ax3[2].plot(x, Out_KP)

# ax4[0].plot(x, cut_P_Z)
# ax4[1].plot(x, cut_P_N)
# ax4[2].plot(x, cut_P_P)
# ax4[3].plot(x, cut_P_Z)
# ax4[3].plot(x, cut_P_N)
# ax4[3].plot(x, cut_P_P)


# ax4.fill_between(y_risk, risk0, out_not, facecolor = 'r', alpha = 0.7)
# ax4.plot(y_risk, risk_not, 'r', linestyle = '--')
# ax4.fill_between(y_risk, risk0, out_little, facecolor = 'g', alpha = 0.7)
# ax4.plot(y_risk, risk_little, 'g', linestyle = '--')
# ax4.fill_between(y_risk, risk0, out_mid, facecolor = 'b', alpha = 0.7)
# ax4.plot(y_risk, risk_mid, 'b', linestyle = '--')
# ax4.fill_between(y_risk, risk0, out_high, facecolor = 'y', alpha = 0.7)
# ax4.plot(y_risk, risk_high, 'y', linestyle = '--')
# ax4.fill_between(y_risk, risk0, out_veryHigh, facecolor = 'm', alpha = 0.7)
# ax4.plot(y_risk, risk_veryHigh, 'm', linestyle = '--')
# ax4.set_title('Out of the Risk')

plt.show()

