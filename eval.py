import numpy as np

def eval(node):
  state = node.state
  operator = node.operator
  board_list = state.get_board_list()#現在の盤面に配置しているコマのリスト
  _, _, dist, size = operator.get_all_param()

  eval = 0
  ## コマの大きさ
  size_eval = 0
  size_eval_x=1
  ## 角
  kado_eval=0
  kado_eval_x=5
  ## 中央
  center_eval=0
  center_eval_x=5
  ##　盤上で動かせるコマの数
  move_available=0
  move_available_x=10
  ##　リーチ
  reach_eval=0
  reach_eval_x=100
  ## 勝利
  win_eval = 0
  win_eval_x = 100000
  ## 妨害
  bougai_eval=0
  bougai_eval_x=500

  #コマの大きさに基づく評価ポイント
  size_eval = size

  # コマの角に基づく評価ポイント
  if dist in [1, 3, 5, 7]:
    kado_eval += kado_eval_x

  # コマの真ん中に基づく評価ポイント
  if dist in [4]:
    center_eval += center_eval_x

  # 盤上で動かせるコマの数に基づく評価ポイント
  for x, piece in enumerate(board_list):
      if piece > 0:
        move_available += move_available_x
        if x in [1,3,5,7]:
          kado_eval += 1
      elif piece < 0:
        move_available -= move_available_x

  # リーチに基づく評価ポイント
  board2=[0 for i in range(10)]
  for x in range(0,9):
    board2[x+1]=board_list[x]

  for x in range(1,10):
    for y in range(1,10):
      if(x==y):
        continue
      else:
        if((board2[x]<0 and board2[y]<0)):#x,yの場所に配置されているコマが同チームであるなら
          reach=15 - (x + y) #リーチ判定関数
          if ((reach != x) and (reach != y) and (1<=reach<=9)):#リーチであるならば
            reach_eval-=reach_eval_x
          if dist+1 in [reach, x, y]:
            bougai_eval += bougai_eval_x
        elif((board2[x]>0 and board2[y]>0)):#x,yの場所に配置されているコマが同チームであるなら
          reach=15 - (x + y) #リーチ判定関数
          if ((reach != x) and (reach != y) and (1<=reach) and (reach<=9)):#リーチであるならば
            reach_eval+=reach_eval_x

  # 勝利に基づく評価ポイント
  if node.win in [-1, 1]:
    win_eval = win_eval_x*node.win

  return size_eval + reach_eval + move_available + kado_eval + center_eval + win_eval + bougai_eval
