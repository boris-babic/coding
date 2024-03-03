'''
pizzas = ['al tono', 'basic bitch', 'ew hawaiian', 'mexican']

for pizza in pizzas:
    print(f'I like {pizza} pizza')
print('I really like pizza')

animals = ['cat', 'dogg', 'turtle', 'tortoise']
for animal in animals:
    print(animal)

4-5
x = 1000000
num =[i+1 for i in range(x)]
for i in range(x):
    print(num[i])

print(max(num))
print(min(num))
print(sum(num))

4-6
num =[i*2+1 for i in range(10)]
for i in range(10):
    print(num[i], end=' ')

4-7
triple = [num*3 for num in range(1,11)]
for i in range(10):
    print(triple[i], end = ' ')

4-9
cubes = [i**3 for i in range(1, 11)]
for i in range(10):
    print(cubes[i], end =' ')

list = ['a', 'b', 'c', 'd', 'e', 'f']
print(f'The first 2 items in the list are:{list[:2]}')
print(f'The middle 2 items in the list are:{list[2:4]}')
print(f'The last 2 items in the list are:{list[-2:]}')
'''
buffet = ('cola', 'juice', 'hot dog', 'sprite', 'fanta')
for thing in buffet:
    print(thing)
buffet = ('cola', 'juice', 'lasagna', 'nestea', 'fanta')
for thing in buffet:
    print(thing)

x = 95
y = 103
n = 4 #pocet mocnin
for i in range(x, y+1):
    for j in range(1, n+1):
        print(i**j, end=' ')
    print()