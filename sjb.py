#-*- coding: utf-8 -*-

import random

player = int(input("请出拳 石头 (1)/ 剪刀 (2)/ 布 (3) : "))

computer = random.randint(1,3)

print("玩家选择的拳头是 %d - 电脑出的拳头是 %d" % (player, computer))

if ((player == 1 and computer == 2) or 
        (player == 2 and computer == 3) or 
        (player == 3 and computer == 1)):
        print("ok,fine! you win")
elif player == computer:
    print("wish you luck next time!!!")
else:
    print("Daddy is here,knee!!!! or die")            
