f=open('data.txt')
times=f.read().split()
f.close()
print(times)
total_times=int(times[0])
win_times=int(times[1])
avg_times=int(times[2])
if total_times==0:
	print()
else:
	avg_times=float(win_times)/total_times
