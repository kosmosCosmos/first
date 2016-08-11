from random import randint
scores=[0,0]
count=0
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
	you_save = input()
	com_save = randint(1, 3)
	print(com_choose)
	game_score = int(com_save) - int(you_save)
	if game_score != 0:
		print()
	else:
		scores[1] = scores[1] + 1
	if scores[0] > scores[1]:
		print('you lose')
	else:
		print('you win')
for counts in range(1,3):
	game()
while scores[0]==scores[1]:
	print('equal')
	count=count+1
	print('start new round,this is the %d time extra match'%count)
	game()
print('game over')