# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 03:40:09 2023

@author: User
"""
import matplotlib.pyplot as plt
import numpy as np
from statistics import mean
#Memplot graf pengiraan
y1 = 0.05159592628479004
y2 = 0.03997802734375
y3 = 0.033324241638183594
y4 = 0.05221152305603027
y5 = 0.04139971733093262
y6 = 0.043730974197387695
y7 = 0.032758474349975586
y8 = 0.04156947135925293
y9 = 0.03619718551635742
y10 = 0.03458070755004883
y11 = 0.033457279205322266
y12 = 0.044150590896606445
y13 = 0.04130959510803223
y14 = 0.05511760711669922
y15 = 0.04426741600036621
y16 = 0.05248212814331055
y17 = 0.03383207321166992
y18 = 0.040581703186035156
y19 = 0.03610849380493164
y20 = 0.04377388954162598
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

plt.title('Masa pengiraan bagi Skema Tandatangan Satu Kali Winternitz (WOTSS)')
plt.show()

print(xvalue)
print(yvalue)
print(ymean)
