#!/usr/bin/python3
# portQuiz.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random

# The quiz data. Keys are ports and values are their service.
ports = {'20-21': 'FTP',
         '22': 'SSH',
         '23': 'Telnet',
         '25': 'SMTP',
         '42': 'WINS',
         '53': 'DNS',
         '80 8080': 'HTTP',
         '88': 'Kerberos',
         '110': 'POP3',
         '111': 'PortMapper-Linux',
         '123': 'NTP',
         '135': 'RPC-DCOM',
         '139': 'SMB',
         '143': 'IMAP',
         '161-162': 'SNMP',
         '389': 'LDAP',
         '445': 'CIFS',
         '514': 'Syslog',
         '636': 'Secure LDAP',
         '1080': 'Socks5',
         '1241': 'Nessus Server',
         '1433-1434': 'SQL Server',
         '1494 2598': 'Citrix Applications',
         '1521': 'Oracle Listener',
         '2512 2513': 'Citrix Management',
         '3389': 'RDP',
         '6662 6667': 'IRC',
        }

# Generate 5 quiz files or as many as you like.
for quizNum in range(5):
    # Create the quiz and answer key files.
    quizFile = open('portsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('portsquiz_answers%s.txt' % (quizNum + 1), 'w')

    # Write out the header for the quiz
    quizFile.write('Name:\n\nDate:\n\n')
    quizFile.write((' ' * 20) + 'Ports Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    # Shuffle the order of the states.
    services = list(ports.keys())
    random.shuffle(services)

# Loop through all 27 ports, making a question for each.
    for questionNum in range(27):
        # Get right and wrong answers.
        correctAnswer = ports[services[questionNum]]
        wrongAnswers = list(ports.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # Write the question and the answer options to the quiz file.
        quizFile.write('%s. What service operates on port %s?\n' %
                       (questionNum + 1, services[questionNum]))
        for i in range(4):
            quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        # Write the answer key to a file.
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[
            answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()
