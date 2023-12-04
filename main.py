import os #teatee
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from genieclust import Genie
from sklearn.cluster import KMeans, SpectralClustering, DBSCAN, OPTICS, HDBSCAN
#from hdbscan import HDBSCAN
from root import root
from calculate_results import calculate_results
#from clustering_algoritms import clustering_algoritm
import random

# Any number can be used in place of '0'.
from IPython import get_ipython
#get_ipython().magic('reset -sf')

random.seed(0)


# Parâmetros da simulação
load_path = r'C:\Users\dl_ca\OneDrive - Universidade Federal do Pará - UFPA\Documentos\Python Scripts\cran-simple-UAV-clustering'
#os.chdir(load_path)

data = pd.read_csv("bairros_filtrados.csv")
#data.plot(x="X1", y="X2", kind="scatter");

#n_clusters = 12
#m = ClDev(clusterer='kmeans', n_clusters=5, standardize=False)
#labels = m.fit_predict(data)
#m.visualize(data)
#data3 = find_centroids(data, labels, n_clusters)
#data2 = m.cluster_centers_

sel_n_clusters = 12
x=1
total=1
resu=[]
for x in range(sel_n_clusters):
    model = KMeans(n_clusters=total, random_state=0, verbose=1)

    labels = model.fit_predict(data)
    l_clusters = list(np.unique(labels))

    centr = []
    for c in l_clusters:
        temp_data = data.iloc[labels == c]
        centroid = list(temp_data.mean())
        centr.append(centroid)
    centr = pd.DataFrame(centr, columns=['X1','X2'])

    uav2 = pd.DataFrame(centr, columns=['X1','X2']);
    total_number_of_users = len(data);
    number_of_small_base_stations = len(uav2);
    results, base_station_users_and_throughputs, total_users_data_rate = root(total_number_of_users, data, number_of_small_base_stations, uav2)
    print("teste",x, "resultados",results)
    resu.append(results)
    total = x + 1

#total_users_data_rate = calculate_results(data,uav2)
count=0
for x in resu:
    print(count,x)
   # print ("valores")
   # print("qtd=",x[0])
   # print("taxa=", x[2])
   # print("UAVS ON=", x[8])
    count=count+1

plt.scatter(data["X1"], data["X2"], marker='o', c='blue', label='usuario')
plt.scatter(centr["X1"], centr["X2"], marker='x', c='red', label='Sc')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.legend()
plt.title("Kmeans Clustering")
plt.show()

###########################

