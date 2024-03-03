file = 'twain.txt'
dictionary = {}
def dvojice(file_name):
    with open(file_name) as file:
        text = file.read()
    for i in range(len(text)-1):
        if text[i:i+2] in dictionary.keys():
            dictionary[text[i:i+2]] +=1
        else:
            dictionary[text[i:i+2]] =1
    for keys, values in reversed(sorted(dictionary.items(), key= lambda x: x[1])):
        print(f'{repr(keys)} je {values} krat')
            
dvojice(file)
