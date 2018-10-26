class Node(object):
    left = None
    right = None

    def __init__(self, data=None):
        self.value = data


class BsTree(object):
    length = 0
    root = None

    def __init__(self, data=None):
        self.root = Node(data)

    def insert(self, value, curr_node=None):
        new_node = Node(value)
        if not curr_node:
            curr_node = self.root
        if curr_node.value:
            if value < curr_node.value:
                if curr_node.left:
                    self.insert(value, curr_node.left)
                else:
                    curr_node.left = new_node
            elif value > curr_node.value:
                if curr_node.right:
                    self.insert(value, curr_node.right)
                else:
                    curr_node.right = new_node
            else:
                print("Insertion error")

    def search(self, value, curr_node=None, path=None):
        if not path:
            path = []

        if not curr_node:
            curr_node = self.root

        if value == curr_node.value:
            path.append(curr_node.value)
            return curr_node, path

        elif curr_node.left and value < curr_node.value:
            path.append(curr_node.value)
            return self.search(value, curr_node.left, path)

        elif curr_node.right and value > curr_node.value:
            path.append(curr_node.value)
            return self.search(value, curr_node.right, path)

        else:
            return None, None

    def delete(self, value, curr_node=None):
        is_root = False
        if not curr_node:
            is_root = True
            curr_node = self.root

        if value == curr_node.value:
            if not curr_node.left or not curr_node.right:
                new_node = curr_node.left or curr_node.right

            elif not curr_node.left and curr_node.right:
                new_node = None

            else:
                new_node = self.find_sucs(curr_node)
                new_node.left = curr_node.left
                new_node.right = curr_node.right

            if is_root:
                self.root = new_node

            return True, new_node

        elif value < curr_node.value:
            result, new_node = self.delete(value, curr_node.left)
            if result:
                curr_node.left = new_node

        else:
            result, new_node = self.delete(value, curr_node.right)
            if result:
                curr_node.right = new_node

        return False, None

    def find_sucs(self, node):
        prev_node = node
        next_node = node.right
        while next_node.left:
            prev_node = next_node
            next_node = next_node.left

        if next_node.right:
            n_right = next_node.right

        else:
            n_right = None

        if prev_node == node:
            prev_node.right = n_right

        else:
            prev_node.left = n_right

        return next_node

    def in_traversal(self, node=None):
        data = []
        if not node:
            node = self.root

        if node.left:
            data = self.in_traversal(node.left)

        data.append(node.value)

        if node.right:
            data = data + self.in_traversal(node.right)

        return data

    def post_traversal(self, node=None):
        data = []
        if not node:
            node = self.root

        if node.left:
            data = self.post_traversal(node.left)

        if node.right:
            data = data + self.post_traversal(node.right)

        data.append(node.value)
        return data

    def pre_traversal(self, node=None):
        data = []
        if not node:
            node = self.root

        data.append(node.value)

        if node.left:
            data = data + self.pre_traversal(node.left)

        if node.right:
            data = data + self.pre_traversal(node.right)

        return data

    def inline_traversal(self):
        stack = []
        result = []
        node = self.root
        stack.append(node)
        while stack:
            node = stack.pop(0)
            result.append(node.value)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return result


if __name__ == "__main__":
    new_tree = BsTree(10)
    #
    #           10
    #     4              17
    #  2     6       13      20
    # 1 3   5 8    12  15  18  22
    #
    new_tree.insert(4), new_tree.insert(17)
    new_tree.insert(2), new_tree.insert(6), new_tree.insert(13), new_tree.insert(20)
    new_tree.insert(1), new_tree.insert(3), new_tree.insert(5), new_tree.insert(8)
    new_tree.insert(12), new_tree.insert(15), new_tree.insert(18), new_tree.insert(22)

    node, arr = new_tree.search(2)
    print(arr)

    print("in", new_tree.in_traversal())
    print("pre:", new_tree.pre_traversal())
    print("post:", new_tree.post_traversal())
    print("inline:", new_tree.inline_traversal())
    # new_tree.delete(15)
    # new_tree.delete(10)
    # print("in", new_tree.in_traversal())
