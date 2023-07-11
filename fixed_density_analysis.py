import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os.path
from exponential_curve_fit import exponential, fit_exp


x1, y1, a1, b1, c1, d1 = fit_exp('Output/output_2016-01-08-15-29-38.py')
po1 = (a1, b1, c1, d1)
print b1 + d1

x2, y2, a2, b2, c2, d2 = fit_exp('Output/output_2016-01-08-15-59-41.py')
po2 = (a2, b2, c2, d2)
print b2 + d2

x3, y3, a3, b3, c3, d3 = fit_exp('Output/output_2016-01-08-16-34-13.py')
po3 = (a3, b3, c3, d3)
print b3 + d3

x4, y4, a4, b4, c4, d4 = fit_exp('Output/output_2016-01-08-17-14-30.py')
po4 = (a4, b4, c4, d4)
print b4 + d4

x5, y5, a5, b5, c5, d5 = fit_exp('Output/output_2016-01-08-18-01-04.py')
po5 = (a5, b5, c5, d5)
print b5 + d5

x6, y6, a6, b6, c6, d6 = fit_exp('Output/output_2016-01-08-18-54-10.py')
po6 = (a6, b6, c6, d6)
print b6 + d6


plt.figure()


plt.plot(x1, y1, 'ro')
plt.plot(x1, exponential(x1, *po1), 'r-', label = 'density = 1.0, slope at f(0) = %0.3f' % float(b1 + d1))

plt.plot(x2, y2, color = '#CC2EFA', marker = 'o', linestyle = 'None')
plt.plot(x2, exponential(x2, *po2), color = '#CC2EFA', label = 'density = 1.1, slope at f(0) = %0.3f' % float(b2 + d2))

plt.plot(x3, y3, color = '#F88017', marker = 'o', linestyle = 'None')
plt.plot(x3, exponential(x3, *po3), color = '#F88017', label = 'density = 1.2, slope at f(0) = %0.3f' % float(b3 + d3))

plt.plot(x4, y4, 'go')
plt.plot(x4, exponential(x4, *po4), 'g-', label = 'density = 1.3, slope at f(0) = %0.3f' % float(b4 + d4))

plt.plot(x5, y5, 'bo')
plt.plot(x5, exponential(x5, *po5), 'b-', label = 'density = 1.4, slope at f(0) = %0.3f' % float(b5 + d5))

plt.plot(x6, y6, color = '#00BFFF', marker = 'o', linestyle = 'None')
plt.plot(x6, exponential(x6, *po6), color = '#00BFFF', label = 'density = 1.5, slope at f(0) = %0.3f' % float(b6 + d6))

# curve formula
plt.text(0.30, 0.92, r'$f(x)=a+bxe^{-cx}+dx$', fontsize = 14)

font = 'Helvetica Neue Thin'
plt.grid(True)
plt.title("Fraction of percolation for different densities", family = font, fontsize = 20)
plt.xlabel("radius", family = font, fontsize = 16)
plt.ylabel("probability of percolation", family = font, fontsize = 16)
legend = plt.legend(fancybox = True, shadow = True, fontsize = 12, loc = 'bottom right')
for legobj in legend.legendHandles:
    legobj.set_linewidth(2.0) # lines 63 & 64 from: http://stackoverflow.com/
        #questions/9706845/increase-the-linewidth-of-the-legend-lines-in-matplotlib



plt.show()


# Detail between 1.11 and 1.20
x1, y1, a1, b1, c1, d1 = fit_exp('Output/output_2016-01-08-19-54-21.py')
po1 = (a1, b1, c1, d1)
print b1 + d1

x2, y2, a2, b2, c2, d2 = fit_exp('Output/output_2016-01-08-20-29-29.py')
po2 = (a2, b2, c2, d2)
print b2 + d2

x3, y3, a3, b3, c3, d3 = fit_exp('Output/output_2016-01-08-21-05-46.py')
po3 = (a3, b3, c3, d3)
print b3 + d3

x4, y4, a4, b4, c4, d4 = fit_exp('Output/output_2016-01-08-21-41-49.py')
po4 = (a4, b4, c4, d4)
print b4 + d4

x5, y5, a5, b5, c5, d5 = fit_exp('Output/output_2016-01-08-22-19-51.py')
po5 = (a5, b5, c5, d5)
print b5 + d5

x6, y6, a6, b6, c6, d6 = fit_exp('Output/output_2016-01-08-22-58-11.py')
po6 = (a6, b6, c6, d6)
print b6 + d6

x7, y7, a7, b7, c7, d7 = fit_exp('Output/output_2016-01-08-23-36-32.py')
po7 = (a7, b7, c7, d7)
print b7 + d7

x8, y8, a8, b8, c8, d8 = fit_exp('Output/output_2016-01-09-00-16-15.py')
po8 = (a8, b8, c8, d8)
print b8 + d8

