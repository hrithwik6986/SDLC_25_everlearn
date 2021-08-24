import hang_man,KBC,snakegame,ticTacToe
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

