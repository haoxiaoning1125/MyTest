# coding=utf-8

from pprint import pprint


def dfs(start, matrix, vis):
    """深度优先遍历"""
    dires = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    x, y = start
    vis[x][y] = 1
    for dx, dy in dires:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and not vis[nx][ny] and matrix[nx][ny] == 1:
            dfs([nx, ny], matrix, vis)


if __name__ == '__main__':
    matrix = [  # 1: 通, 0: 不通
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1],
        [1, 1, 0, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 0]
    ]
    n = len(matrix)
    vis = [[0 for i in range(n)] for j in range(n)]
    dfs([0, 0], matrix, vis)
    pprint(vis)
