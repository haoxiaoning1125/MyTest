# coding=utf-8
# 有向图, 单源最短路径: dijkstra
# 以起始点为中心向外层层扩散, 直到扩展到终点
# 1, 找出开销最小的节点, 即可在最短时间内到达的节点
# 2, 更新该节点邻居的开销
# 3, 重复上述过程, 直到对图中每个节点都进行了上述操作
# 4, 计算最终路径

INF = (1 << 32) - 1

GRAPH = {  # 节点开销, 记录各节点到相邻节点的路径长度
    'start': {'a': 6, 'b': 2},
    'a': {'end': 1},
    'b': {'a': 3, 'end': 5},
    'end': {}
}
COSTS = {'a': 6, 'b': 2, 'end': INF}  # 从起点到各节点的最短路径长度
PARENTS = {'a': 'start', 'b': 'start', 'end': None}  # 父节点
PROCESSED = []  # 已经处理过的节点


def find_lowest_cost_node(costs):
    """找到开销最小的节点"""
    lowest_cost = INF
    lowest_cost_node = None
    for node in costs:
        if node not in PROCESSED and costs[node] < lowest_cost:
            lowest_cost = costs[node]
            lowest_cost_node = node
    return lowest_cost_node


def find_shortest_path():
    """寻找最短路径"""
    node = 'end'
    shortest_path = ['end']
    while PARENTS.get(node) != 'start':
        shortest_path.append(PARENTS.get(node))
        node = PARENTS.get(node)
    shortest_path.append('start')
    shortest_path.reverse()
    return shortest_path


def dijkstra():
    node = find_lowest_cost_node(COSTS)  # 当前最小开销的节点
    while node is not None:
        cost = COSTS[node]
        neighbors = GRAPH[node]
        for n in neighbors:
            new_cost = cost + neighbors[n]
            if new_cost < COSTS[n]:
                COSTS[n] = new_cost
                PARENTS[n] = node
        PROCESSED.append(node)
        node = find_lowest_cost_node(COSTS)
    return find_shortest_path()


if __name__ == '__main__':
    print dijkstra()
