# Sigmoid curve fit for multiple_runs_fixed_radius
# Code adapted from first year Imperial online Python manual available on Blackboard
# and from http://stackoverflow.com/questions/3433486/how-to-do-exponential-and-logarithmic-curve-fitting-in-python-i-found-only-poly

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os.path


def sigmoid(x, a, b):
   return 1 / (1 + np.exp(a - b * x))


def fit_sigmoid(output_file):
    simulation_results = {}
    execfile(output_file, simulation_results) # puts contents of output_file into dictionary simulation_results
                    #from: http://stackoverflow.com/questions/18631014/setting-function-variables-with-execfile
    x = np.array(simulation_results['densities'])
    y = np.array(simulation_results['percolation_probability'])

    initial_guess=[1.0, 1.0]
    po, po_cov = curve_fit(sigmoid, x, y, initial_guess)

    #Standard deviational errors (a+- first number and b+- second number)
    po_err = np.sqrt(np.diag(po_cov))
    print po_err

    a, b = tuple(po)

    return x, y, a, b
