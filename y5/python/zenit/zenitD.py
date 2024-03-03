answers = []
number = input()
for i in range(int(number)):
    x = input()
    reversed_binary = f'{int(x):032b}'[::-1]
    answers.append(int(reversed_binary, base=2))
    
for i in answers:
    print(i)