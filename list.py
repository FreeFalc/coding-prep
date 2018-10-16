class Node(object):
    next = None

    def __init__(self, data=None):
        self.data = data


class Linklist(object):
    def __init__(self, node=None):

        if node is None:
            node = Node()
        self.head = node

    def insert(self, item, position=None):
        node = self.head
        new_node = Node(item)
        number = 0
        if position == 0:
            new_node.next = node
            self.head = new_node
            return

        while node.next and position != number:
            prev_node = node
            node = node.next
            number += 1
        if position is not None and position == number:
            new_node.next = node
            prev_node.next = new_node
        else:
            node.next = new_node
        return

    def delete(self, position=None):
        pass

    def iter(self):
        node = self.head

        while node.next is not None:
            yield node.data
            node = node.next

        yield node.data

    def generate(self, fromlist=[]):
        self.head = Node(fromlist[0])

        for i in range(1, len(fromlist)):
            self.insert(fromlist[i])

    def __repr__(self):
        line = ""

        for node in self.iter():
            if line == "":
                line = str(node)
            else:
                line = line + " -> " + str(node)

        return line

    def __len__(self):
        count = 0

        for _ in self.iter():
            count += 1
        return count


if __name__ == "__main__":
    # execute only if run as a script
    a = Linklist(Node(1))
    a.head.next = Node(2)
    a.insert(3)
    a.insert(4)
    b = Linklist()

    b.generate([1, 2, 3, 4, 5])
    print(a)
    print(len(a))
    print(b)
    print(len(b))

