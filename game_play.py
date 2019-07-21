import numpy as np
from numpy.random import seed
from numpy.random import rand
from numpy.random import randint
from utils import load_word_data, count_score
import time
import sys
from save import save, load
mistake_sign=["-","-","o","<","-","<"]


seed(int(time.time()))          #난수 발생을 위해 기준을 시간으로 지정

def initGame():         #게임에 사용될 기초적인 정보를 가져오는 함수

    word_data=load_word_data()
    random=randint(0, len(word_data))
    quiz_word=word_data[random]
    word_length = len(quiz_word)
    slice_word = []
    for i in range(word_length):
        slice_word.append(quiz_word[i])
    times, score=get_game_info()
    check = np.zeros(word_length)

    print ('Start game')
    print ('Length of word is', word_length)
    print("Score: " + str(score))
    print ('_ ' *word_length)


    life = 6
    mistake=0
    already_input_alph=[]
    already_input_word=[]
    return quiz_word, slice_word, word_length, life, mistake, already_input_alph ,already_input_word, check, score

def checkExistence(str, x, check):
    count_=0
    for i in range(0,len(str)):
        if x==str[i]:
            count_=count_+1
            check[i]=1
    if count_==0:
        return check, False
    else:
        return check, True

def get_game_info():
    datafile=open("./Info/game_info.txt", "r")
    split_data=[]
    game_data=datafile.readlines()
    for i in game_data:
        split_data.append((i.split(":")[1]).split("\n")[0])
    times=int(split_data[0])+1
    score = split_data[1]
    datafile.close()
    return times, score

def set_game_info(playtime, score):
    datafile=open("./Info/game_info.txt", "w")
    datafile.write("PlayTime:" + str(playtime) + "\n")
    datafile.write("Score:" + str(score) + "\n")
    datafile.close()

def word_bool(length,slice_word,check):
    for i in range(0,length):
        if check[i]==1:
            print(slice_word[i], end=" ")
        else:
            print("_", end=" ")


def game_loop(file, state):
    # 게임을 플레이
    if not state:
        quiz_word, slice_word, length, life, mistake, already_input_alph, already_input_word, check, score = initGame()
    else:
        quiz_word, slice_word, length, life, mistake, already_input_alph, already_input_word, check = load(file)
        times,score=get_game_info()
        print ('Start game')
        print ('Length of word is', length)
        print("Score: " + str(score))
        word_bool(length, slice_word, check)

        print("||", end='')
        for i in range(0,mistake):
            print(mistake_sign[i], end="")
        print("\n" + 'Already input Alphabet: ', already_input_alph)
        print("Already input Words: ", already_input_word)

        state=False
    Bool=True

    while Bool:
        print("1. Main Menu")
        input_alph = input("Alphabet or Word(No a capital letter): ")
        if len(input_alph) > 1:
            already_input_word.append(input_alph)
            if quiz_word==input_alph:
                print("Congratulations! You Win! ")
                Bool=False
            else:
                print("Sorry. That's wrong. ")
                print("Score: " + str(score))
                mistake = mistake+1
                check, check_bool = checkExistence(slice_word, input_alph, check)
                word_bool(length,slice_word,check)

        elif input_alph == "1":
            save(quiz_word, mistake, check, already_input_word, already_input_alph)
            break

        else:
            already_input_alph.append(input_alph)
            print("Score: " + str(score))
            check, check_bool = checkExistence(slice_word, input_alph, check)
            word_bool(length,slice_word,check)
            if not check_bool:
                mistake += 1

        if np.sum(check==1) == length:
            print("Congratulations! You Win! ")
            Bool=False

        if mistake==6:
            print("Sorry. You lose. Answer is " + quiz_word)
            Bool=False

        if Bool==True:
            print("||", end='')
            for i in range(0,mistake):
                print(mistake_sign[i], end="")
            print("\n" + 'Already input Alphabet: ', already_input_alph)
            print("Already input Words: ", already_input_word)

        if Bool==False:
            # 게임 정보 불러오기.
            times, score = get_game_info()
            new_score = count_score(score, mistake, quiz_word, already_input_alph)


            # 게임 정보 쓰기.
            set_game_info(times, new_score)

            print("Countiune:1    Menu:2     End:3")
            user_choice=int(input("Choice: "))

            if user_choice==1:
                Bool=True
                quiz_word, slice_word, length, life, mistake, already_input_alph, already_input_word, check, score = initGame()
            elif user_choice==3:
                print("Bye~")
                time.sleep(2)
                sys.exit()
