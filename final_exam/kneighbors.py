import matplotlib.pyplot as plt

def PlotNearestNeighbors(neighbor_list, color_list, test_point, test_index):

    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(12,5))

    if len(neighbor_list) != len(color_list):
        raise ValueError("Error: unable to plot K-Nearest Neighbors because the " + \
                         "'neighbor_list' and 'color_list' have different lengths");

    x_values = [point[0] for neighbors in neighbor_list for point in neighbors]
    y_values = [point[1] for neighbors in neighbor_list for point in neighbors]
    c_values = [color_list[neighbor_list.index(neighbors)] for \
                             neighbors in neighbor_list for point in neighbors]    

    # add the test_points xy-coordinate but we'll add the color a little later
    x_values.append(test_point[0])
    y_values.append(test_point[1])

    ax[0].set_title("Original Sets with Test Point", fontsize=14, pad=15)
    ax[0].scatter(x_values, y_values, c=c_values + ['r'])
    ax[0].set_xticks([])
    ax[0].set_yticks([])

    ax[1].set_title("New Sets Using KNN Classifier", fontsize=14, pad=15)
    ax[1].scatter(x_values, y_values, c=c_values + [color_list[test_index]])
    ax[1].set_xticks([])
    ax[1].set_yticks([])
    plt.show()