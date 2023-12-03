import random


capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'NewMexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'WestVirginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
for testnum in range(35):
    test = open('test%s.txt' % (testnum + 1), 'w')
    key = open('key%s.txt' % (testnum + 1), 'w')

    test.write('name:\n\ncode:\n\n')
    test.write('State Capitals Quiz (Form %s)\n\n' % (testnum + 1))

    states = list(capitals.keys())
    random.shuffle(states)

    for questionnum in range(50):
        correctanswer = capitals[states[questionnum]]
        wronganswers = list(capitals.values())
        wronganswers.remove(correctanswer)
        wronganswers = random.sample(wronganswers, 3)
        answers = wronganswers + [correctanswer]
        random.shuffle(answers)

        test.write('%s. What is the capital of %s?\n' % (questionnum + 1, states[questionnum]))
        for i in range(4):
            test.write('%s. %s\n' % ('ABCD'[i], answers[i]))

        key.write('%s. %s\n' % (questionnum + 1, 'ABCD'[answers.index(correctanswer)]))

    test.close()
    key.close()