#solution with dictionaries
#just like lists but you name the index
people = []
marks = '12345'
with open('y5\python\ziaci.txt') as file:
    subjects = file.readline().split()
    for row in file:
        person = {}
        information = row.strip().split()
        person['Name'] = information[1] + ' ' + information[0]
        for i,subject in enumerate(subjects):
            person[f'{subject}'] = information[i+2]
            #we made a pair name of the subject: mark from that subject
            #example: Matematika: 2
        people.append(person)

best_average = 5

for person in people:
    count, sum = 0, 0
    for key, value in person.items():
        if value in marks:
            count +=1
            sum += int(value)
    average = sum/count
    if average < best_average:
        best_average = average
        best_person = person['Name']
print(f'The person with best average is {best_person} with average of {best_average}')
best_score = 80

for subject in subjects:
    score = 0
    for person in people:
        if person[f'{subject}'] in marks:
            score += int(person[f'{subject}'])
    if score < best_score:
        best_score = score
        best_subject = subject
print(f'Best grades were in {best_subject}')

#solution without dictionaries
people = [] # list of people with their marks
marks = '12345' #achieveable marks
with open('y5\python\ziaci.txt') as file:
    subjects = file.readline().split() # makes a list of all subjects
    for row in file:
#makes a list of a person with name at index 0&1 and the rest are marks
        person = row.strip().split() 
        people.append(person) #adds to the list of people already done

best_average = 5 #worst possible mark
for person in people:
    count, sum = 0, 0 
    for i in range(len(person)): #looping through persons 'profile'
        if str(person[i]) in marks: #if it finds a mark it will count an average
            sum += int(person[i])
            count += 1
    average = sum/count
    if average < best_average:
        best_average = average
        best_person = person[1] + ' ' + person[0]
print(f'The person with best average is {best_person} with average of {best_average}')

best_score = 80 #because we have 16 students and the worst possible marks from a subject would add up to 80
for i in range(len(subjects)): #looping through subjects, current subject will be expressed by its position
    score = 0
    for person in people: #looping through people
        if person[i+2] in marks: # +2 because first 2 spots are names
            score += int(person[i+2])
    if score < best_score:
        best_score = score
        best_subject = subjects[i]
print(f'Best grades were in {best_subject}')