import argparse
import matplotlib.pyplot as plt
import numpy as np


def fibonacci_sphere(num_points):
    ga = (3 - np.sqrt(5)) * np.pi # golden angle                                                                             

    # Create a list of golden angle increments along tha range of number of points                                           
    theta = ga * np.arange(num_points)

    # Z is a split into a range of -1 to 1 in order to create a unit circle                                                  
    z = np.linspace(1/num_points-1, 1-1/num_points, num_points)

    # a list of the radii at each height step of the unit circle                                                             
    radius = np.sqrt(1 - z * z)

    # Determine where xy fall on the sphere, given the azimuthal and polar angles                                            
    y = radius * np.sin(theta)
    x = radius * np.cos(theta)

    # Display points in a scatter plot                                                                                       
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z)
    plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'fibonacci sphere')                       
    parser.add_argument('numpts', type=int, help='number of points/2 to distribute across spherical cap')
    args = parser.parse_args(200)
    fibonacci_sphere(int(args.numpts))