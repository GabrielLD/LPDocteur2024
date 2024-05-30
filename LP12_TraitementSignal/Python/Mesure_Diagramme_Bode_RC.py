#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 11:36:20 2024

@author: gld
"""
#C = 10nF
# R = 10kOhm
import numpy as np
import matplotlib.pyplot as plt
f = [10,20, 30,50,100,200,400,600,800,1000,1200,1400,1800,2500,3000,4000,6000, 9000] #Hz
s = np.array([1,1,1,1,1.0,996e-3,971e-3,936e-3,892e-3,843e-3,794e-3,745e-3,656e-3,570e-3, 510e-3,410e-3,310e-3,230e-3]) #V
e = 1 #V

fig= plt.figure()
ax=fig.add_subplot(1,1,1)
liine, =ax.plot(f,s/e,'*')
ax.set_xscale('log')
plt.show()
