from random import randint

import game_global

match=[0,0]
count=0
print('%s,你已经玩了%d次，赢了%d次，平均%.2f次赢一次'%(game_global.name,game_global.total_times,game_global.win_times,game_global.avg_times))
def game():
	print('you choose what')
	print('1,2,3')
	com_choose = randint(1, 3)
	print(com_choose)
	you_choose = input()
	game_score = int(com_choose) - int(you_choose)
	if game_score != 0:
		match[0] = match[0] + 1
	else:
		print()
	print('you save what')
	print('1,2,3')
	com_save = randint(1, 3)
	print(com_save)
	you_save = input()
	game_score = int(com_save) - int(you_save)
	if game_score != 0:
		match[1] = match[1] + 1
	else:
		print()
def compare():
	if match[0] > match[1]:
		print('you win')
		game_global.win_times=game_global.win_times+1
	elif match[0] < match[1]:
		print('you lose')
	else:
		print('equal')
for counts in range(1,3):
	print('这是第%d次玩游戏' % counts)
	game()
while match[0]==match[1]:
	count=count+1
	print('start new round,this is the %d time extra match'%count)
	game()
compare()
print(match)
game_global.total_times=game_global.total_times+1
game_global.scores[game_global.name] = [str(game_global.win_times), str(game_global.total_times), str(game_global.avg_times)]
result =''
for n in game_global.scores:
	line = n +' ' + ' '.join(game_global.scores[n]) + '\n'
	result += line
f=open('data.txt','w')
f.write(result)
f.close()
print('game over')