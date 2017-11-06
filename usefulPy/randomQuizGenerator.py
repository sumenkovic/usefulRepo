#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random,pprint

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for i in range(35):
    questFile = open('capitalsQuestion%s.txt' %(i+1), 'w')
    answerFile = open('capitalAnswer%s.txt' %(i+1), 'w')
    questFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    questFile.write((' ' * 20) + 'States Capitals Quiz (Form %s)' %(i+1))
    questFile.write('\n\n')

    states = list(capitals.keys())
    random.shuffle(states)
    for i in range(50):
        correctAnswer = capitals[states[i]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        questFile.write('%s. What is the capital of %s?\n' %(i+1,states[i]))
        for j in range(4):
            questFile.write('     %s. %s\n' %('ABCD'[j],answerOptions[j]))
        questFile.write('\n')

        answerFile.write('%s. %s\n' % (i + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
        questFile.close()
        answerFile.close()
