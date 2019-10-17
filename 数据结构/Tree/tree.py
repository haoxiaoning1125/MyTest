# coding=utf-8
# 树

from node import Node


class Tree:
    def __init__(self, root=None):
        self.root = root

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
                # len(nodes_list) - 1 在前
                node.right = Node(nodes_list[id+1]) if id < len(nodes_list) - 1 and nodes_list[id+1] else None
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
                node = nodes.pop(0)
                if node is None:
                    ret.append(None)
                    continue
                ret.append(node.data)
                nodes.append(node.left)
                nodes.append(node.right)
        return ret

    def travel_by_dlr(self):
        # 前序遍历, 递归
        def dlr(root, ret):
            if root is None:
                # ret.append(None)
                return
            ret.append(root.data)
            dlr(root.left, ret)
            dlr(root.right, ret)
        ret = []
        dlr(self.root, ret)
        return ret

    def travel_by_dlr_(self):
        # 前序遍历, 非递归
        # 右节点先进栈
        if self.root is None:
            return []
        stack = [self.root]
        ret = []
        while stack:
            node = stack.pop()
            ret.append(node.data)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return ret

    def travel_by_ldr(self):
        # 中序遍历, 递归
        def ldr(root, ret):
            if root is None:
                # ret.append(None)
                return
            ldr(root.left, ret)
            ret.append(root.data)
            ldr(root.right, ret)
        ret = []
        ldr(self.root, ret)
        return ret

    def travel_by_ldr_(self):
        # 中序遍历, 非递归
        # 根节点所有左节点入栈 -> 输出栈顶元素 -> 处理栈顶元素的右子树
        if self.root is None:
            return []
        stack = []
        node = self.root
        ret = []
        while node is not None or stack:
            while node is not None:
                stack.append(node)
                node = node.left
            if stack:
                node = stack.pop()
                ret.append(node.data)
                node = node.right
        return ret

    def travel_by_lrd(self):
        # 后序遍历, 递归
        def lrd(root, ret):
            if root is None:
                # ret.append(None)
                return
            lrd(root.left, ret)
            lrd(root.right, ret)
            ret.append(root.data)
        ret = []
        lrd(self.root, ret)
        return ret

    def travel_by_lrd_(self):
        # 后序遍历, 非递归
        # 双栈法
        if self.root is None:
            return []
        stack1 = [self.root]  # 保存树节点
        ret = []  # 保存后序遍历的结果
        while stack1:
            node = stack1.pop()
            # if node is None:
            #     continue
            ret.append(node.data)
            # stack1.append(node.left)
            # stack1.append(node.right)
            if node.left is not None:
                stack1.append(node.left)
            if node.right is not None:
                stack1.append(node.right)
        return ret[::-1]


if __name__ == '__main__':
    nodes_list = [1, None, 2]
    tree = Tree()
    tree.build_tree(nodes_list)
    print '层序遍历: {}'.format(tree.travel_by_lev())
    print '-' * 35

    print '递归'
    print '前序遍历: {}'.format(tree.travel_by_dlr())
    print '中序遍历: {}'.format(tree.travel_by_ldr())
    print '后序遍历: {}'.format(tree.travel_by_lrd())
    print '-' * 35

    print '非递归'
    print '前序遍历: {}'.format(tree.travel_by_dlr_())
    print '中序遍历: {}'.format(tree.travel_by_ldr_())
    print '后序遍历: {}'.format(tree.travel_by_lrd_())
