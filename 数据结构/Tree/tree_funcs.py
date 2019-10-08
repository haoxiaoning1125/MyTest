# coding=utf-8

from tree import Tree
from node import Node


def nodes_count(root):
    # 节点个数
    # 递归
    # if root is None:
    #     return 0
    # return 1 + nodes_count(root.left) + nodes_count(root.right)

    # 非递归
    nodes = [root]
    ret = 0
    while nodes:
        ret += 1
        node = nodes.pop(0)
        if node.left:
            nodes.append(node.left)
        if node.right:
            nodes.append(node.right)
    return ret


def leaf_nodes_count(root):
    # 叶节点个数
    # 递归
    # if root is None:
    #     return 0
    # if root.left is None and root.right is None:
    #     return 1
    # return leaf_node_count(root.left) + leaf_node_count(root.right)

    # 非递归
    if root is None:
        return 0
    ret = 0
    nodes = [root]
    while nodes:
        node = nodes.pop(0)
        if node.left is None and node.right is None:
            ret += 1
        if node.left:
            nodes.append(node.left)
        if node.right:
            nodes.append(node.right)
    return ret


def depth(root):
    # 树的深度
    # 递归
    # if root is None:
    #     return 0
    # return max(depth(root.left), depth(root.right)) + 1

    # 非递归
    if root is None:
        return 0
    current_level_count = 1
    next_level_count = 0
    depth = 0
    nodes = [root]
    while nodes:
        node = nodes.pop(0)
        current_level_count -= 1
        if node.left:
            nodes.append(node.left)
            next_level_count += 1
        if node.right:
            nodes.append(node.right)
            next_level_count += 1
        if current_level_count == 0:
            depth += 1
            current_level_count = next_level_count
            next_level_count = 0
    return depth


def nodes_count_of_lev_k(root, k):
    # 第k层节点数
    # 递归
    if root is None or k < 1:
        return 0
    if k == 1:
        return 1
    return nodes_count_of_lev_k(root.left, k - 1) + nodes_count_of_lev_k(root.right, k - 1)


def is_same(root1, root2):
    # 两颗二叉树是否相同
    # 递归
    # if root1 is None and root2 is None:
    #     return True
    # elif root1 is None or root2 is None:
    #     return False
    # if root1.data != root2.data:
    #     return False
    # return is_same(root1.left, root2.left) and is_same(root1.right, root2.right)
    nodes1 = [root1]
    nodes2 = [root2]
    while nodes1 and nodes2:
        node1 = nodes1.pop(0)
        node2 = nodes2.pop(0)
        if node1 is None and node2 is None:
            continue
        elif node1 and node2 and node1.data == node2.data:
            nodes1.append(node1.left)
            nodes1.append(node1.right)
            nodes2.append(node2.left)
            nodes2.append(node2.right)
        else:
            return False
    return True


def is_avl(root):
    # 是否是平衡二叉树
    if root is None:
        return True
    if abs(depth(root.left) - depth(root.right) > 1):
        return False
    return is_avl(root.left) and is_avl(root.right)


def mirror(root):
    # 树的镜像
    # 递归
    if root is None:
        return root
    new_root = Node(root.data)
    new_root.left = mirror(root.right)
    new_root.right = mirror(root.left)
    return new_root


if __name__ == '__main__':
    nodes_list = range(1, 9)
    tree = Tree()
    tree.build_tree(nodes_list)

    print '节点个数: {}'.format(nodes_count(tree.root))
    print '叶节点个数: {}'.format(leaf_nodes_count(tree.root))
    print '深度: {}'.format(depth(tree.root))
    k = 3
    print '第{}层节点数: {}'.format(k, nodes_count_of_lev_k(tree.root, k))
    tree2 = Tree()
    tree2.build_tree(nodes_list[::-1])
    print '树{} 和树{} 相同?: {}'.format(
        tree.travel_by_lev(), tree2.travel_by_lev(), is_same(tree.root, tree2.root)
    )
    print '树{}是平衡二叉树?: {}'.format(tree.travel_by_lev(), is_avl(tree.root))
    tree3 = Tree()
    tree3.build_tree(range(1, 7))
    print 'tree3: {}'.format(tree3.travel_by_lev())
    tree3 = Tree(mirror(tree3.root))
    print 'tree3: {}'.format(tree3.travel_by_lev())
