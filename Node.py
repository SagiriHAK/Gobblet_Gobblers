class Node(object):
    def __init__(self, state, operator, parent_node, depth, win=0) -> None:
        self.state = state
        self.operator = operator
        self.parent = parent_node
        self.depth = depth
        self.win = win
        self.eval = None

    def set_eval(self, eval):
        self.eval = eval

    def set_child_node(self, child):
        self.child = child

    def set_win(self, win):
        self.win = win

    def get_win(self):
        return self.win
