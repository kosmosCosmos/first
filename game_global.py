f=open('data.txt')
lines=f.readlines()
scores={}
print('请输入名字')
name=input()
for l in lines:
	s=l.split()
	scores[s[0]] = s[1:]
score=scores.get(name)
if score==None:
	score=[0,0,0]
total_times=int(score[0])
win_times=int(score[1])
avg_times=float(score[2])
if total_times==0:
	print()
else:
	avg_times=float(win_times)/total_times

