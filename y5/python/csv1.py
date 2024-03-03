import csv

def date_converter(date):
    return f"{int(date[:date.find('.')]):02d}.{int(date[date.find('.')+1:-5]):02d}.{date[-4:]}"
'''
file = open('naklady.csv', encoding='utf-8-sig')
dictionary = {}
months = [int(0)] * 12
months_dictionary = {}
for row in file:
    date, value = row.strip().split()
    dictionary[f'{date}'] = float(value[:-1])
    months[int(date[date.find('.')+1:-5])-1] += float(value[:-1])


dictionary_by_month = dict(sorted(dictionary.items(), key=lambda x: int(x[0][x[0].find('.')+1:-5])))
dictionary_by_value = dict(sorted(dictionary.items(), key=lambda x: x[1]))

for key, value in dictionary_by_month.items():
    print(key, value)
for key, value in dictionary_by_value.items():
    print(key, value)


for index, value in enumerate(months):
    months_dictionary[f'{index+1}'] = round(value, 2)
print(months_dictionary)
'''
print(date_converter('1.9.2019'))