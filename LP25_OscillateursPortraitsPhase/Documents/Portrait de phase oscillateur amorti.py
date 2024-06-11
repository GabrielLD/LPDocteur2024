#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 19:36:52 2022

@author: gabriel
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
# format vectoriel par défaut des images
from IPython.display import set_matplotlib_formats
import matplotlib as mpl
mpl.rcParams.update(mpl.rcParamsDefault)


# Paramètres généraux de pyplot
set_matplotlib_formats('svg')
SMALL_SIZE = 8
MEDIUM_SIZE = 10
BIGGER_SIZE = 12

# système d'équations:
#    theta'(t) = omega(t)
#    omega'(t) = -b*omega(t) - c*sin(theta(t))


def pend(y, t, b, c):
    theta, omega = y
    dydt = [omega,- c*np.sin(theta) -b*omega ]
    return dydt

y0 = [np.pi - 1, 0.0]
t = np.linspace(0, 10 * np.pi, 2000)

omega0 = 1
Q=10
b = omega0/Q #0.25 #omega0/Q
c = omega0**2 #3.5  #omega0^2

theta_init = np.linspace(0, np.pi, 20)

fig = plt.figure(figsize=(13, 6))
plt.subplots_adjust(left   = 0.1,
                    bottom = 0.1,
                    right  = 0.9,
                    top    = 0.9,
                    wspace = 0.4,
                    hspace = 0.5)
gs = fig.add_gridspec(ncols=2, nrows=1)
ax_t = fig.add_subplot(gs[0,0])
ax_p = fig.add_subplot(gs[0,1])
#for theta_0 in theta_init:
#    theta, theta_dot = odeint(simple_pendulum, (theta_0, 0), t).T
sol = odeint(pend, y0, t, args=(b, c))



ax_t.plot(t, sol[:,0],'b-',label=u"$\\theta$")
ax_t.plot(t, sol[:,1],'r-',label=u"$\dot{\\theta}$")

ax_t.set_xlabel(u'$t$ (s)', fontsize=26)
ax_t.set_ylabel(u'$\\theta, \dot{\\theta}$', fontsize=26)
ax_t.legend(bbox_to_anchor=(.99, .99),loc='upper right', borderaxespad=0.)

ax_t.set_xlim(0, 10*np.pi)
#ax_t.set_ylim(-np.pi, np.pi)
ax_t.title.set_text('Trajectoire')


ax_p.plot(sol[:,0], sol[:,1])

ax_p.set_xlabel(u'$\\theta$', fontsize=26)
ax_p.set_ylabel(u'$\dot{\\theta}$', fontsize=26)
ax_p.axis('equal')
ax_p.set_xlim(-np.pi, np.pi)
#ax_p.set_ylim(-2, 2)
ax_p.title.set_text('diagramme de phase')

plt.show()

m=100E-3
l = 9.81
g = 9.81



Ec = 0.5*m*(l*sol[:,0])**2
Ep = m*g*l*(1-np.cos(sol[:,1]))
Em = Ec+Ep
plt.figure()
plt.plot(t,Em, label='Energie Mecanique')
plt.plot(t,Ec, label='Energie cinétique')
plt.plot(t,Ep, label='Energie potentielle')
plt.xlabel('temps')
plt.ylabel('E (J)')
plt.legend()
plt.show()