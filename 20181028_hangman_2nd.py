import random
list_pre = ["apple","banana","fish","peach","pine"]

def hangman(word):
    wrong = 0
    stages = ["",
            "_________           ",
            "|                   ",
            "|        |          ",
            "|        O          ",
            "|       /|\\         ",
            "|       / \\         ",
            ]#stagesは０～６の７ステージ
    rletters = list(word) #rlesttersには答えが入る
    board = ["_"]*len(word) #boardには現状が入る。基本アンダーバー
    win = False
    print("welcome to hangman!")
    while wrong < len(stages) - 1: #stage[6]まではやりますよというもの
        print("\n")
        msg = "char?"
        char = input(msg)
        if char in rletters:#答えの中に回答があるかチェック
            cind =rletters.index(char)#何番目に格納されているか
            board[cind] = char #答えの所に入れる
            rletters[cind] = '$' #indexは最初しかかえさないから
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board: #_がなかったらもう勝でしょということ
            print("you are winner")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("you are loser {}.".format(word))


ran = random.randint(0,4)
hangman(list_pre[ran])
