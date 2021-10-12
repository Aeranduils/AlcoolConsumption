import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

########################################################################################################################
#                                                   USER PARAMETERS                                                    #
########################################################################################################################

# Define the pathname of the data file to exploit
data_file_pathname_mat = "C:\\Users\\FThef\\Desktop\\student-mat.csv"
data_file_pathname_por = "C:\\Users\\FThef\\Desktop\\student-por.csv"

########################################################################################################################
#                                                      LOAD DATA                                                       #
########################################################################################################################

# Open and load the data
my_data_frame_mat = pd.read_csv(data_file_pathname_mat, sep=",", header=0)
my_data_frame_por = pd.read_csv(data_file_pathname_por, sep=",", header=0)

# Print some instances in the console
print(my_data_frame_mat.head())

########################################################################################################################
#                                              GET INFORMATION ON THE DATA                                             #
########################################################################################################################

# Get the array from the dataframe
my_data_array = my_data_frame_mat.values

# Get the shape of the data
data_shape = my_data_array.shape

# Print the shape information in the console
print("\nThere is " + str(data_shape[0]) + " instances and " + str(data_shape[1]) + " features")

# Print the feature names in the console
print("\nThe features are:")
for column_name in my_data_frame_mat.columns:
    print("     -" + column_name)

# Get the min and max values for each feature and print them in the console
print("\n")
for column_name in my_data_frame_mat.columns:
    print("-" + column_name)

    column_data = my_data_frame_mat[column_name]

    if column_data.dtype != np.str:

        min_value = np.min(column_data)
        max_value = np.max(column_data)
        #nan_presence = np.sum(np.isnan(column_data))

        print("     the minimum value is " + str(min_value) + " and the maximum value is " + str(max_value))
        #print("         there are NaN value: " + str(nan_presence))

# Print information on the "DEATH_EVENT" column
class_id = np.unique(my_data_frame_mat["famsup"])
print("\nInformation on the 'famsup' column:")
for id_value in class_id:

    indices = np.where(my_data_frame_mat["famsup"] == id_value)
    print("     -" + str(id_value) + " with " + str(indices[0].size) + " instances")







