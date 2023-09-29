import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from genieclust import Genie
from sklearn.cluster import KMeans, SpectralClustering, DBSCAN, OPTICS
#from hdbscan import HDBSCAN
from root import root
#from clustering_algoritms import clustering_algoritm
import random

# Any number can be used in place of '0'.
from IPython import get_ipython
#get_ipython().magic('reset -sf')

random.seed(0)


# Parâmetros da simulação
load_path = r'C:\Users\dl_ca\OneDrive - Universidade Federal do Pará - UFPA\Documentos\Python Scripts\cran-simple-UAV-clustering'
#os.chdir(load_path)

data = pd.read_csv("data_X.csv")
#data.plot(x="X1", y="X2", kind="scatter");

#n_clusters = 5
#m = ClDev(clusterer='kmeans', n_clusters=5, standardize=False)
#labels = m.fit_predict(data)
#m.visualize(data)
#data3 = find_centroids(data, labels, n_clusters)
#data2 = m.cluster_centers_

sel_n_clusters = 6

#Aqui vou inserir as clusterizacoes
#########################
model = Genie(n_clusters=sel_n_clusters, gini_threshold=0.3, M=1, exact=True, verbose=1)

labels = model.fit_predict(data)
l_clusters = list(np.unique(labels))

centr = []
for c in l_clusters:
    temp_data = data.iloc[labels == c]
    centroid = list(temp_data.mean())
    centr.append(centroid)
centr = pd.DataFrame(centr, columns=['X','Y'])

plt.scatter(data["X1"], data["X2"], marker='o', c = 'blue', label='usuario')
plt.scatter(centr["X"], centr["Y"], marker='o', c = 'red', label='Sc')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.legend()
plt.title("Genie Clustering")
plt.show()

centr

uav2 = pd.DataFrame(centr, columns=['X','Y']);
total_number_of_users = len(data);
number_of_small_base_stations = len(uav2);
results, base_station_users_and_throughputs, total_users_data_rate = root(total_number_of_users, data, number_of_small_base_stations, uav2)
print('Conexão finalizada do Genie')
###########################
#########################
model = KMeans(n_clusters=sel_n_clusters, random_state=0, verbose=1)

labels = model.fit_predict(data)
l_clusters = list(np.unique(labels))

centr = []
for c in l_clusters:
    temp_data = data.iloc[labels == c]
    centroid = list(temp_data.mean())
    centr.append(centroid)
centr = pd.DataFrame(centr, columns=['X','Y'])

plt.scatter(data["X1"], data["X2"], marker='o', c = 'blue', label='usuario')
plt.scatter(centr["X"], centr["Y"], marker='o', c = 'red', label='Sc')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.legend()
plt.title("Kmeans Clustering")
plt.show()

centr

uav2 = pd.DataFrame(centr, columns=['X','Y']);
total_number_of_users = len(data);
number_of_small_base_stations = len(uav2);
results, base_station_users_and_throughputs, total_users_data_rate = root(total_number_of_users, data, number_of_small_base_stations, uav2)
print('Conexão finalizada do Kmeans')
###########################
#########################
model = DBSCAN(eps=0.5, min_samples=5, metric='euclidean', n_jobs=None)

labels = model.fit_predict(data)
l_clusters = list(np.unique(labels))

centr = []
for c in l_clusters:
    temp_data = data.iloc[labels == c]
    centroid = list(temp_data.mean())
    centr.append(centroid)
centr = pd.DataFrame(centr, columns=['X','Y'])

plt.scatter(data["X1"], data["X2"], marker='o', c = 'blue', label='usuario')
plt.scatter(centr["X"], centr["Y"], marker='o', c = 'red', label='Sc')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.legend()
plt.title("DBSCAN Clustering")
plt.show()

centr

uav2 = pd.DataFrame(centr, columns=['X','Y']);
total_number_of_users = len(data);
number_of_small_base_stations = len(uav2);
results, base_station_users_and_throughputs, total_users_data_rate = root(total_number_of_users, data, number_of_small_base_stations, uav2)
print('Conexão finalizada do DBSCAN')
###########################
# #########################

model = OPTICS(min_samples=5,
                        min_cluster_size=None,
                        metric='euclidean',
                        xi=0.05,
                        n_jobs=None)

labels = model.fit_predict(data)
l_clusters = list(np.unique(labels))

centr = []
for c in l_clusters:
    temp_data = data.iloc[labels == c]
    centroid = list(temp_data.mean())
    centr.append(centroid)
centr = pd.DataFrame(centr, columns=['X','Y'])

plt.scatter(data["X1"], data["X2"], marker='o', c = 'blue', label='usuario')
plt.scatter(centr["X"], centr["Y"], marker='o', c = 'red', label='Sc')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.legend()
plt.title("Optics Clustering")
plt.show()

centr

uav2 = pd.DataFrame(centr, columns=['X','Y']);
total_number_of_users = len(data);
number_of_small_base_stations = len(uav2);
results, base_station_users_and_throughputs, total_users_data_rate = root(total_number_of_users, data, number_of_small_base_stations, uav2)
print('Conexão finalizada do Optics')
# ###########################
# #########################
model = HDBSCAN(min_cluster_size=None,
                         min_samples=5,
                         metric='euclidean',
                         )

labels = model.fit_predict(data)
l_clusters = list(np.unique(labels))

centr = []
for c in l_clusters:
    temp_data = data.iloc[labels == c]
    centroid = list(temp_data.mean())
    centr.append(centroid)
centr = pd.DataFrame(centr, columns=['X','Y'])

plt.scatter(data["X1"], data["X2"], marker='o', c = 'blue', label='usuario')
plt.scatter(centr["X"], centr["Y"], marker='o', c = 'red', label='Sc')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.legend()
plt.title("HDBSCAN Clustering")
plt.show()

centr

uav2 = pd.DataFrame(centr, columns=['X','Y']);
total_number_of_users = len(data);
number_of_small_base_stations = len(uav2);
results, base_station_users_and_throughputs, total_users_data_rate = root(total_number_of_users, data, number_of_small_base_stations, uav2)
print('Conexão finalizada do HDBSCAN')
###########################
#########################
model = SpectralClustering(n_clusters=sel_n_clusters, affinity='rbf', assign_labels='discretize',
                                random_state=None, n_jobs=None)

labels = model.fit_predict(data)
l_clusters = list(np.unique(labels))

centr = []
for c in l_clusters:
    temp_data = data.iloc[labels == c]
    centroid = list(temp_data.mean())
    centr.append(centroid)
centr = pd.DataFrame(centr, columns=['X','Y'])

plt.scatter(data["X1"], data["X2"], marker='o', c = 'blue', label='usuario')
plt.scatter(centr["X"], centr["Y"], marker='o', c = 'red', label='Sc')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.legend()
plt.title("Spectral Clustering")
plt.show()

centr

uav2 = pd.DataFrame(centr, columns=['X','Y']);
total_number_of_users = len(data);
number_of_small_base_stations = len(uav2);
results, base_station_users_and_throughputs, total_users_data_rate = root(total_number_of_users, data, number_of_small_base_stations, uav2)
print('Conexão finalizada do Spectral')
###########################