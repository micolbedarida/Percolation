# Sigmoid curve fit for multiple_runs_fixed_radius
# Code adapted from first year Imperial online Python manual available on Blackboard

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os.path


def exponential(x, a, b, c, d):
   return a + b * x * np.exp(-c*x) + d*x


def fit_exp(output_file):
    simulation_results = {}
    execfile(output_file, simulation_results) # puts contents of output_file into dictionary simulation_results
                    #from: http://stackoverflow.com/questions/18631014/setting-function-variables-with-execfile
    x = np.array(simulation_results['radii'])
    y = np.array(simulation_results['percolation_probability'])

    initial_guess=[1.0, 1.0, 1.0, 1.0]
    po, po_cov = curve_fit(exponential, x, y, initial_guess, maxfev = 100000)

    #Standard deviational errors (a+- first number and b+- second number)
    po_err = np.sqrt(np.diag(po_cov))
    print po_err

    a, b, c, d = tuple(po)

    return x, y, a, b, c, d
