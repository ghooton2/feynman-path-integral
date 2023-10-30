import numpy as np
import vegas
import math
import matplotlib.pyplot as plt

#N: spatial points
#T: complex time interval
#Epsilon: 'time' step

#https://vegas.readthedocs.io/en/latest/vegas.html
#nitn: no. of iterations
#neval: Approximate number of integrand evaluations in each iteration

def potentialSub(x):
    return (1/2)*(x**2)

def S_Sum(x,a,m,N):
    latSum = 0
    latSum += (m/(2*a)) * ((x[0]-x_0)**2) + a*potentialSub(x_0)
    for j in range(0,N-2):
        latSum += (m/(2*a)) * ((x[j+1]-x[j])**2) + a*potentialSub(x[j])
    latSum += (m/(2*a)) * ((x_0-x[-1])**2) + a*potentialSub(x[-1])
    return latSum

def G_integral(x):
    N = 7
    T = 4
    a = T/N
    m=1
    exp_power = S_Sum(x,a,m,N)
    const = ((m/(2*np.pi*a))**(N/2))
    return (const*(math.exp(-exp_power)))

def G_integral_norm(x):
    N = 7
    T = 4
    a = T/N
    m=1
    latSum = 0
    for j in range(0,N-1):
        latSum += (m/(2*a)) * ((x[j+1]-x[j])**2) + a*potentialSub(x[j])
    latSum += (m/(2*a)) * ((x[0]-x[-1])**2) + a*potentialSub(x[-1])

    exp_power = latSum
    const = ((m/(2*np.pi*a))**(N/2))
    return (const*(math.exp(-exp_power)))

def actual(x, T):
    #E0 = 1/2
    xE0top = math.exp((-(x**2))/2)
    xE0bottom = (np.pi**(1/4))
    xE0 = xE0top/xE0bottom
    return xE0**2#*(math.exp(-E0*T)))

def compute_integral(N):
    limits = [[-5, 5]]*(N-1)
    integ = vegas.Integrator(limits)
    result = integ(G_integral, nitn=80, neval=20000)
    return result.mean

def compute_integral_norm(N):
    limits = [[-5, 5]]*(N)
    integ = vegas.Integrator(limits)
    result = integ(G_integral_norm, nitn=80, neval=30000)
    return result.mean

T = 4
E0 = 1/2

x_values = []
act_y = []

prop_y = []
N = 7
a = T/N
m=1
area = 0

for z in range(0,39):
    x_0 = z*0.05
    x_values += [x_0]
    act_y += [actual(x_0, 4)]
    temp = compute_integral(N)
    print(temp)
    prop_y += [temp]


area = compute_integral_norm(N)

for test in range(0, len(prop_y)):
    prop_y[test] = prop_y[test]*(1/area)


plt.plot(x_values,act_y, label='Exact')
plt.scatter(x_values,prop_y, label='Path Integral')
plt.legend()
plt.show()
