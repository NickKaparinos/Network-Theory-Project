# Network Theory Project
# Aristotle University of Thessaloniki
# Nick Kaparinos
# 2020

# The purpose of this script is to analyse a graph given in a .gml file
import time

import matplotlib.pyplot as plt
import networkx as nx
import seaborn as sns

print("Analyse Graph")
plt.ion()
#G = nx.read_gml("HeavyMetal476.gexf")
G = nx.read_gexf("HeavyMetal476.gexf")
start = time.perf_counter()

# Anlyse Graph
# Degrees
degrees = nx.degree(G)
inDegrees = nx.in_degree_centrality(G)
outDegrees = nx.out_degree_centrality(G)
print("1")

# Metrics
if nx.is_weakly_connected(G):
    Gundirected = nx.to_undirected(G)
    print("undirected")
    center = nx.center(Gundirected)
    eccentricity = nx.eccentricity(Gundirected)
    diameter = nx.diameter(Gundirected)
    radius = nx.radius(Gundirected)
else:
    center = nx.center(G)
    eccentricity = nx.eccentricity(G)
    diameter = nx.diameter(G)
    radius = nx.radius(G)

# Average shortest path length
averageShortestPath = nx.average_shortest_path_length(G)
print("4")

# Transivity
transivity = nx.transitivity(G)
print("7")

# Clustering coefficient
clusteringCoeff = nx.average_clustering(G)
clustering = nx.clustering(G)
print("5")

# Centrality
closenessCentrality = nx.closeness_centrality(G)
betweensCentrality = nx.betweenness_centrality(G)
katzCentrality = nx.katz_centrality_numpy(G)
eigenCentrality = nx.eigenvector_centrality_numpy(G)
print("3")

# Page rank
pageRank = nx.pagerank_scipy(G)
print("6")

# Hits Authorities
hubs, authorities = nx.hits_scipy(G)

print(f"Total run time = {time.perf_counter() - start}.")

# Results
message = f"Analysis complete!\nExecution time = {time.perf_counter() - start:.2f} second(s).\nThe graph is "
directed = "directed" if nx.is_directed(G) == True else "undirected"
message += directed

if nx.is_directed(G):
    if nx.is_strongly_connected(G):
        connected = " and strongly connected.\n"
    elif nx.is_weakly_connected(G):
        connected = " and weekly connected.\n"
    else:
        connected = " and disconnected\n"
else:
    if nx.is_connected(G):
        connected = " and connected.\n"
    else:
        connected = " and disconnected\n"
message += connected
print(message)

print(
    f"Center = {center}\ndiameter = {diameter}\nradius = {radius}\nAverage shortest path length = {averageShortestPath:.4f}\nTransivity = {transivity:.4f}\nClustering coefficient = {clusteringCoeff:.4f}")

# Degree plots
degrees = [i[1] for i in list(G.degree)]
inDegrees = [i[1] for i in list(G.in_degree)]
outDegrees = [i[1] for i in list(G.out_degree)]

# plt.figure(100)
sns.displot(degrees)
plt.title("Node degree distribution")
plt.xlabel("Node degree")

fet = 5

# plt.figure(101)
sns.displot(inDegrees)
plt.title("Node in degree distribution")
plt.xlabel("Node in degree")

# plt.figure(102)
sns.displot(outDegrees)
plt.title("Node out degree distribution")
plt.xlabel("Node out degree")

# Gather dictionaries in a list and sort them on values
listOfDicts = [closenessCentrality, betweensCentrality, katzCentrality, eigenCentrality, pageRank, authorities, hubs]
dictNames = ["Closeness Centrality", "Betweens Centrality", "Katz Centrality", "Eigenvector Centrality", "Page Rank",
             "Authorities", "Hubs"]

listOfDicts = [{k: v for k, v in sorted(i.items(), key=lambda item: item[1], reverse=True)} for i in listOfDicts]
fet = 5
# Scatterplots of the 20 nodes with the highest values in each dictionary
for i in range(len(listOfDicts)):
    dict = listOfDicts[i]
    name = dictNames[i]

    j = 0
    limit = 20
    dictToPlot = {}
    for k, v in dict.items():
        dictToPlot[k] = v
        j += 1
        if j == limit:
            break

    # plt.figure(i)
    # ax = plt.axes()
    # sns.scatterplot(x=dictToPlot.values(), y=dictToPlot.keys())
    # ax.set_title(name + f": Scatterplot of the {limit} nodes with highest value")
    # plt.show()
    plt.figure(i + 4)
    sns.scatterplot(x=dictToPlot.values(), y=dictToPlot.keys())
    plt.title(name + f": {limit} nodes with highest value")

# Authorities Hubs
# for i in range(3):
#     a = list(listOfDicts[6].keys())[0]
#     print(f"Authority number {i+1} :" + a + "\nPredecessors:")
#     for j in G.successors(a):
#         print(j)

# i = 0
# fet = {}
# for k, v in listOfDicts[3].items():
#     i += 1
#     fet[k] = v
#     if (i == 50):
#         break
# ax = plt.axes()
# sns.scatterplot(y=fet.keys(), x=fet.values())
# ax.set_title("fet")
# plt.show()

# closenessCentrality = {k: v for k, v in sorted(closenessCentrality.items(), key=lambda item: item[1], reverse=True)}
# betweensCentrality = {k: v for k, v in sorted(betweensCentrality.items(), key=lambda item: item[1], reverse=True)}
# katzCentrality = {k: v for k, v in sorted(katzCentrality.items(), key=lambda item: item[1], reverse=True)}
# eigenCentrality = {k: v for k, v in sorted(eigenCentrality.items(), key=lambda item: item[1], reverse=True)}
# pageRank = {k: v for k, v in sorted(pageRank.items(), key=lambda item: item[1], reverse=True)}
# authorities = {k: v for k, v in sorted(authorities.items(), key=lambda item: item[1], reverse=True)}
# hubs = {k: v for k, v in sorted(hubs.items(), key=lambda item: item[1], reverse=True)}

# Check components, clustering, clique, community
debug = True
plt.ioff()
plt.show()
