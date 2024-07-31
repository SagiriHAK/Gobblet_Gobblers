from State import State
from Operator import Operator
from typing import Optional
from Node import Node

def view_piece(state,x):
    board_list=state.get_board_list()
    # print(board_list)
    # board_list=[9,0,0,-8,-6,0,0,1,0]
    RED = '\033[31m'
    BLUE= '\033[34m'
    END = '\033[0m'
    match board_list[x]:
        case 1:
            return RED+"== S =="+END
        case 2|3|4:
            return RED+"== M =="+END
        case 5|6|7|8|9|10|11|12|13|14|15:
            return RED+"== L =="+END
        case -1:
            return BLUE+"== S =="+END
        case -2|-3|-4:
            return BLUE+"== M =="+END
        case -5|-6|-7|-8|-9|-10|-11|-12|-13|-14|-15:
            return BLUE+"== L =="+END

        case 0:
            return "       "#xの場所にコマがなかったら、空欄にしたいから


def view_state(state):
    # board_list=state.get_board_list()
    print("| 7 - - | 0 - - | 5 - - |")
    print("|"+view_piece(state,7)+"|"+view_piece(state,0)+"|"+view_piece(state,5)+"|")
    print("| 2 - - | 4 - - | 6 - - |")
    print("|"+view_piece(state,2)+"|"+view_piece(state,4)+"|"+view_piece(state,6)+"|")
    print("| 3 - - | 8 - - | 1 - - |")
    print("|"+view_piece(state,3)+"|"+view_piece(state,8)+"|"+view_piece(state,1)+"|")
    print("| - - - | - - - | - - - |")
    print("\n")

def main():
    state = State()#test
    #operator = Operator(1, -1, 0, 3)
    view_state(state)

if __name__ == "__main__":
   main()
