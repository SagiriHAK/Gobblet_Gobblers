class Node(object):
    def __init__(self, state, operator, parent_node, depth) -> None:
        self.state = state
        self.operator = operator
        self.parent = parent_node
        self.depth = depth
        self.eval = None

    def set_eval(self, eval):
        self.eval = eval

    def set_child_node(self, child):
        self.child = child
