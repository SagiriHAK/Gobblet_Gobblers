import numpy as np
from copy import deepcopy

from State import State
from Operator import Operator
from Node import Node
from eval import eval
from View import view_state
from pprint import pprint

def _check_win(check):
    for i, elem1 in enumerate(check):
        for j, elem2 in enumerate(check):
            if j == i:
                continue
            for k, elem3 in enumerate(check):
                if k == i or k == j:
                    continue
                if elem1 + elem2 + elem3 == 15:
                    return True
    return False

def pick(state, operator):
    """pick a piece"""
    board_list = state.get_board_list()
    turn, source, _, size = operator.get_all_param()
    if source == -1:
        piece_dict = state.get_piece(turn)
        piece_dict[size] -= 1
        state.set_piece(turn, piece_dict)
    else:
        board_list[source] -= turn * size
        state.set_board_list(board_list)

def is_win(state):
    """decision of victory or defeat"""
    board_list = state.get_board_list()
    negative = [elem + 1 for elem in range(len(board_list)) if board_list[elem] < 0]
    positive = [elem + 1 for elem in range(len(board_list)) if board_list[elem] > 0]
    negative_win = _check_win(negative)
    positive_win = _check_win(positive)
    if negative_win or positive_win:
        return True
    else:
        return False

# def can_put(state, operator):
#     boarders = [1,4]
#     board_list = state.get_board_list()
#     _, _, dist, size = operator.get_all_param()

#     idx = np.searchsorted(boarders, abs(board_list[dist]), side="left") 
#     if idx == 0:
#         return True
#     maximum_piece = 3**idx

#     if maximum_piece < size:
#         return True
#     else:
#         return False

def can_put(state, operator):
    boarders = [1,4]
    board_list = state.get_board_list()
    _, _, dist, size = operator.get_all_param()

    idx = np.searchsorted(boarders, abs(board_list[dist]), side="left") 
    maximum_piece = 3**idx

    if maximum_piece <= size:
        return True
    else:
        return False

def put(state, operator):
    """put a piece"""
    board_list =state.get_board_list()
    turn, source, dist, size = operator.get_all_param()
    if can_put(state, operator):
        # print(turn)
        board_list[dist] += turn*size
        state.set_board_list(board_list)
        return True
    else:
        return False

def move(state:State, operator:Operator):
    pick(state, operator)
    # if is_win(state):
    #     state.set_win(operator.get_turn)
    can_put = put(state, operator)
    # if state is None:
    #     print(state)
    return state
    # if (can_put == False):
    #     print("!!!!!!!!!!!!!!!!!!")
    # # print(operator.get_all_param())
    # # print(state)
    # # print(operator)
    # # print(state.get_board_list())
    # if can_put:
    #     return state
    # else:
    #     return None

# return to source and max_piece
def check_position(state, operator):
    board_list = state.get_board_list()
    turn, _, dist, size = operator.get_all_param()
    turn = -1 if turn == 1 else 1
    movable_piece = []
    boarders = [1,4]
    for i, elem in enumerate(board_list):
        if elem == 0:
            continue

        idx = np.searchsorted(boarders, abs(elem), side="left")
        maximum_piece = 3**idx

        if turn == -1 and elem < 0 or turn == 1 and elem > 0:
            movable_piece.append([i, maximum_piece])

    return movable_piece

def enable_hand(state, movable_piece):
    cand_operator = []
    boarders = [1,4]
    board_list = state.get_board_list()
    for elem in movable_piece:
        for i, piece in enumerate(board_list):
            if i == elem[0]:
                continue

            if piece == 0:
                maximum_piece = 0
            else:
                idx = np.searchsorted(boarders, abs(piece), side="left")
                maximum_piece = 3**idx

            if maximum_piece < elem[1]:
                cand_operator.append([elem[0], i, elem[1]])
    return cand_operator

