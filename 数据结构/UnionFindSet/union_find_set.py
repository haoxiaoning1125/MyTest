# coding=utf-8
# 并查集
# https://blog.csdn.net/qq_41593380/article/details/81146850


class UnionFindSet(object):
    def __init__(self, data_list):
        self.father_dict = {}  # 节点的父节点
        self.size_dict = {}  # 父节点的大小

        for node in data_list:
            self.father_dict[node] = node
            self.size_dict[node] = 1

    def find_head(self, node):
        # 查找根节点
        op_nodes = []
        while node != self.father_dict[node]:
            op_nodes.append(node)
            node = self.father_dict[node]
        for n in op_nodes:  # 优化
            self.father_dict[n] = node
            self.size_dict[n] = 1
        return node

    def in_same_set(self, node_a, node_b):
        # 两节点是否在同一集合
        return self.find_head(node_a) == self.find_head(node_b)

    def union(self, node_a, node_b):
        # 合并 node_a 和 node_b 所在的两个集合
        if node_a is None or node_b is None:
            return
        a_head = self.find_head(node_a)
        b_head = self.find_head(node_b)
        if a_head != b_head:
            a_set_size = self.size_dict[a_head]
            b_set_size = self.size_dict[b_head]
            if a_set_size >= b_set_size:
                self.father_dict[b_head] = a_head
                self.size_dict[a_head] = a_set_size + b_set_size
            else:
                self.father_dict[a_head] = b_head
                self.size_dict[b_head] = a_set_size + b_set_size

    def add_node(self, node, father):
        # 添加节点
        if father in self.father_dict.keys() and node not in self.father_dict.keys():
            self.size_dict[father] += 1
            self.size_dict[node] = 1
            self.father_dict[node] = father

    def __str__(self):
        return 'father_dict: {}\nsize_dict: {}'.format(self.father_dict, self.size_dict)


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    union_find_set = UnionFindSet(a)
    union_find_set.union(1, 2)
    union_find_set.union(3, 5)
    union_find_set.union(3, 1)
    print union_find_set.in_same_set(2, 5)
    print union_find_set
    print '-' * 30

    union_find_set.add_node(6, 4)
    union_find_set.add_node(7, 4)
    print union_find_set.in_same_set(6, 7)
    print union_find_set
    print '-' * 30

    union_find_set.add_node(8, 6)
    union_find_set.add_node(9, 8)
    union_find_set.add_node(10, 7)
    print union_find_set.in_same_set(9, 10)
    print union_find_set.in_same_set(9, 2)
    print union_find_set
