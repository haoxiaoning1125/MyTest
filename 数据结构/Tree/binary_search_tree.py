# coding=utf-8
# 二叉查找树

from node import Node
from tree import Tree


class BST(Tree):
    def build_tree(self, nodes_list):
        def add_node(root, node_data):
            if node_data < root.data:
                if root.left is None:
                    root.left = Node(node_data)
                else:
                    add_node(root.left, node_data)
            else:
                if root.right is None:
                    root.right = Node(node_data)
                else:
                    add_node(root.right, node_data)

        if nodes_list[0]:
            root = Node(nodes_list[0])
            self.root = root
            for node_data in nodes_list[1:]:
                add_node(root, node_data)

    def search(self, data):
        def search_(root, data):
            r_data = root.data
            if r_data == data:
                print '{} finded!'.format(data)
                return
            elif r_data < data:
                if root.right is not None:
                    search_(root.right, data)
                else:
                    print 'not find.'
                    return
            else:
                if root.left is not None:
                    search_(root.left, data)
                else:
                    print 'not find.'
                    return

        search_(self.root, data)


if __name__ == '__main__':
    nodes_list = [21, 28, 14, 32, 25, 18, 11, 30, 29, 15, 5, 12, 23, 27, 37]
    bst = BST()
    bst.build_tree(nodes_list)
    print bst.travel_by_lev()
    bst.search(27)
    bst.search(1010)
