def printBoard(Board):
    print(Board['1']+' | '+Board['2']+' | '+Board['3'])
    print("-------------")
    print(Board['4']+' | '+Board['5']+' | '+Board['6'])
    print("-------------")
    print(Board['7']+' | '+Board['8']+' | '+Board['9'])

Board={'1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9'}
player1=input("Enter player 1 name:")
player2=input("Enter player 2 name:")
for i in range(1,10):
    if i%2!=0:
        print()
        printBoard(Board)
        move=input("please enter your move %s:"%(player1))
        Board[move]='x'
        printBoard(Board)
        if (Board['1']=='x' and Board['2']=='x' and Board['3']=='x') or  (Board['1']=='x' and Board['4']=='x' and Board['7']=='x') or (Board['1']=='x' and Board['5']=='x' and Board['9']=='x') or (Board['2']=='x' and Board['5']=='x' and Board['8']=='x') or (Board['3']=='x' and Board['5']=='x' and Board['7']=='x') or (Board['3']=='x' and Board['6']=='x' and Board['9']=='x') :
            print("player 1 wins")
            break
    else:
        print()
        printBoard(Board)
        move=input("please enter your move %s:"%(player2))
        Board[move]='0'
        printBoard(Board)
        if (Board['1']=='0' and Board['2']=='0' and Board['3']=='0') or  (Board['1']=='0' and Board['4']=='0' and Board['7']=='0') or (Board['1']=='0' and Board['5']=='0' and Board['9']=='0') or (Board['2']=='0' and Board['5']=='0' and Board['8']=='0') or (Board['3']=='0' and Board['5']=='0' and Board['7']=='0') or (Board['3']=='0' and Board['6']=='0' and Board['9']=='0') :
            print("player 2 wins")
            break
    
