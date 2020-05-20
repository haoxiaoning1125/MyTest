# # coding=utf-8
# # 单源最短路径, 允许负权边: bellman-ford
#
# INF = (1 << 32) - 1
#
# GRAPH = {  # 起点为a, 求节点a到其余各节点的最短路径
#     'a': {'b': -3, 'e': -5},
#     'b': {'c': 2},
#     'c': {'d': 3},
#     'd': {'e': 2},
#     'e': {}
# }
#
# DIS = {'a': 0, 'b': INF, 'c': INF, 'd': INF, 'e': INF}
# NODES = ['a', 'b', 'c', 'd', 'e']
# NODE_COUNT = 5
# EDGE_COUNT = 5
#
#
# def bellman_ford():
#     for node in NODES:
#         for j in range(EDGE_COUNT):
#             if DIS[node] >
