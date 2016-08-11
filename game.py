from random import randint

import game_global

scores=[0,0]
count=0
if game_global.total_times==0:
	print()
else:
	avg_times=float(game_global.win_times)/game_global.total_times
	print('你已经玩了%d次，赢了%d次，平均%.2f次赢一次')
def game():
	print('you choose what')
	print('1,2,3')
	com_choose = randint(1, 3)
	print(com_choose)
	you_choose = input()
	game_score = int(com_choose) - int(you_choose)
	if game_score != 0:
		scores[0] = scores[0] + 1
	else:
		print()
	print('you save what')
	print('1,2,3')
	com_save = randint(1, 3)
	print(com_save)
	you_save = input()
	game_score = int(com_save) - int(you_save)
	if game_score != 0:
		scores[1] = scores[1] + 1
	else:
		print()
def compare():
	if scores[0] > scores[1]:
		print('you win')
		game_global.win_times=game_global.win_times+1
	elif scores[0] < scores[1]:
		print('you lose')
	else:
		print('equal')
for counts in range(1,3):
	print('这是第%d次玩游戏' % counts)
	game()
while scores[0]==scores[1]:
	count=count+1
	print('start new round,this is the %d time extra match'%count)
	game()
compare()
print(scores)
game_global.total_times=game_global.total_times+1
print(game_global.total_times)
print(game_global.win_times)
print('game over')