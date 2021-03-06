
import matplotlib.pyplot as plt

from random_walk import RandomWalk


# keep making new walks as long as the program is active
while True:

    # make random walk and plot the lines
    rw = RandomWalk(5000)

    rw.fill_walk()

    # set the size of the plotting window
    plt.figure(dpi=128, figsize=(10, 6))

    point_numbers = list(range(rw.num_points))

    plt.plot(rw.x_values,
             rw.y_values)


    # emphasize first and last point
    plt.scatter(0, 0, c='orange', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # remove the axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("make another walk?: ")
    if keep_running == 'n':
        break



