from percolation import single_run, multiple_runs_fixed_radius, multiple_runs_fixed_density

# Fixed radius
for r in [0.08, 0.07, 0.06, 0.05, 0.04, 0.03, 0.02]:
    multiple_runs_fixed_radius(iterations = 500, min_density = 0.5, max_density = 2.5, density_interval = 0.1, radius = r)

# Fixed density
multiple_runs_fixed_density(iterations = 10000, min_radius = 0.05, max_radius = 0.5, radius_interval = 0.01, density = 1.0)
multiple_runs_fixed_density(iterations = 10000, min_radius = 0.05, max_radius = 0.5, radius_interval = 0.01, density = 1.1)
multiple_runs_fixed_density(iterations = 10000, min_radius = 0.05, max_radius = 0.5, radius_interval = 0.01, density = 1.2)
multiple_runs_fixed_density(iterations = 10000, min_radius = 0.05, max_radius = 0.5, radius_interval = 0.01, density = 1.3)
multiple_runs_fixed_density(iterations = 10000, min_radius = 0.05, max_radius = 0.5, radius_interval = 0.01, density = 1.4)
multiple_runs_fixed_density(iterations = 10000, min_radius = 0.05, max_radius = 0.5, radius_interval = 0.01, density = 1.5)

multiple_runs_fixed_density(iterations = 10000, min_radius = 0.05, max_radius = 0.5, radius_interval = 0.01, density = 1.11)
multiple_runs_fixed_density(iterations = 10000, min_radius = 0.05, max_radius = 0.5, radius_interval = 0.01, density = 1.12)
multiple_runs_fixed_density(iterations = 10000, min_radius = 0.05, max_radius = 0.5, radius_interval = 0.01, density = 1.13)
multiple_runs_fixed_density(iterations = 10000, min_radius = 0.05, max_radius = 0.5, radius_interval = 0.01, density = 1.14)
multiple_runs_fixed_density(iterations = 10000, min_radius = 0.05, max_radius = 0.5, radius_interval = 0.01, density = 1.15)
multiple_runs_fixed_density(iterations = 10000, min_radius = 0.05, max_radius = 0.5, radius_interval = 0.01, density = 1.16)
multiple_runs_fixed_density(iterations = 10000, min_radius = 0.05, max_radius = 0.5, radius_interval = 0.01, density = 1.17)
multiple_runs_fixed_density(iterations = 10000, min_radius = 0.05, max_radius = 0.5, radius_interval = 0.01, density = 1.18)
multiple_runs_fixed_density(iterations = 10000, min_radius = 0.05, max_radius = 0.5, radius_interval = 0.01, density = 1.19)
#multiple_runs_fixed_density(iterations = 10000, min_radius = 0.05, max_radius = 0.5, radius_interval = 0.01, density = 1.21)
#multiple_runs_fixed_density(iterations = 10000, min_radius = 0.05, max_radius = 0.5, radius_interval = 0.01, density = 1.22)
#multiple_runs_fixed_density(iterations = 10000, min_radius = 0.05, max_radius = 0.5, radius_interval = 0.01, density = 1.23)

# Fixed radius
multiple_runs_fixed_radius(iterations = 500, min_density = 0.5, max_density = 2.5, density_interval = 0.1, radius = 0.01)
