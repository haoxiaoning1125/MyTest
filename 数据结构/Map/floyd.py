# coding=utf-8
# 有向图, 多源最短路径: floyd
# 1, 用GRAPH记录当前各节点间的最短路径长度, 初始为图的邻接矩阵
# 2, 将每个节点作为中间节点, 若经过中间节点路径更短, 则更新GRAPH

from pprint import pprint

INF = (1 << 32) - 1
GRAPH = {  # 节点开销, 记录各节点到相邻节点的路径长度
    'start': {'start': INF, 'a': 6, 'b': 2, 'end': INF},
    'a': {'start': INF, 'a': INF, 'b': INF, 'end': 1},
    'b': {'start': INF, 'a': 3, 'b': INF, 'end': 5},
    'end': {'start': INF, 'a': INF, 'b': INF, 'end': INF}
}
NODES = ['start', 'a', 'b', 'end']


def floyd():
    for i in NODES:  # 中间点
        for j in NODES:
            for k in NODES:
                j_i = GRAPH[j][i]
                i_k = GRAPH[i][k]
                j_k = GRAPH[j][k]
                if j_i + i_k < j_k:
                    GRAPH[j][k] = GRAPH[j][i] + GRAPH[i][k]


if __name__ == '__main__':
    floyd()
    pprint(GRAPH)
