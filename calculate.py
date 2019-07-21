
def compare_word(word):
    game_word=main.word()
    for i in game_word:
        if word==i or word=="0back0":
            return 1
    return 0
