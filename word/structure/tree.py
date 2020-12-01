import copy


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeHandle:
    """
    attribute:
        self.white: str
        self.data_root: TreeNode
        self.data_list: list
        # self.data_linked: link

    method:
        self.tree2list(data: TreeNode) -> list
        self.list2tree(data: [list, tuple]) -> TreeNode
        self.pre_order_traversal(data: TreeNode)
        self.in_order_traversal(data: TreeNode)
        self.post_order_traversal(data: TreeNode)

    """

    def __init__(self, white=None):
        self.white = "#" if white is None else white

        # if data_type == "tree":
        #     self.data_root = copy.deepcopy(data)
        #     self.data_list = self.tree2list(data)
        # elif data_type == "list":
        #     self.data_root = copy.deepcopy(data)
        #     self.data_list = self.list2tree(data)

    def tree2list(self, data):
        """

        :param data:
        :return:

        >>> c = TreeHandle(white="#")
        >>> root = c.list2tree([1,2,3,4])
        >>> lit = c.tree2list(root)
        >>> lit
        [1, 2, 3, 4]
        >>> root = c.list2tree([1, 2, "#", 3, 4, "#", 5])
        >>> c.tree2list(root)
        [1, 2, "#", 3, 4, "#", 5]



        """
        deq = [data]
        new_list = list()
        while deq:
            node = deq.pop(0)

            if node == self.white:
                if not deq:
                    return new_list
                new_list.append(self.white)
                continue

            if node:
                new_list.append(node.val)

            if node.left:
                deq.append(node.left)
            else:
                (deq if node.right else list()).append(self.white)

            if node.right:
                deq.append(node.right)
            else:
                (deq if node.left else list()).append(self.white)
        return new_list

    def list2tree(self, data: [list, tuple]) -> TreeNode:
        """

        :param data:
        :return:

        >>> c = TreeHandle().list2tree([1,2,3,4])
        >>> c.val
        1
        >>> c.left.val
        2
        >>> c.right.val
        3
        >>> c.left.left.val
        4
        >>> bool(c.left.right)
        False

        >>> c = TreeHandle()
        >>> root = c.list2tree([1,2,"#", 3, 4, "#",5])
        >>> root.val
        1
        >>> root.left.val
        2
        >>> bool(root.right)
        False
        >>> root.left.left.val, root.left.right.val
        (3, 4)
        >>> root.left.left.right.val
        5

        """
        root = TreeNode(val=data.pop(0))
        stack = [root]

        while data:
            node = stack.pop(0)

            cur_val = data.pop(0)
            if cur_val == self.white:
                pass
            else:
                node.left = TreeNode(cur_val)
                stack.append(node.left)
            if data:
                cur_val = data.pop(0)
            else:
                break
            if cur_val == self.white:
                pass
            else:
                node.right = TreeNode(cur_val)
                stack.append(node.right)
        return root


if __name__ == '__main__sd':
    c = TreeHandle()
    root = c.list2tree([1, 2, 3, 4])
    c.tree2list(root)

if __name__ == '__main__':
    import doctest

    doctest.testmod()
