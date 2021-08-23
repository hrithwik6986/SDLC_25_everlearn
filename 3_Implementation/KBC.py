import json
import random
import time


def helpline(optionsList, indexAnswer):
    while True:
        newList = random.sample(optionsList, 2)
        if optionsList[indexAnswer] in newList:
            return newList


def displayScore(lives, score, helpLines):
    print("\n")
    print("Lives Left : ", lives)
    print("Helpline Left : ", helpLines)
    print("Score : ", score)
    print("\n")
    time.sleep(1)
# opening all the files which contain questions and answers


def gamePlay():
    def displayCorrect():
        return optionsDict[question][answersDict[question]]

    with open("data/questions.json") as file:
        data = file.read()
        questionsDict = json.loads(data)
    with open("data/options.json") as file:
        data = file.read()
        optionsDict = json.loads(data)
    with open("data/answers.json") as file:
        data = file.read()
        answersDict = json.loads(data)
    with open("data/rewards.json") as file:
        data = file.read()
        rewardsDict = json.loads(data)
    print("Welcome to Kaun Banega Crorepati!\n")
    print('''Rules:
    You will get 3 lives and a 5050 helpline
    To use the helpline you have to type 5050
    For ever correct answer your score is increased
    For ever incorrect answer a life is deducted
    If you quit in between you can take money home to quit type 'quit'
    If you loose all your lives you Lose! and you can take half of the money home.
    If you answer all the questions correctly you Win!\n''')
    user = input("Enter 'exit' to exit or enter anyting else to play : ")
    if user.lower() == 'exit':
        exit()
    print("\n")
    lives = 3
    helpLines = 1
    score = 0
    displayScore(lives, score, helpLines)
    for index, question in enumerate(questionsDict, start=1):
        if lives == 0:
            print("You Lost!")
            print('You can take ' + str(int(score/2)) + ' Rupees home!')
            exit()
        print(str(index) + ". " + questionsDict[question] + '\n')
        for num, option in enumerate(optionsDict[question], start=1):
            print(str(num) + ". " + str(option))
        print('\n')
        userAnswer = input("Answer : ")
        if userAnswer == 'quit':
            print('You are a Quitter!')
            print('You can take ' + str(int(score)) + ' Rupees home!')
            exit()
        else:
            userAnswer = int(userAnswer)
            if userAnswer == 'quit':
                print('You are a Quitter!')
                print('You can take ' + str(int(score)) + ' Rupees home!')
                exit()
            else:
                userAnswer = int(userAnswer)
        if userAnswer == 5050:
            if helpLines > 0:
                helpLines = 0
                newOptions = helpline(
                    optionsDict[question], answersDict[question])
                print('\n')
                for i, opt in enumerate(newOptions, start=1):
                    print(str(i) + ". " + opt)
                print('\n')
                userAnswer = int(input("Answer : "))
                if userAnswer == 'quit':
                    print('You are a Quitter!')
                    print('You can take ' + str(int(score)) + ' Rupees home!')
                    exit()
                else:
                    userAnswer = int(userAnswer)
                print('\n')
                if userAnswer < 3:
                    if newOptions[userAnswer-1] == displayCorrect():
                        print('Correct!')
                        score = score + rewardsDict[question]
                        displayScore(lives, score, helpLines)
                    else:
                        print('Incorrect!')
                        print('Correct answer : ', displayCorrect())
                        lives = lives - 1
                        displayScore(lives, score, helpLines)
                else:
                    print('Incorrect!')
                    print('Correct answer : ', displayCorrect())
                    lives = lives - 1
                    displayScore(lives, score, helpLines)
            else:
                print('Sorry! You have Already used the 50-50 HelpLine!')
                userAnswer = int(input("Answer : "))
                if userAnswer == 'quit':
                    print('You are a Quitter!')
                    print('You can take ' + str(int(score)) + ' Rupees home!')
                    exit()
                else:
                    userAnswer = int(userAnswer)
                if answersDict[question] == userAnswer - 1:
                    print("Correct!")
                    score = score + rewardsDict[question]
                    displayScore(lives, score, helpLines)
                else:
                    print('Incorrect!')
                    print('Correct answer : ', displayCorrect())
                    lives = lives - 1
                    displayScore(lives, score, helpLines)
        else:
            if answersDict[question] == userAnswer - 1:
                print("Correct!")
                score = score + rewardsDict[question]
                displayScore(lives, score, helpLines)
            else:
                print('Incorrect!')
                print('Correct answer : ', displayCorrect())
                lives = lives - 1
                displayScore(lives, score, helpLines)
    print('You Won!')
    print('You can take ' + str(int(score)) + ' Rupees home!')
    print('Thankyou for playing!')
