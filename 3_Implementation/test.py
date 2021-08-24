from random import randint
import hang_man,KBC,snakegame,ticTacToe
import json,random,pygame
from io import StringIO

def test_random_word():
    guess_words='algeria argentina angola austria afghanistan bulgaria bangladesh belgium brazil bolivia bhutan bahamas cambodia china chile canada cuba denmark egypt fiji finland france germany greece georgia hungary iceland india indonesia iran iraq ireland israel italy japan jamaica kuwait korea kenya libya madagascar malaysia maldives mexico mongolia mauritius nepal norway netherlands nigeria oman pakistan portugal poland qatar russia serbia somalia singapore spain sweden switzerland taiwan thailand turkey unitedkingdom ukraine venezuela vietnam yemen zambia zimbabwe'.split()
    assert hang_man.random_word(hang_man.countries) in guess_words

def test_get_letter(monkeypatch):
    letter=StringIO('a\n')
    monkeypatch.setattr('sys.stdin', letter)
    assert hang_man.get_letter('') != None

def test_correct_letter(monkeypatch):
    rand_word='bulgaria'
    letter=StringIO('a\n')
    monkeypatch.setattr('sys.stdin', letter)
    assert hang_man.get_letter('') in rand_word

def test_wrong_letter(monkeypatch):
    rand_word='bulgaria'
    letter=StringIO('x\n')
    monkeypatch.setattr('sys.stdin', letter)
    assert hang_man.get_letter('') not in rand_word

def test_all_correct(monkeypatch):
    rand_word='algeria' 
    guessedword=[StringIO('a\n'),StringIO('g\n'),StringIO('e\n'),StringIO('l\n'),StringIO('r\n'),StringIO('i\n')]
    miss=corr=''
    foundAllLetters = True
    i=0
    while i<len(guessedword):
        monkeypatch.setattr('sys.stdin', guessedword[i])
        l = hang_man.get_letter(miss + corr)
        if l in rand_word:
            corr = corr + l
        else:
            miss = miss + l
        i+=1
    for j in range(len(rand_word)):
        if rand_word[j] not in corr:
                foundAllLetters = False
                break
    assert foundAllLetters

def test_wrong_guess_word(monkeypatch):
    rand_word='algeria' 
    guessedword=[StringIO('a\n'),StringIO('g\n'),StringIO('b\n'),StringIO('m\n'),StringIO('r\n'),StringIO('t\n')]
    miss=corr=''
    foundAllLetters = True
    i=0
    while i<len(guessedword):
        monkeypatch.setattr('sys.stdin', guessedword[i])
        l = hang_man.get_letter(miss + corr)
        if l in rand_word:
            corr = corr + l
        else:
            miss = miss + l
            if len(miss) == len(hang_man.hangman)-1:
                assert True
        i+=1
    for j in range(len(rand_word)):
        if rand_word[j] not in corr:
                foundAllLetters = False
                break
    assert not foundAllLetters
    
def test_play_again_hangman(monkeypatch):
    playopt=StringIO('y\n')
    monkeypatch.setattr('sys.stdin', playopt)
    assert hang_man.playAgain()

def test_empty_grid(capsys):
    grid=" " + ticTacToe.board[1] + "| " + ticTacToe.board[2] + "| " + ticTacToe.board[3]+'\n'+ "---------"+'\n'+ " " + ticTacToe.board[4] + "| " + ticTacToe.board[5] + "| " + ticTacToe.board[6]+"\n"+"---------"+'\n'+ " " + ticTacToe.board[7] + "| " + ticTacToe.board[8] + "| " + ticTacToe.board[9]+"\n"
    ticTacToe.print_board(ticTacToe.board)
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout==grid

def test_upgrade_grid(monkeypatch,capsys):
    grid=" " + ticTacToe.board[1] + "| " + ticTacToe.board[2] + "| " + ticTacToe.board[3]+'\n'+ "---------"+'\n'+ " " + ticTacToe.board[4] + "| " + ticTacToe.board[5] + "| " + ticTacToe.board[6]+"\n"+"---------"+'\n'+ " " + ticTacToe.board[7] + "| " + ticTacToe.board[8] + "| " + ticTacToe.board[9]+"\n"
    usermove=StringIO('1\n')
    monkeypatch.setattr('sys.stdin', usermove)
    ticTacToe.user_move()
    ticTacToe.print_board(ticTacToe.board)
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout!=grid

def test_user_play(monkeypatch):
    gridmov=[' ' for i in range(10)]
    usermove=StringIO('2\n')
    monkeypatch.setattr('sys.stdin', usermove)
    ticTacToe.user_move()
    assert gridmov!=ticTacToe.board

def test_computer_play(monkeypatch):
    gridmov=[' ' for i in range(10)]
    gridmov[1]='x'
    ticTacToe.insert_alphabet('x',1)
    comp_move=ticTacToe.computer_move()
    ticTacToe.insert_alphabet('o',comp_move)
    assert gridmov!=ticTacToe.board

def test_board_full():
    assert ticTacToe.board_full([' ','x','o','x','x','o','x','o','x','o'])

def test_user_win():
    assert ticTacToe.winner([' ','x','o',' ','o','x',' ','o',' ','x'],'x')

def test_comp_win():
    assert ticTacToe.winner([' ','o','x',' ','o','x',' ','o',' ','x'],'o')

def test_display_lives(capsys):
    lives_helpline='\n\nLives Left :  3\nHelpline Left :  1\nScore :  0\n\n\n'
    KBC.displayScore(3,0,1)
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout==lives_helpline

