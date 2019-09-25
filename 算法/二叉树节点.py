# coding=utf-8
# 给定满二叉树, 求中序遍历序列的下一个节点


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = None

    def build_tree(self, list):
        # 层序遍历 -> 二叉树
        # 每次取出两个节点, 依次作为之前节点的左右节点
        if list[0]:
            root = Node(list[0])
            self.root = root
            nodes = [root]
            id = 1
            while nodes and id < len(list):
                node = nodes[0]
                node.left = Node(list[id]) if list[id] else None
                nodes.append(node.left)
                node.right = Node(list[id+1]) if list[id+1] and id < len(list) - 1 else None
                nodes.append(node.right)
                id += 2
                nodes.pop(0)
        else:
            return

    def travel_by_lev(self):
        # 层序遍历
        ret = []
        if self.root is not None:
            ret = []
            nodes = [self.root]
            while nodes:
                node = nodes[0]
                ret.append(node.data)
                if node.left is not None:
                    nodes.append(node.left)
                if node.right is not None:
                    nodes.append(node.right)
                nodes.pop(0)
        return ret

    def travel_by_ldr(self):
        # 中序遍历
        def ldr(node, ret):
            if node is None:
                return
            else:
                ldr(node.left, ret)
                ret.append(node.data)
                ldr(node.right, ret)

        ret = []
        ldr(self.root, ret)
        return ret


if __name__ == '__main__':
    nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    tree = Tree()
    tree.build_tree(nodes)
    print tree.travel_by_lev()
    print tree.travel_by_ldr()

    node_find = 4
    ldr_list = tree.travel_by_ldr()
    print ldr_list[ldr_list.index(node_find) + 1]
