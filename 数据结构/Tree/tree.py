# coding=utf-8

from node import Node


class Tree:
    def __init__(self):
        self.root = None

    def build_tree(self, nodes_list):
        if nodes_list[0]:
            root = Node(nodes_list[0])
            self.root = root
            nodes = [root]
            id = 1
            while nodes and id < len(nodes_list):
                node = nodes[0]
                node.left = Node(nodes_list[id]) if nodes_list[id] else None
                nodes.append(node.left)
                node.right = Node(nodes_list[id+1]) if nodes_list[id+1] and id < len(nodes_list) - 1 else None
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

    def travel_by_dlr(self):
        # 前序遍历
        def dlr(root, ret):
            if root is None:
                return
            ret.append(root.data)
            dlr(root.left, ret)
            dlr(root.right, ret)
        ret = []
        dlr(self.root, ret)
        return ret

    def travel_by_ldr(self):
        # 中序遍历
        def ldr(root, ret):
            if root is None:
                return
            ldr(root.left, ret)
            ret.append(root.data)
            ldr(root.right, ret)
        ret = []
        ldr(self.root, ret)
        return ret

    def travel_by_lrd(self):
        # 后序遍历
        def lrd(root, ret):
            if root is None:
                return
            lrd(root.left, ret)
            lrd(root.right, ret)
            ret.append(root.data)
        ret = []
        lrd(self.root, ret)
        return ret


if __name__ == '__main__':
    nodes_list = range(1, 10)
    tree = Tree()
    tree.build_tree(nodes_list)
    print '层序遍历: {}'.format(tree.travel_by_lev())
    print '前序遍历: {}'.format(tree.travel_by_dlr())
    print '中序遍历: {}'.format(tree.travel_by_ldr())
    print '后序遍历: {}'.format(tree.travel_by_lrd())
