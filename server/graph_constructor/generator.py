import networkx as nx
import random
from itertools import combinations, groupby
from pyvis.network import Network

def gnp_random_connected_graph(n, p):
    id = 0
    edges = combinations(range(n), 2)
    G = nx.MultiDiGraph()
    G.add_nodes_from(range(n))
    if p <= 0:
        return G
    if p >= 1:
        return nx.complete_graph(n, create_using=G)
    for _, node_edges in groupby(edges, key=lambda x: x[0]):
        node_edges = list(node_edges)
        random_edge = random.choice(node_edges)
        print(*random_edge)
        G.add_edge(*random_edge, weight=round(random.random(), 1), type = 0, id = id)
        id+= 1
        # G.add_edge(*random_edge, weight=round(random.random(), 1), type = 0, id = id)
        # id+= 1
        # G.add_edge(*random_edge, weight=round(random.random(), 1), type = 0, id = id)
        # id+= 1


        G.add_edge(*random_edge[::-1], weight=round(random.random(), 1), type = 0, id = id)
        id+= 1
        # G.add_edge(*random_edge[::-1], weight=round(random.random(), 1), type = 0, id = id)
        # id+= 1
        # G.add_edge(*random_edge[::-1], weight=round(random.random(), 1), type = 0, id = id)
        # id+= 1
        # for e in node_edges:
        #     if random.random() < p:
        #         G.add_edge(*e)
    return G

if __name__ == "__main__":
    nodes = 10
    probability = 0.2
    G = gnp_random_connected_graph(nodes, probability)  
    print(G.edges)
    # Создаем объект графа Pyvis
    net = Network(height="400px", width="600px", directed =True)
    net.from_nx(G)
    print(net)
    net.save_graph("random_multi_graph.html")
