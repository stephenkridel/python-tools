# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import math as math
import numpy as np

sigX = float(input('Please input the Sigma X stress: '));
sigY = float(input('Please input the Sigma Y stress: '));
tau = float(input('Please input the Tau stress: '));
thetaDeg = np.linspace(0, 360, num=1000);
thetaRad = (math.pi / 360) * thetaDeg;

sigXPrime = [];
sigYPrime = [];
tauPrime = [];

for i in thetaRad: 
    sigXPrime.append(((sigX + sigY) / 2) + ((sigX + sigY) / 2) * math.cos(2 * i) + tau * math.sin(2 * i));
    
    sigYPrime.append(((sigX + sigY) / 2) - ((sigX + sigY) / 2) * math.cos(2 * i) - tau * math.sin(2 * i));
    
    tauPrime.append(-((sigX - sigY) / 2) * math.degrees(math.sin(2 * i)) + tau * math.degrees(math.cos(2 * i)));


sig1 = ((sigX + sigY) / 2) + math.sqrt(((sigX - sigY) / 2)**2 + tau**2);
sig2 = ((sigX + sigY) / 2) - math.sqrt(((sigX - sigY) / 2)**2 + tau**2);
tauMax = math.sqrt(((sigX - sigY) / 2)**2 + tau**2);
thetaPrime = math.atan(tau / ((sigX - sigY) / 2)) / 2;

print('Sigma 1 = ' + str(sig1));
print('Sigma 2 = ' + str(sig2));
print('Tau = ' + str(tauMax));
print('Theta Prime = ' + str(thetaPrime));

plt.plot(thetaDeg, sigXPrime, label='Sigma X Prime')
plt.plot(thetaDeg, sigYPrime, label='Sigma Y Prime')
plt.plot(thetaDeg, tauPrime, label='Tau Prime')

plt.xlabel('Theta (degrees)')
plt.ylabel('Stresses (Pa)')
plt.title('Stress Transformations')
plt.legend()
# plt.savefig('StressTransform.jpg', dpi=1200)
