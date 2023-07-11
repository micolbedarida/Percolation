from percolation import single_run, multiple_runs_fixed_radius, multiple_runs_fixed_density
from sigmoid_curve_fit import sigmoid, fit_sigmoid
import matplotlib.pyplot as plt
import os.path

filenames = [
    'output_2016-01-09-03-41-23.py',
    'output_2016-01-08-07-22-21.py',
    'output_2016-01-08-06-56-17.py',
    'output_2016-01-08-06-47-21.py',
    'output_2016-01-08-06-43-28.py',
    'output_2016-01-08-06-41-30.py',
    'output_2016-01-08-06-40-23.py',
    'output_2016-01-08-06-39-41.py',
]

radii = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08]

colors = ['#FF0000', '#FF7F00', '#FFFF00', '#00FF00', '#006400', '#00b8e6', '#0000FF', '#8b00FF']

plt.figure()

curves = []
for filename, radius, color in zip(filenames, radii, colors):
    x, y, a, b = fit_sigmoid(os.path.join('Output', filename))
    po = (a, b)
    curves.append({'x': x, 'y': y, 'a': a, 'b': b, 'po': po, 'rad': radius})
    plt.plot(x, y, color = color, marker = 'o', linestyle = 'None')
    plt.plot(x, sigmoid(x, *po), color = color,
            label = "rad = %0.2f" % (radius))

# Compute and plot center (i.e. coord average) of intersection points between
#  pairs of sigmoids
sx = 0  # Summation of x coords
sy = 0  # Summation of y coords
c = 0   # Count of intersection points
for curve1 in curves:
    for curve2 in curves:
        if curve1 != curve2:
            # Compute x of intersection point between two sigmoids
            #  exp(a - b * x) must be the same for both curves, thus
            #  x = delta a / delta b
            x0 = (curve1['a'] - curve2['a']) / (curve1['b'] - curve2['b'])
            y0 = sigmoid(x0, curve1['a'], curve1['b'])
            sx += x0
            sy += y0
            c += 1
cx, cy = sx / c, sy / c     # Center coordinates are averages of coords of intersection points
print 'Center of sigmoids intersections is (%0.4f, %0.4f)' % (cx, cy)
plt.plot(cx, cy, "Dk")

font = 'Helvetica Neue Thin'
plt.title("Threshold curves for different radii", family = font, fontsize = 18)
plt.grid(True)
plt.xlabel("density", family = font, fontsize = 14)
plt.ylabel("probability of percolation", family = font, fontsize = 14)
legend = plt.legend(fancybox = True, shadow = True, fontsize = 10, loc = 'upper left')

plt.text(1.55, 0.05, r'$y=\frac{1}{1+e^{a-bx}}$', fontsize = 20)
plt.axis('tight')   # Crop graph to interesting part with data

# Inset axes over the main axes
a = plt.axes([.63, .43, .25, .27], axisbg='#E0E0E0')

for curve, color in zip(curves, colors):
    x, y = curve['x'], curve['y']
    po = curve['po']
    rad = curve['rad']
    plt.plot(x, y, color = color, marker = 'o', linestyle = 'None')
    plt.plot(x, sigmoid(x, *po), color = color, label = "rad = %0.2f" % (rad))

plt.plot(cx, cy, "Dk")
plt.text(cx + 0.007, cy, 'threshold =\n %0.2f' % cx, fontsize = 10)

# Zoomed-in view of intersection area
plt.axis((cx - 0.03, cx + 0.03, cy - 0.03, cy + 0.03))
plt.tick_params(axis='both', labelsize = 9)
plt.title('Detail of intersection area', family = font)

plt.show()
