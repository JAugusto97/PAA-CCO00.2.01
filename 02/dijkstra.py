# Caio Ueno e João Augusto Leite

import numpy as np
import networkx as nx

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

    print(normal_matrix)
    print(impostor_matrix)

    for _ in range(int(C)):

        source_node = int(input())

        # call dijkstra(source_node, 0, normal_matrix)
        # call dijkstra(source_node, 0, impostor_matrix)
        # compare minimum paths

        print("defeat")
