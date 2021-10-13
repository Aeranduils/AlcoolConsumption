import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

########################################################################################################################
#                                                   USER PARAMETERS                                                    #
########################################################################################################################

# Definit le chemin d'accès pour chaque dataset
data_file_pathname_mat = "C:\\Users\\FThef\\Desktop\\student-mat.csv"
data_file_pathname_por = "C:\\Users\\FThef\\Desktop\\student-por.csv"

########################################################################################################################
#                                                      LOAD DATA                                                       #
########################################################################################################################

# Ouvre et charge les données dans un data frame
my_data_frame_mat = pd.read_csv(data_file_pathname_mat, sep=",", header=0)
my_data_frame_por = pd.read_csv(data_file_pathname_por, sep=",", header=0)

# Affiche quelques enregistrements
print(my_data_frame_mat.head())

########################################################################################################################
#                                              GET INFORMATION ON THE DATA                                             #
########################################################################################################################

# Get the array from the dataframe
my_data_array = my_data_frame_mat.values

# Get the shape of the data
data_shape = my_data_array.shape

# Print the shape information in the console
print("\nIl y a " + str(data_shape[0]) + " enregistrements et " + str(data_shape[1]) + " attributs")

# Print the feature names in the console
print("\nLes catégories sont:")
for column_name in my_data_frame_mat.columns:
    print("     -" + column_name)

# Affiches les valeurs min et max ou les valeurs possibles pour chaque attribut
print("\n")
for column_name in my_data_frame_mat.columns:
    print("-" + column_name)
    column_data = my_data_frame_mat[column_name]

    if column_data.dtype != object:

        min_value = np.min(column_data)
        max_value = np.max(column_data)
        nan_presence = np.sum(np.isnan(column_data))

        print("     La valeur minimal " + str(min_value) + " et le maximum est " + str(max_value))
        print("     Nombre de NaN: " + str(nan_presence))
    else :
        values = np.unique(column_data)
        print("     Les valeurs possibles sont " + str(values))


# Affiche les infos de la colonne 'famsup'
class_id = np.unique(my_data_frame_mat["famsup"])
print("\nInformation sur la colonne 'famsup':")
for id_value in class_id:
    indices = np.where(my_data_frame_mat["famsup"] == id_value)
    print("     -" + str(id_value) + " avec " + str(indices[0].size) + " enregistrements")

# Affiche le nombre de NaN par attribut
print("\nNombre de NaN par attribut")
print(my_data_frame_mat.isna().sum())

# Affiche les attributs et leur type
print(my_data_frame_mat.info())


# Affichage des stats par attributs
data_frame_stat = my_data_frame_mat[['age','absences', 'G1', 'G2', 'G3']]

print("\nStatistiques: ")
print(data_frame_stat.describe())



















