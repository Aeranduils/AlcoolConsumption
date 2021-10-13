import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


def plot_bar_graphics(column_name, class_id, my_data_frame):
    my_width = 0.3
    counter = 0
    for id_value in class_id:

        indices = np.where(my_data_frame["school"] == id_value)
        column_data = my_data_frame[column_name].values[indices]

        # Get all possible values in the column "anaemia"
        feature_values = np.unique(column_data)

        # Initialize variable
        tmp_percentages = []

        for value in feature_values:
            tmp_indices = np.where(column_data == value)
            tmp_percentages.append((tmp_indices[0].size / indices[0].size) * 100)

        data_label = "school" + str(id_value)

        if counter == 0:

            plt.bar(feature_values - (my_width / 2), tmp_percentages, width=my_width, alpha=0.5,
                    label=data_label, edgecolor="k")
            counter = counter + 1

        else:

            plt.bar(feature_values + (my_width / 2), tmp_percentages, width=my_width, alpha=0.5,
                    label=data_label, edgecolor="k")

    plt.title("People with or not " + column_name, fontsize=10)
    plt.xlabel(column_name + " No = 0 and Yes = 1")
    plt.ylabel("Percentage of people among each group")
    plt.legend(loc="upper right")
    plt.show()