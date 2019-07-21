def load_word_data():
    word_file=open("./Info/game_word.txt")
    word_data=word_file.readlines()
    word_file.close()
    word_list=[]
    for i in word_data:
        word_list.append(i.split("\n")[0])
    return word_list

def compare_word(word):
    game_word=load_word_data()
    for i in range(0,len(game_word)):
        if word==game_word[i]:
            return False
    return True

def getPosition(word):
    game_word=load_word_data()
    for i in range(0,len(game_word)):
        if word==game_word[i]:
            return i
    return False

def write_file(word_list):
    word_data=open("./Info/game_word.txt", "w")
    for i in word_list:
        word_data.write(i+"\n")
    word_data.close()

def count_score(score, mistake, quiz_word, already_input_alph):
    if mistake==6:
        score = int(score)-15
        return score
    else:
        if len(quiz_word)-len(already_input_alph)<0:
            score=int(score)+10
            return score
        else:
            score=int(score)+10+10*(len(quiz_word)-len(already_input_alph))
            return score
