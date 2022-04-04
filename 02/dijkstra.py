# Caio Ueno e João Augusto Leite

import numpy as np


def dijkstra(source_node: int, target_node: int, adj_matrix: np.ndarray):

    if source_node == target_node:
        return 0

    vertices = [i for i in range(adj_matrix.shape[0])]

    # store final min cost of path to vertice from source node
    min_costs = {}

    # costs to vertices to use/update during algorithm
    lambdas = {v: np.inf for v in vertices}

    # set source node cost to 0
    lambdas[source_node] = 0

    while len(lambdas) > 0:

        u = min(lambdas, key=lambdas.get)

        neighbors = np.argwhere(adj_matrix[u, :]).ravel()

        for n in neighbors:
            # if n is still on lambdas dict
            # and cost to to through u is less
            # than its current cost
            if n in lambdas.keys() and adj_matrix[u, n] + lambdas[u] < lambdas[n]:
                lambdas[n] = adj_matrix[u, n] + lambdas[u]
                min_costs[n] = adj_matrix[u, n] + lambdas[u]

        lambdas.pop(u)

        if u == target_node:
            break

    return min_costs[target_node]


if __name__ == "__main__":

    M, E, N, C = tuple(input().split())
    normal_edges = input().split()
    vent_edges = input().split()

    normal_matrix = np.zeros((int(M), int(M)), dtype=float)

    # fill normal_matrix
    for i in range(0, 3 * int(E), 3):

        v1, v2, dist = tuple(normal_edges[i : i + 3])
        v1, v2, dist = int(v1), int(v2), float(dist)

        normal_matrix[v1, v2] = dist
        normal_matrix[v2, v1] = dist

    impostor_matrix = normal_matrix.copy()

    # fill impostor_matrix
    for i in range(0, 2 * int(N), 2):

        v1, v2 = tuple(vent_edges[i : i + 2])
        v1, v2 = int(v1), int(v2)

        # vent is better than hall or there is no hall
        if impostor_matrix[v1, v2] >= 1 or impostor_matrix[v1, v2] == 0:
            impostor_matrix[v1, v2] = 1
            impostor_matrix[v2, v1] = 1

    # print(normal_matrix)
    # print(impostor_matrix)

    for _ in range(int(C)):

        source_node = int(input())

        my_cost = dijkstra(source_node, 0, normal_matrix)
        impostor_cost = dijkstra(source_node, 0, impostor_matrix)

        if my_cost <= impostor_cost:
            print("victory")
        else:
            print("defeat")
