import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt
import time
import os.path


def single_run(disk_number, radius):
    initial_time()

    circle_centers, clusters = find_percolation(disk_number, radius)

    # Save random coordinates in file to be able to deterministically duplicate the experiment and analyze data
    f = open(os.path.join('Logs', 'random_coordinates_%s.py' % time_stamp), 'w+')
    f.write('circle_centers = %s\n' % repr(circle_centers))
    f.close()
    output_file_name = write_output_file('# single_run(disk_number = %d, radius = %f)\n\n' % (disk_number, radius), \
            'clusters = %s\n' % repr(clusters)) # file title

    plot_graph(circle_centers, clusters, radius)
    return output_file_name


def multiple_runs_fixed_radius(iterations, min_density, max_density, density_interval, radius):
    # iterations - number of loops for each density
    initial_time()

    effective_densities = []
    perc_prob = []
    density = min_density

    while density <= max_density:
        percolation_amount = 0
        disk_number = round(density / (np.pi * radius ** 2)) # because can only have integer number of disks
        disk_density = disk_number * np.pi * radius ** 2 # need to recalculate disk density because it could differ from
                                                        #"density" in the loop because of rounding above
        eff_disk_density = 0.0
        for iteration in range(iterations):
            centers, clusters = find_percolation(disk_number, radius, find_all = False)
            centers_in_unit_square = [coord for coord in centers if 0.0 <= coord[0] <= 1.0 and 0.0 <= coord[1] <= 1.0]
            num_centers_in_unit_square = len(centers_in_unit_square)
            eff_disk_density += num_centers_in_unit_square * np.pi * radius ** 2 # statistically, area of circle outside
                                                    #of unit square is equal to area of circles that flow into unit square
            if has_percolation(clusters):
                percolation_amount += 1

        eff_disk_density /= iterations  # Arithmetic mean - need to calculate mean to plot it as a scatter plot,

        effective_densities.append(eff_disk_density)
        perc_prob.append(float(percolation_amount) / iterations)
        density += density_interval

    output_file_name = write_output_file('# multiple_runs_fixed_radius(iterations = %d, min_density = %f, max_density = %f, density_interval = %f, radius = %f)\n\n' \
            % (iterations, min_density, max_density, density_interval, radius), \
            'densities = %s\n\npercolation_probability = %s\n' % (effective_densities, perc_prob))

    return output_file_name


def multiple_runs_fixed_density(iterations, min_radius, max_radius, radius_interval, density):
    # iterations - number of iterations for min_radius.
    # For radii bigger than min_radius, the number of iterations is inveresely proportional to the number of disks.
    # This is done for optimisation purposes.
    initial_time()

    max_disk_number = round(density / (np.pi * min_radius ** 2) * (1 + 2*min_radius)**2)
      #multiplied by (1+2r)**2 because there need to be more disks in order to have "density" in the square with side 1+2r
    disk_num_times_it = iterations * max_disk_number

    radii = []
    perc_prob = []
    radius = min_radius

    while radius <= max_radius:
        percolation_amount = 0
        disk_number = round(density / (np.pi * radius ** 2) * (1 + 2*radius)**2)
        effective_radius = (2 * density + np.sqrt(disk_number * density * np.pi)) / (disk_number * np.pi - 4 * density)
        if effective_radius in radii:
            radius += radius_interval
            continue    # Avoid duplicate experiments with the same radius due to rounding.
                        #These would yield two points with same x coordinate.
        iterations_for_current_cycle = int(round(disk_num_times_it / disk_number))
        for iteration in range(iterations_for_current_cycle):
            centers, clusters = find_percolation(disk_number, effective_radius)
            if has_percolation(clusters):
                percolation_amount += 1

        perc_prob.append(float(percolation_amount) / iterations_for_current_cycle)
        radius += radius_interval

    output_file_name = write_output_file('# multiple_runs_fixed_density(iterations = %d, min_radius = %f, max_radius = %f, radius_interval = %f, density = %f)\n\n' \
            % (iterations, min_radius, max_radius, radius_interval, density), \
            'radii = %s\n\npercolation_probability = %s\n' % (radii, perc_prob))

    return output_file_name


def find_percolation(disk_number, radius, find_all = True):
    random_coordinates = np.array([rand.uniform(0 - radius, 1 + radius, size = disk_number * 2)])
    # rand.uniform: random distribution with equal probability everywhere;
    # centers are not generated between 0 and 1 because otherwise density would be smaller around the edges and therefore not uniform
    circle_centers = random_coordinates.reshape(disk_number, 2)
    return circle_centers, find_clusters(circle_centers, radius, find_all)


