def eval(node):
    state=node.state
    board_list=state.get_board_list()#現在の盤面に配置しているコマのリスト
    eval=0

    size_eval=0
    size_eval_x=1
    for x in range (0,9):#コマの大きさに基づくポイント
        if(board_list[x]==1|board_list[x]==-1):#小
            size_eval=size_eval+1*size_eval_x

        elif(2<=board_list[x]<=4|-4<=board_list[x]<=-2):#中
            size_eval=size_eval+2*size_eval_x

        elif(5<=board_list[x]<=15|-15<=board_list[x]<=-5):#大
            size_eval=size_eval+3*size_eval_x
        else:
            continue#コマがない

    kado_eval=0
    kado_eval_x=1#角の係数
    move_available=0
    move_available_x=1
    for x in range (0,9):
        if(board_list[x]!=0):
            move_available+=move_available_x#盤面上で動かせる数
        if(x==7|x==5|x==3|x==1):
            kado_eval+=1*kado_eval_x
    move_available+=(len(state.get_player_piece())+len(state.get_cpu_piece()))*move_available_x

    board2=[0 for i in range(10)]
    reach_eval=0
    reach_eval_x=1#リーチポイント係数
    for x in range(0,9):
      board2[x+1]=board_list[x]

    for x in range(1,10):
      for y in range(1,10):
        if(x==y):
          continue
        else:
          if((board2[x]<0 & board2[y]<0) | (board2[x]>0 & board2[y]>0)):#x,yの場所に配置されているコマが同チームであるなら
            reach=15 - (x + y) #リーチ判定関数
            if ((reach != x) & (reach != y) & (1<=reach) & (reach<=9)):#リーチであるならば
              reach_eval+=reach_eval_x
          else:
            continue

    eval=size_eval+reach_eval+move_available+kado_eval

    return eval