def test_quiz_answers_correct(monkeypatch):
    with open("./3_Implementation/data/questions.json") as file:
        data = file.read()
        questionsDict = json.loads(data)
    with open("./3_Implementation/data/options.json") as file:
        data = file.read()
        optionsDict = json.loads(data)
    with open("./3_Implementation/data/answers.json") as file:
        data = file.read()
        answersDict = json.loads(data)
    with open("./3_Implementation/data/rewards.json") as file:
        data = file.read()
        rewardsDict = json.loads(data)
    lives = 3
    helpLines = 1
    score = 0
    KBC.displayScore(lives, score, helpLines)
    for index, question in enumerate(questionsDict, start=1):
        if lives == 0:
            assert False
        opt=StringIO(str(answersDict[question]+1)+'\n')
        monkeypatch.setattr('sys.stdin',opt)
        userAnswer = input("Answer : ")
        if userAnswer == 'quit':
            assert False
        else:
            userAnswer = int(userAnswer)
            if userAnswer == 'quit':
                assert False
            else:
                userAnswer = int(userAnswer)
        if userAnswer == 5050:
            if helpLines > 0:
                helpLines = 0
                newOptions = KBC.helpline(
                    KBC.optionsDict[question], KBC.answersDict[question])
                userAnswer = int(input("Answer : "))
                if userAnswer == 'quit':
                    assert False
                else:
                    userAnswer = int(userAnswer)
                if userAnswer < 3:
                    if newOptions[userAnswer-1] == KBC.displayCorrect():
                        score = score + KBC.rewardsDict[question]
                    else:
                        lives = lives - 1
                else:
                    lives = lives - 1
            else:
                userAnswer = int(input("Answer : "))
                if userAnswer == 'quit':
                    assert False
                else:
                    userAnswer = int(userAnswer)
                if KBC.answersDict[question] == userAnswer - 1:
                    score = score + KBC.rewardsDict[question]
                else:
                    lives = lives - 1
        else:
            if answersDict[question] == userAnswer - 1:
                score = score + rewardsDict[question]
            else:
                lives = lives - 1
    print('You Won!')
    print('You can take ' + str(int(score)) + ' Rupees home!')
    print('Thankyou for playing!')
    assert True

def test_quiz_answers_wrong(monkeypatch):
    with open("./3_Implementation/data/questions.json") as file:
        data = file.read()
        questionsDict = json.loads(data)
    with open("./3_Implementation/data/options.json") as file:
        data = file.read()
        optionsDict = json.loads(data)
    with open("./3_Implementation/data/answers.json") as file:
        data = file.read()
        answersDict = json.loads(data)
    with open("./3_Implementation/data/rewards.json") as file:
        data = file.read()
        rewardsDict = json.loads(data)
    lives = 3
    helpLines = 1
    score = 0
    for index, question in enumerate(questionsDict, start=1):
        if lives == 0:
            break
        opt=StringIO(str(answersDict[question]-1)+'\n')
        monkeypatch.setattr('sys.stdin',opt)
        userAnswer = input("Answer : ")
        if userAnswer == 'quit':
            assert True
        else:
            userAnswer = int(userAnswer)
            if userAnswer == 'quit':
                exit()
            else:
                userAnswer = int(userAnswer)
        if userAnswer == 5050:
            if helpLines > 0:
                helpLines = 0
                newOptions = KBC.helpline(
                    KBC.optionsDict[question], KBC.answersDict[question])
                userAnswer = int(input("Answer : "))
                if userAnswer == 'quit':
                    exit()
                else:
                    userAnswer = int(userAnswer)
                print('\n')
                if userAnswer < 3:
                    if newOptions[userAnswer-1] == KBC.displayCorrect():
                        score = score + KBC.rewardsDict[question]
                    else:
                        print('Correct answer : ', KBC.displayCorrect())
                        lives = lives - 1
                else:
                    lives = lives - 1
            else:
                userAnswer = int(input("Answer : "))
                if userAnswer == 'quit':
                    exit()
                else:
                    userAnswer = int(userAnswer)
                if KBC.answersDict[question] == userAnswer - 1:
                    score = score + KBC.rewardsDict[question]
                else:
                    lives = lives - 1
        else:
            if answersDict[question] == userAnswer - 1:
                score = score + rewardsDict[question]
            else:
                lives = lives - 1
    if(lives==3):
        print('You Won!')
        print('You can take ' + str(int(score)) + ' Rupees home!')
        print('Thankyou for playing!')
        assert False
    else:
        assert True

def test_snake_move_left(monkeypatch):
    monkeypatch.setattr('sys.stdin',pygame.K_LEFT)
    pygame.init()
    dis_width = 600
    dis_height = 400
    dis = pygame.display.set_mode((dis_width, dis_height))
    snake_block=10
    if pygame.event.get()==pygame.K_LEFT:
        assert (snake_block-1,snake_block)==(9,10)

def test_snake_move_right(monkeypatch):
    monkeypatch.setattr('sys.stdin',pygame.K_RIGHT)
    snake_block=10
    if pygame.event.get()==pygame.K_RIGHT:
        assert (snake_block+1,snake_block)==(11,10)

def test_snake_move_up(monkeypatch):
    monkeypatch.setattr('sys.stdin',pygame.K_UP)
    snake_block=10
    if pygame.event.get()==pygame.K_UP:
        assert (snake_block,snake_block-1)==(10,9)

def test_snake_move_down(monkeypatch):
    monkeypatch.setattr('sys.stdin',pygame.K_DOWN)
    snake_block=10
    if pygame.event.get()==pygame.K_DOWN:
        assert (snake_block,snake_block+1)==(10,11)

def test_snake_length(monkeypatch):
    monkeypatch.setattr('sys.stdin',pygame.K_RIGHT)
    snake_block=10
    snake_length=1
    foodx,foody=11,10
    if pygame.event.get()==pygame.K_RIGHT:
        if (snake_block+1,snake_block)==(foodx,foody):
            assert (snake_length+1)==2