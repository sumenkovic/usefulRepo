#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random

# The quiz data. Keys are states and values are their capitals.
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

# Generate 35 quiz files.
for quizNum in range(35):
#create quiz files and answers
    quizFile = open("capitalsQuiz%s.txt" %(quizNum + 1), 'w')
    answerFile = open("capitalsQuiz%s_answer.txt" %(quizNum + 1), 'w')
#write header for quiz
    quizFile.write("Name:\nDate:\nPeriod:")
    quizFile.write(" " * 20 + "State capital quiz Form %s" %(quizNum +1))
    quizFile.write("\n\n")
#shuffle states as list
    states = list(capitals.keys())
    random.shuffle(states)
#loop through all of states and make question for each
    for questionNum in range(50):
        #right and wrong answers
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
        #writing to quiz files
        quizFile.write("%s. What's the capital of %s?\n" %(questionNum +1, states[questionNum]))
        for i in range(4):
            quizFile.write("    %s. %s\n" %("ABCD"[i], answerOptions[i]))
        quizFile.write("\n")
        #writing to answer file
        answerFile.write("%s. %s\n" %(questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerFile.close()
