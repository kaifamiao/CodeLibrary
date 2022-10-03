from collections import deque
from binary_tree import Tree, Node

class State(object):
    def __init__(self, node):
        self.node = node
        self.visited_left = False
        self.visited_right = False


class DepthFirstTraversal(object):
    @staticmethod
    def pre_order(tree):
        stack = deque()
        node = tree.get_root()
        state = State(node)
        stack.append(state)
        print(node.get_value())

        while node is not None:
            if node.has_left() and not state.visited_left:
                state.visited_left = True
                node = node.get_left()
                state = State(node)
                stack.append(state)
                print(node.get_value())
            elif node.has_right() and not state.visited_right:
                state.visited_right = True
                node = node.get_right()
                state = State(node)
                stack.append(state)
                print(node.get_value())
            else:
                stack.pop()
                if len(stack) > 0:
                    state = stack[-1]
                    node = state.node
                else:
                    node = None
    
    @staticmethod
    def post_order(tree):
        stack = deque()
        node = tree.get_root()
        state = State(node)
        stack.append(state)

        while node is not None:
            if node.has_left() and not state.visited_left:
                state.visited_left = True
                node = node.get_left()
                state = State(node)
                stack.append(state)
            elif node.has_right() and not state.visited_right:
                state.visited_right = True
                node = node.get_right()
                state = State(node)
                stack.append(state)
            else:
                last = stack.pop()
                print(last.node.get_value())
                if len(stack) > 0:
                    state = stack[-1]
                    node = state.node
                else:
                    node = None
    
    @staticmethod
    def in_order(tree):
        stack = deque()
        node = tree.get_root()
        state = State(node)
        stack.append(state)

        while node is not None:
            if node.has_left() and not state.visited_left:
                state.visited_left = True
                node = node.get_left()
                state = State(node)
                stack.append(state)
            elif node.has_right() and not state.visited_right:
                state.visited_right = True
                node = node.get_right()
                state = State(node)
                stack.append(state)
            else:
                last = stack.pop()
                last_node = last.node
                if not last_node.has_left() and not last_node.has_right():
                    print(last_node.get_value())
                if len(stack) > 0:
                    state = stack[-1]
                    node = state.node
                    if not state.visited_right:
                        print(node.get_value())
                else:
                    node = None


if __name__ == '__main__':
    tree = Tree("apple")
    tree.get_root().set_left(Node("banana"))
    tree.get_root().set_right(Node("cherry"))
    tree.get_root().get_left().set_left(Node("dates"))
    tree.get_root().get_left().set_right(Node("mangoes"))

    print('Pre-Order Traversal:')
    DepthFirstTraversal.pre_order(tree)
    print('\nIn-Order Traversal:')
    DepthFirstTraversal.in_order(tree)
    print('\nPost-Order Traversal:')
    DepthFirstTraversal.post_order(tree)
