# coding=utf-8
# 有向图, 多源最短路径: floyd
# 1, 用GRAPH记录当前各节点间的最短路径长度, 初始为图的邻接矩阵
# 2, 将每个节点作为中间节点, 若经过中间节点路径更短, 则更新GRAPH

from pprint import pprint

INF = (1 << 32) - 1
GRAPH = {  # 节点开销, 记录各节点到相邻节点的路径长度
    'v0': {'v0': INF, 'v1': 30, 'v2': INF, 'v3': 10, 'v4': 50},
    'v1': {'v0': INF, 'v1': INF, 'v2': 60, 'v3': INF, 'v4': 80},
    'v2': {'v0': INF, 'v1': INF, 'v2': INF, 'v3': INF, 'v4': INF},
    'v3': {'v0': INF, 'v1': INF, 'v2': INF, 'v3': INF, 'v4': 30},
    'v4': {'v0': 50, 'v1': INF, 'v2': 40, 'v3': INF, 'v4': INF}
}
NODES = ['v0', 'v1', 'v2', 'v3', 'v4']


def floyd():
    for k in NODES:  # 中间点
        for i in NODES:
            for j in NODES:
                GRAPH[i][j] = min(GRAPH[i][j], GRAPH[i][k] + GRAPH[k][j])


if __name__ == '__main__':
    floyd()
    pprint(GRAPH)

    diameter = 0
    for node_1 in NODES:
        for node_2 in NODES:
            d = GRAPH[node_1][node_2]
            if d != INF and d > diameter:
                diameter = d
    print '-' * 80 + '\ndiameter of the map: {}'.format(diameter)