def min_max_algorithm(tree):
    # define max depth and maximize or minimize
    depth = 4
    is_maximizing = True

    #  if depth bigger than zero then continue loop
    while depth > 0:
        # maximize the score
        if is_maximizing:
            max_eval_dict = dict()
            # scan the leaves what depth match the searching
            # if max chind of parent's Node is not exist then set searching Node to that, else compare to Node what already exist and set bigger to child
            for leaf in tree:
                if leaf.depth == depth and leaf.eval is not None:
                    if max_eval_dict.get(leaf.parent) is None:
                        max_eval_dict[leaf.parent] = leaf
                    else:
                        if max_eval_dict[leaf.parent].eval < leaf.eval:
                            max_eval_dict[leaf.parent] = leaf

            # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1")
            # pprint(max_eval_dict)
            # if len(max_eval_dict) == 1:
            #     for elem in max_eval_dict:
            #         # print(max_eval_dict[elem].operator.get_all_param())
            # set child Node to parent Node
            for parent in max_eval_dict:
                if parent is None:
                    continue
                parent.set_eval(max_eval_dict[parent].eval)
                parent.set_child_node(max_eval_dict[parent])

        # minimize the score
        else:
            min_eval_dict = dict()
            # scan the leaves what depth match the searching
            # if max chind of parent's Node is not exist then set searching Node to that, else compare to Node what already exist and set smaller to child
            for leaf in tree:
                if leaf.depth == depth and leaf.eval is not None:
                    if min_eval_dict.get(leaf.parent) is None:
                        min_eval_dict[leaf.parent] = leaf
                    else:
                        if min_eval_dict[leaf.parent].eval > leaf.eval:
                            min_eval_dict[leaf.parent] = leaf

            # set child Node to parent Node
            for parent in min_eval_dict:
                if parent is None:
                    continue
                parent.set_eval(min_eval_dict[parent].eval)
                parent.set_child_node(min_eval_dict[parent])

        #  decrease depth and toggle maximize and minimize
        depth -= 1
        is_maximizing = False if is_maximizing else True

    best_operator = None
    # make best operator and return that
    for leaf in tree:
        if leaf.depth == 1:
            best_operator = leaf.child.operator
            break

    return best_operator

def calc_child_eval(tree):
    """calculate"""
    for leaf in tree:
        if leaf.depth == 4:
            _tmp = eval(leaf)
            leaf.set_eval(_tmp)

# Node: current state, BEFORE OPERATOR, parent_node, depth
def make_tree(state, operator, max_depth=4):
    open_list = []
    close_list = []
    s1 = Node(state, operator, None, 1)
    open_list.append(s1)
    # cnt = 0
    while len(open_list) != 0:
        node = open_list.pop(0)
        node_depth = node.depth

        if node_depth > max_depth:
            break
        # if cnt >= 20:
        #     break
        movable_piece = check_position(node.state, node.operator)
        # cnt+=1
        turn = node.operator.get_turn()
        # turn = -1 if turn == 1 else 1
        next_turn = 1 if turn == -1 else -1
        rest_piece = node.state.get_piece(next_turn)
        for piece in rest_piece:
            if rest_piece[piece] > 0:
                movable_piece.append([-1,piece])

        cand_operator = enable_hand(node.state, movable_piece)
        for elem in cand_operator:
            _state = deepcopy(node.state)

            # Noneの場合(動かせない場合は)turnは変更しない
            _child_state = move(_state, Operator(next_turn,elem[0],elem[1],elem[2]))
            if _child_state is None:
                _state = deepcopy(node.state)

            # if player or cpu win, set the parent node's reach variable to -1 or 1.
            if _child_state.get_win() == -1 or _child_state.get_win() == 1:
                node.state.set_reach(next_turn)

            open_list.append(
                Node(
                    _child_state,
                    Operator(next_turn,elem[0],elem[1],elem[2]),
                    node,
                    node_depth+1
                )
            )
            # next_turn = 1 if turn == -1 else -1

        close_list.append(node)
    return close_list

# def main():
#     state = State()
#     state.set_board_list([0,0,0,0,0,0,0,0,0])
#     view_state(state)

#     operator = Operator(-1, -1, 3, 9)
#     state = move(state, operator)
#     view_state(state)

#     tree = make_tree(state, Operator(-1, -1, 3, 9))
#     calc_child_eval(tree)
#     best = min_max_algorithm(tree)
#     state = move(state, best)
#     # print(state.get_board_list())
#     # print(best.get_all_param())
#     view_state(state)


# main loop
def main():
    state = State()
    state.set_board_list([0,0,0,0,0,0,0,0,0])
    # print(state.get_board_list())
    view_state(state)
    while True:
        source, dist, size = map(int, input("plase input operator:").split())
        
        operator = Operator(-1, source, dist, size)
        state = move(state, operator)
        # print(state.get_board_list())
        view_state(state)
        if is_win(state):
            print("player win!")
            break

        tree = make_tree(state, Operator(-1, source, dist, size))
        calc_child_eval(tree)
        best = min_max_algorithm(tree)
        state = move(state, best)
        # print(state.get_board_list())
        view_state(state)
        if is_win(state):
            print("cpu win!")
            break

# def main():
#     state = State()
#     state.set_board_list([-6,-2,1,-9,3,9,0,8,0])
#     print(is_win(state))

if __name__ == "__main__":
    main()
