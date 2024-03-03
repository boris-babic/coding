
#6-1
person = {
    'first name' : 'Zuzka',
    'last name'  : 'Bacovcinova',
    'city'       : 'Vranov',
}
print(f'{person["first name"]} {person["last name"]} byva v {person["city"]}')
#6-2
numbers = {
    'Boris' : '1',
    'Adam'  : '2',
    'Palki' : '3',
    'Pato'  : '4',
    'Harry' : '5'
}
for k, v in numbers.items():
    print(f'{k} ma rad {v}')

#6-3, 6-4
dictionary = {
    'go'   : 'ist',
    'make' : 'robit',
    'run'  : 'bezat',
    'jump' : 'skakat',
}
for k, v in dictionary.items():
    print(k, v, sep='- ')
#6-5
rivers = {
    'nile'      : 'egypt',
    'vah'       : 'slovakia',
    'missisipi' : 'the US',
}

me = {
    'name' : 'Boris',
    'surname' : 'Babic'
}
print(me)
me['age'] = 14
print(me)
school = me.get('school', 'Nechodis na skolu')
print(school)
#6-7
tabita = {
    'first'   : 'Tabita',
    'last'    : 'Mikusova',
    'location': 'Prievidza'
}

sima = {
    'first'   : 'Simona',
    'last'    : 'Hudecova',
    'location': 'Dubnica'
}

pato = {
    'first'   : 'Patrik',
    'last'    : 'Capliar',
    'location': 'Vrutky'
}
people = [tabita, sima, pato]
for person in people:
    print(person ['first'], person['last'], 'ktory byva v obci',person['location'])

#6-9
places = {
    'Boris'  : ['meggy', 'greece', 'ski slopes'],
    'Sima'   : ['Dubnica', 'Klobusince', 'doors'],
    'Tabita' : ['Prievidza', 'kanianka', 'Hradok']
}
for person, place in places.items():
    print(f'{person} likes being in :')
    for i in place:
        print('  ',i)
    print()
        
#6-11
cities = {
    'Ruzomberok' : {
        'country'    : 'Slovakia',
        'population' : 'not a lot',
        'fact'       : 'tha best',
    },
    'London'     : {
        'country'    : 'Uk',
        'population' : 'a fuck ton',
        'fact'       : 'its really old',
    },
    'Kyiv'       : {
        'country'    : 'Ukraine',
        'population' : 'average',
        'fact'       : 'kinda hot in there',
    },
}
for city, item in cities.items():
    print(city + ':')
    for i, j in item.items():
        print(i, j, sep=': ')
    print()
