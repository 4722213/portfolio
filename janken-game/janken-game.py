#coding:utf-8
import random

f = open('test4.txt', 'w')

hands = {1:"グー", 2:"チョキ", 3:"パー"}
win = 0
lose = 0
draw = 0

print("これからじゃんけんを開始します")
while True:
  you = random.randint(1,3)
  me = int(input("グー:1 チョキ:2 パー:3のいずれかを数値で入力してください: ") )

  if(you == me):
    print("あいこです。")
    draw += 1
    a = input("終了しますか？(Y/N): ")
    if a == "y" or a == "Y":
      break
  else:
    print("相手は" + hands[you] + "です。")
    print("あなたは" + hands[me] + "です。")

    if me == 1 and you == 3:
      print("あなたの負けです。")
      lose += 1
    elif me == 2 and you == 1:
      print("あなたの負けです。")
      lose += 1
    elif me == 3 and you == 2:
      print("あなたの負けです。")
      lose += 1
    else:
      print("あなたの勝ちです。")
      win += 1

    a = input("終了しますか？(Y/N): ")
    if a == "y" or a == "Y":
      break

f.write("勝った回数は" + str(win) +"回です。\n")
f.write("負けた回数は" + str(lose) +"回です。\n")
f.write("あいこの回数は" + str(draw) +"回です。")

f.close()