# Task 1
def check_overlap(array_of_centers, given_disk, list_of_disks, radius):
    """Check if a given disk overlaps with any of the disks in a list.
    Arguments:
    array_of_centers -- array of disk center coordinate pairs
    given_disk -- index of the given disk in array_of_centers
    list_of_disks -- index of other disks in array_of_centers
    radius -- disk radius
    Returns:
    List of indexes of the overlapping disks in array_of_centers
    """
    touching_disks = []
    four_radius_squared = 4 * radius ** 2
    x_given_disk = array_of_centers[given_disk, 0]
    y_given_disk = array_of_centers[given_disk, 1]
    for index in list_of_disks:
        delta_x = array_of_centers[index, 0] - x_given_disk
        delta_y = array_of_centers[index, 1] - y_given_disk
        distance_between_centers_squared = delta_x * delta_x + delta_y * delta_y
                            # This is faster than doing delta_x**2 and delta_y**2
        if distance_between_centers_squared <= four_radius_squared and index != given_disk:
            touching_disks.append(index)
    return touching_disks


# Task 2
def join_clusters(c1, c2):
    for i in c2['disks']:
        if i not in c1['disks']:
            c1['disks'].append(i)
    c1['disks'].sort()
    c1['left'] = c1['left'] or c2['left'] # if one of them is True, "or" gives True
    c1['right'] = c1['right'] or c2['right']
    return c1


# Tasks 3 and 4
def find_clusters(disk_coordinates, radius, find_all = True):
    '''takes as argument array of disk coordinates and a radius and
    returns a list containing the clusters'''
    clusters = []
    for disk_index, disk_xy in enumerate(disk_coordinates):
        clusters_to_join = []
        for cluster_index, cluster in enumerate(clusters):
            overlaps = check_overlap(disk_coordinates, disk_index, cluster['disks'], radius)
            if len(overlaps) > 0:   # Disk overlaps at least one of the disks in the cluster
                # insert disk in cluster
                cluster['disks'].append(disk_index)
                # and update left and right
                cluster['left'] = cluster['left'] or touch_left(disk_xy, radius)
                cluster['right'] = cluster['right'] or touch_right(disk_xy, radius)
                # remember matching cluster for possible future join
                clusters_to_join.append(cluster_index)
        if len(clusters_to_join) == 0: #given disk does not touch any of the disks in any of the existing clusters
            # create new cluster with this disk
            clusters.append({'disks': [disk_index], 'left': touch_left(disk_xy, radius), 'right': touch_right(disk_xy, radius)})
        elif len(clusters_to_join) >= 2: # given disk touches disks in more than one cluster
            # join clusters
            joint_cluster = clusters_to_join[0]
            clusters_to_remove = []
            for i in clusters_to_join[1:]:
                join_clusters(clusters[joint_cluster], clusters[i])
                clusters_to_remove.append(i)
            # clean up clusters in reverse order so that indexes don't change
            clusters_to_remove.reverse()
            for i in clusters_to_remove:
                clusters.remove(clusters[i])

        if not find_all and has_percolation(clusters):  # Early return if we need only one percolating cluster
            return clusters

    return clusters


def touch_left(disk_xy, radius):
    return disk_xy[0] <= radius

def touch_right(disk_xy, radius):
    return disk_xy[0] >= 1.0 - radius


def has_percolation(clusters): # system percolates if one of the clusters percolates
    for cluster in clusters:
        if cluster['right'] and cluster['left']:
            return True # if it finds one cluster that percolates, the loop stops
    return False

def plot_graph(circle_centers, all_clusters, radius):
    plt.axis('scaled') #same scale on x and y axis
    plt.axis([0, 1, 0, 1])
    # Coloring the clusters
    for cluster in all_clusters:
        percolation = cluster['right'] and cluster['left']
        if percolation:
            col = (1.0, rand.uniform(0, 0.30), rand.uniform(0, 0.20))   # Random shade of red
        else:
            col = (rand.uniform(0, 0.30), rand.uniform(0, 0.50), 0.80)  # Random shade of blue
        for disk_index in cluster['disks']:
            circle = plt.Circle((circle_centers[disk_index,0], circle_centers[disk_index,1]), radius = radius, color = col, alpha = .6)
            plt.gca().add_patch(circle)
    font = 'Helvetica Neue Thin'
    plt.title('Disk number: %d, Disk radius: %0.3f' % (len(circle_centers), radius), family = font, fontsize = 16)
    plt.axis('off')
    plt.show()

# Automatically save file with output
def write_output_file(params, result):
    filename = os.path.join('Output', 'output_%s.py' % time_stamp)
    f = open(filename, 'w+')
    f.write(params)
    f.write(result)
    f.close()
    return filename

# Unique stamp for file so the different versions don't override each other
def initial_time():
    # Time stamp needed for automatically saving output.
    global time_stamp   # Variable must be global because it's accessed from more than one function.
    time_stamp = time.strftime('%Y-%m-%d-%H-%M-%S',time.gmtime())
