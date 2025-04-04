# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 02:20:56 2023

@author: User
"""
import matplotlib.pyplot as plt
import numpy as np
from statistics import mean
#Memplot graf pengiraan
y1 = 0.0017838478088378906
y2 = 0.005789279937744141
y3 = 0.003760814666748047
y4 = 0.008973360061645508
y5 = 0.008826732635498047
y6 = 0.003190279006958008
y7 = 0.004482269287109375
y8 = 0.005080223083496094
y9 = 0.002390146255493164
y10= 0.0026700496673583984
y11 = 0.006521940231323242
y12 = 0.0019674301147460938
y13 = 0.005731821060180664
y14 = 0.00811624526977539
y15 = 0.00783681869506836
y16 = 0.0009965896606445312
y17 = 0.0064334869384765625
y18 = 0.004723548889160156
y19 = 0.0028586387634277344
y20 = 0.004708290100097656
y1value = np.array([y1,y2, y3, y4, y5])
y2value = np.array([y6, y7, y8, y9, y10])
y3value = np.array([y11, y12, y13, y14, y15])
y4value = np.array([y16, y17, y18, y19, y20])

yvalue = np.concatenate((y1value, y2value, y3value, y4value))
xvalue = np.array([1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

ymean = mean(yvalue)

plt.plot(xvalue,yvalue)

plt.xlabel('')
plt.ylabel('Masa pengiraan (saat)')

plt.title('Masa pengiraan bagi Skema Tandatangan Satu Kali Lamport-Diffie (LDOTSS)')
plt.show()

print(xvalue)
print(yvalue)
print(ymean)