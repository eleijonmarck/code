import sched
import time
from os import system

s = sched.scheduler(time.time, time.sleep)
a = ['Jumping jacks','Wall sit','Push-up','Abdominal crunch','Step up onto chair','Squat','Triceps dip on chair','Plank','High knees running in place','Lunge','Push up and rotation','Side plank']
i=0

def do_something(sc,i):
	if (i > 11):
		quit()
	system ('say ' + a[i])
	sc.enter(30, 1, do_something, (sc,i+1))

s.enter(1, 1, do_something, (s,i))
s.run()