x9, y9, a9, b9, c9, d9 = fit_exp('Output/output_2016-01-09-00-55-29.py')
po9 = (a9, b9, c9, d9)
print b9 + d9

x10, y10, a10, b10, c10, d10 = fit_exp('Output/output_2016-01-08-16-34-13.py')
po10 = (a10, b10, c10, d10)
print b10 + d10

'''
x11, y11, a11, b11, c11, d11 = fit_exp('Output/output_2016-01-09-01-35-47.py')
po11 = (a11, b11, c11, d11)
print b11 + d11

x12, y12, a12, b12, c12, d12 = fit_exp('Output/output_2016-01-09-02-17-11.py')
po12 = (a12, b12, c12, d12)
print b12 + d12

x13, y13, a13, b13, c13, d13 = fit_exp('Output/output_2016-01-09-02-59-04.py')
po13 = (a13, b13, c13, d13)
print b13 + d13
'''

plt.figure()

plt.plot(x1, y1, 'ro')
plt.plot(x1, exponential(x1, *po1), 'r-',
        label = 'density = 1.11, slope at f(0) = %0.3f' % float(b1 + d1))

plt.plot(x2, y2, color = '#CC2EFA', marker = 'o', linestyle = 'None')
plt.plot(x2, exponential(x2, *po2), color = '#CC2EFA',
        label = 'density = 1.12, slope at f(0) = %0.3f' % float(b2 + d2))

plt.plot(x3, y3, color = '#F88017', marker = 'o', linestyle = 'None')
plt.plot(x3, exponential(x3, *po3), color = '#F88017',
        label = 'density = 1.13, slope at f(0) = %0.3f' % float(b3 + d3))

plt.plot(x4, y4, color = '#33cc33', marker = 'o', linestyle = 'None')
plt.plot(x4, exponential(x4, *po4), color = '#33cc33',
        label = 'density = 1.14, slope at f(0) = %0.3f' % float(b4 + d4))

plt.plot(x5, y5, 'bo')
plt.plot(x5, exponential(x5, *po5), 'b-',
        label = 'density = 1.15, slope at f(0) = %0.3f' % float(b5 + d5))

plt.plot(x6, y6, color = '#00BFFF', marker = 'o', linestyle = 'None')
plt.plot(x6, exponential(x6, *po6), color = '#00BFFF',
        label = 'density = 1.16, slope at f(0) = %0.3f' % float(b6 + d6))

plt.plot(x7, y7, color = '#5900b3', marker = 'o', linestyle = 'None')
plt.plot(x7, exponential(x7, *po7), color = '#5900b3',
        label = 'density = 1.17, slope at f(0) = %0.3f' % float(b7 + d7))

plt.plot(x8, y8, color = '#ffff00', marker = 'o', linestyle = 'None')
plt.plot(x8, exponential(x8, *po8), color = '#ffff00',
        label = 'density = 1.18, slope at f(0) = %0.3f' % float(b8 + d8))

plt.plot(x9, y9, color = '#ff00ff', marker = 'o', linestyle = 'None')
plt.plot(x9, exponential(x9, *po9), color = '#ff00ff',
        label = 'density = 1.19, slope at f(0) = %0.3f' % float(b9 + d9))

plt.plot(x10, y10, color = '#009999', marker = 'o', linestyle = 'None')
plt.plot(x10, exponential(x10, *po10), color = '#009999',
        label = 'density = 1.20, slope at f(0) = %0.3f' % float(b10 + d10))

'''
plt.plot(x11, y11, 'bo')
plt.plot(x11, exponential(x11, *po11), 'b-', label = 'density = 1.21, slope at f(0) = %0.3f' % b11 + d11)

plt.plot(x12, y12, color = '#00BFFF', marker = 'o', linestyle = 'None')
plt.plot(x12, exponential(x12, *po12), color = '#00BFFF', label = 'density = 1.22, slope at f(0) = %0.3f' % a12)

plt.plot(x13, y13, 'ro')
plt.plot(x13, exponential(x13, *po13), 'r-', label = 'density = 1.23, slope at f(0) = %0.3f' % a13)
'''

# curve formula
plt.text(0.04, 0.76, r'$f(x)=bxe^{-cx}+dx+a$', fontsize = 14)

# change colors and files

plt.title("Fraction of percolation for different densities", family = font, fontsize = 20)
plt.grid(True)
plt.xlabel("radius", family = font, fontsize = 16)
plt.ylabel("probability of percolation", family = font, fontsize = 16)
legend = plt.legend(fancybox = True, shadow = True, fontsize = 12, loc = 'bottom right')
for legobj in legend.legendHandles:
    legobj.set_linewidth(2.0) # lines 63 & 64 from: http://stackoverflow.com/
        #questions/9706845/increase-the-linewidth-of-the-legend-lines-in-matplotlib


plt.show()
