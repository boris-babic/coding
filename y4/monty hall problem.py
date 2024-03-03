import random
import time

win=0
loose=0
cmpt=0
rounds=10000000

for k in range(0,rounds):
    doors=["car", "goat", "goat"]
    cmpt=cmpt+1
    
    random.shuffle(doors)
    
    n=random.randrange(3)
    if doors[n]  == "car":
        loose=loose+1
        print("goat")
    if doors[n] == "goat":
        win=win+1
        print("new car")

s=win*100.0/rounds
d=loose*100.0/rounds

print("#########RESULTS#########")
print("percent of success: %s" %(s))
print("percent of fail: %d" %(d))
