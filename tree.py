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

    def delete(self, value, node=None ):
        pass

    def in_traversal(self, node):
        data = []
        if node:
            data = self.in_traversal(node.left)
            data.append(node.value)
            data = data + self.in_traversal(node.right)
        return data

    def post_traversal(self, node):
        data = []
        if node:
            data = self.post_traversal(node.left)
            data = data + self.post_traversal(node.right)
            data.append(node.value)
        return data

    def pre_traversal(self, node):
        data = []
        if node:
            data.append(node.value)
            data = data + self.pre_traversal(node.left)
            data = data + self.pre_traversal(node.right)
        return data


if __name__ == "__main__":
    new_tree = BsTree(10)
    # new_tree.root.left = Node(4)
    # new_tree.root.right = Node(17)
    # new_tree.root.left.left = Node(2)
    # new_tree.root.left.right = Node(5)
    # new_tree.root.right.left = Node(15)
    # new_tree.root.right.right = Node(20)
    new_tree.insert(4)
    new_tree.insert(17)
    new_tree.insert(2)
    new_tree.insert(5)
    new_tree.insert(15)
    new_tree.insert(20)
    new_tree.insert(4)

    node, arr = new_tree.search(2)
    print(arr)
    print("in", new_tree.in_traversal(new_tree.root))
    print("pre:", new_tree.pre_traversal(new_tree.root))
    print("post:", new_tree.post_traversal(new_tree.root))



