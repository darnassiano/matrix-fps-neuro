import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


excel=pd.ExcelFile("raster.xlsx")
neuron_matrix=excel.parse("Hoja1",header=None).as_matrix()

N,F=neuron_matrix.shape  # N -> 90, F -> 2160

A=np.zeros((N,N))

S=np.zeros(N)

# Generando la matriz adyancente con base a los fotogramas
for i in range(F-1):
    print("Recuperando fotograma: ",i)            # Procesamiento por columna
    photogram=neuron_matrix[:,i]
    for j in range(N):
        #print("el valor de neurona",j, " es: " ,photogram[j])
        if photogram[j] == 1:
            for h in range(j+1,N):
                if photogram[h] == 1:
                    A[j,h] = 1
                    A[h,j] = 1
                else:
                    pass


# Generando un array de sumas acumulativas por fila (Neurona)
for i in range(N):
    S[i]=A[i,:].sum()


x=[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70]

y,bins,patches=plt.hist(S,x,histtype="stepfilled",color='lightgray')
plt.plot(x[:-1],y)
plt.title("Neuron Activation Histogram")
plt.xlabel("Grades")
plt.ylabel("Frequency")
plt.show()
