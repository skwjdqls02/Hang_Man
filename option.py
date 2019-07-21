from utils import compare_word, load_word_data, getPosition, write_file
from save import choose_file
def game_playtime():      #playtime을 출력하는 함수
    datafile=open("./game_info.txt", "r")
    playtime=datafile.readline()
    datafile.close()
    answer="%s" %playtime
    print(answer)

def game_rule():        #게임에 룰을 설명합니다.
    print("\n"+"무작위의 영단어가 빈칸 처리되어 나옵니다." + "\n" + "(ex cat=_ _ _) 있을 것 같은 알파벳을 입력했을떼 있다면 그 알파벳이 그자리에 나올것입니다. (ex cat=_ _ _  -> a입력 -> _ a _)" + "\n" + "입력한 알파벳이 해당 단어에 없다면 --O<-<이 하나씩 완성될 것입니다. " + "\n" + "완성이 된다면 -20pt에 다음단어로 넘어 갑니다. 완성전에 단어를 맞춘다면 +25pt 입니다." + "\n")
'''
def change_point(old_save_point):     #원래 저장 주소를 받아옵니다
    print("If you want to go back input 0back0 ")    #잘못들어왔을 경우 나가는 코드를 줍니다.
    print("EX) C:\\User\\users\\Desktop\\save.txt")    #작성 예시
    new_save_point=input("Input save point: ")

    if save_point=="0back0":
        return old_save_point     #잘못들어온 경우이므로 주소는 그대로 유지 됩니다.
    else:
        return new_save_point     #새로 입력된 주소를 반환합니다.
'''
def edit_word():                    #새로운 단어를 추가
    print("ADD:1    REMOVE:2")
    user_choice=int(input("Choice: "))
    print("Write only word")
    new_word=input("word: ")

    if user_choice==1:
        if compare_word(new_word) == False:    #존재하는 단어를 입력한 경우 다음 문장을 프린트
            print("It already exists")
            return
        else:                                  #존재하지 않는 단어를 입력한 경우 다음 문장을 프린트
            datafile=open("./game_word.txt", "a")
            datafile.write(new_word + '\n')
            datafile.close()
            text="%s is added" %new_word
            print(text)

    elif user_choice==2:                      #단어 삭제 함수

        if not compare_word(new_word):  #사실상 필요없는 참거짓과 삭제할 단어의 위치 반환
            remove_word_poitsion=getPosition(new_word)
            if remove_word_poitsion==False:
                print("No word")

            else:
                word_list=load_word_data()
                print("Remove " + word_list[remove_word_poitsion])
                del(word_list[remove_word_poitsion])   #단어 삭제
                write_file(word_list)

def word_sort():
    word_list=load_word_data()
    memo_position=0
    for i in range(0,len(word_list)):
        low=word_list[i][0]
        memo_position = i
        for g in range(i+1,len(word_list)):
            if word_list[g][0]<low:
                low=word_list[g][0]
                memo_position=g

            elif word_list[g][0] == low:
                if len(word_list[memo_position]) < len(word_list[g]):
                    length=len(word_list[memo_position])
                else:
                    length=len(word_list[g])
                for h in range(1,length):
                    if word_list[memo_position][h] > word_list[g][h]:
                        memo_position=g
                        break
                    elif word_list[memo_position][h] == word_list[g][h]:
                        pass
                    else:
                        break
        word_list[i],word_list[memo_position]=word_list[memo_position],word_list[i]
    write_file(word_list)

def show_list():
    word_list=load_word_data()
    print(" ")
    for i in range(0,len(word_list)):
        print(i+1, end='')
        print("." + " "+ word_list[i])
    print(" ")

def game_score():
    datafile=open("./game_info.txt", "r")
    datalist=datafile.readlines()
    score=datalist[1]
    datafile.close()
    answer="%s" %score
    print(answer)


def option():
    file=0
    state=False
    while 1:
        print("1.PLAY TIME  2.SCORE   3.RULE   4.SORT WORD   5.ADD/REMOVE WORD   6.SHOW WORD LIST   7.LOAD DATA   8.BACK")
        user_choose=int(input("Choose Number: "))     #사용자가 선택한 번호를 받아 옵니다.
        if user_choose==1:                           #게임플레이시간을 원하므로 game_playtime함수로 이동합니다.
            game_playtime()
        elif user_choose==2:
            game_score()
        elif user_choose==3:                         #게임에 룰을 원하므로 game_rule함수 이동합니다.
            game_rule()
        elif user_choose==4:                         #게임저장 위치를 바꾸기위해 change_point함수로 이동합니다.
            word_sort()
        elif user_choose==5:                         #단어 저장을 선택했으므로 add_word함수로 이동
            edit_word()
        elif user_choose==6:
            show_list()
        elif user_choose==7:
            file,state=choose_file()
        elif user_choose==8:                         #뒤로 가기를 선택했으므로 opition을 끝냅니다.
            break
    return file, state
