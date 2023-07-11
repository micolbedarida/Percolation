from percolation import single_run, multiple_runs_fixed_radius, multiple_runs_fixed_density
from sigmoid_curve_fit import fit_sigmoid, sigmoid
from exponential_curve_fit import fit_exp, exponential
import matplotlib.pyplot as plt


'''Instructions: Call one or more of the following functions:'''

'''
single_run(disk_number = 450, radius = 0.03)


results_file = multiple_runs_fixed_radius(iterations = 5, min_density = 0, max_density = 3, density_interval = 0.1, radius = 0.1)
x, y, a, b = fit_sigmoid(results_file)
po = (a, b)

plt.figure()
plt.plot(x, y, 'ko', label = "Original Data")
plt.plot(x, sigmoid(x, *po), 'r-', label = "Fitted Curve")
plt.legend(bbox_to_anchor = (0.35, 1))
plt.title('Curve equation: 1 / (1 + exp(%f - %f * x))' % (a, b))
plt.xlabel('density')
plt.ylabel('fraction of percolation')
plt.show()
'''

results_file = multiple_runs_fixed_density(iterations = 10, min_radius = 0.05, max_radius = 0.5, radius_interval = 0.02, density = 1.3)
x, y, a, b, c, d = fit_exp(results_file)
po = (a, b, c, d)

plt.figure()
plt.plot(x, y, 'ko', label = "Original Data")
plt.axis([0, 0.5, 0, 1])
plt.plot(x, exponential(x, *po), 'r-', label="Fitted Curve")
plt.legend(bbox_to_anchor = (0.35, 0.20))
plt.title('Curve equation: %0.4f + %0.4f * x * e ^ (-%0.4f * x) + %0.4f * x' % tuple(po))
plt.xlabel('radius')
plt.ylabel('fraction of percolation')
plt.show()
