import random

heads=0
tails=0
rounds=100


for i in range (rounds):
    n=random.randint(1, 2)
    if n == 1:
        heads=heads+1
        print('heads')
    if n == 2:
        tails=tails+1
        print('tails')


s=heads*100/rounds
d=tails*100/rounds
print('heads: %s'%(s))
print('tails: %d'%(d))
