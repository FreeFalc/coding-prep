"""
Given BST f ex
    4
  2   5
 1 3   6
transform (inplace) it to double linked list based on inorder traversal
1 <-> 2 <-> 3 <-> 5 <-> 6
"""

import tree


class BST(tree.BsTree):
    tmp_result = [None]
    tail = None

    def transform(self, cnode=None):

        if not cnode:
            cnode = self.root
        if cnode.left:
            self.transform(cnode.left)

        prev_node = self.tmp_result.pop()

        if prev_node:
            prev_node.right = cnode
        else:
            self.root = cnode

        cnode.left = prev_node
        self.tmp_result.append(cnode)

        if cnode.right:
            self.transform(cnode.right)
        else:
            self.tail = cnode

    def listtraversal(self):
        node = self.root
        result = []
        while node:
            if node.right:
                r_val = node.right.value
            else:
                r_val = None
            if node.left:
                l_val = node.left.value
            else:
                l_val = None
            t_result = [l_val, node.value, r_val]
            result.append(t_result)
            node = node.right
            print(t_result)
        return result


if __name__ == "__main__":
    mytree = BST(4)
    mytree.insert(2), mytree.insert(5)
    mytree.insert(1), mytree.insert(3), mytree.insert(6)
    mytree.transform()
    print(mytree.listtraversal())
    print(mytree.root.value)
    print(mytree.tail.value)
