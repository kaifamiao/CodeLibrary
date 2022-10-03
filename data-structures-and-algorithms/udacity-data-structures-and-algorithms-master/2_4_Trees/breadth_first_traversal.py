from collections import deque
from binary_tree import Tree, Node


class BreathFirstTraversal(object):
    @staticmethod
    def traverse(tree):
        queue = deque()
        root = tree.get_root()
        queue.append(root)

        while len(queue) != 0:
            node = queue.popleft()
            print(node.get_value())
            if node.has_left():
                queue.append(node.get_left())
            if node.has_right():
                queue.append(node.get_right())


if __name__ == '__main__':
    tree = Tree("apple")
    tree.get_root().set_left(Node("banana"))
    tree.get_root().set_right(Node("cherry"))
    tree.get_root().get_left().set_left(Node("dates"))
    tree.get_root().get_left().set_right(Node("mangoes"))

    BreathFirstTraversal.traverse(tree)