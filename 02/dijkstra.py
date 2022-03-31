# Caio Ueno e João Augusto Leite

import numpy as np
import networkx as nx

if __name__ == "__main__":
    
    M, E, N, C = tuple(input().split())
    normal_edges = input().split()
    vent_edges = input().split()

    for _ in range(int(C)):
        
        source_node = int(input())
        
        # call dijkstra(source_node, 0, normal_matrix)
        # call dijkstra(source_node, 0, impostor_matrix)
        # compare minimum paths

        print("defeat")