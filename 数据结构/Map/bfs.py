# coding=utf-8

from pprint import pprint


def bfs(start, matrix):  # start: [x, y]
    """广度优先遍历"""
    n = len(matrix)
    queue_ = [start]
    vis = [[0 for y in range(n)] for x in range(n)]
    vis[start[0]][start[1]] = 1
    dires = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    while queue_:
        x, y = queue_.pop(0)
        for dx, dy in dires:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not vis[nx][ny] and matrix[nx][ny] == 1:
                queue_.append([nx, ny])
                vis[nx][ny] = 1
    return vis


if __name__ == '__main__':
    matrix = [  # 1: 通, 0: 不通
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1],
        [1, 1, 0, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 0]
    ]
    vis = bfs([0, 0], matrix)
    pprint(vis)
