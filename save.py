
import os
import glob

def show_list():
    print(" ")
    file_name_list=glob.glob("./save/*.txt")
    for i in range(0,len(file_name_list)):
        print(str(i+1) + "." + " " + file_name_list[i])
    print(" ")
    return file_name_list


def file_name():
    file_name=input("Input file name: ")
    name="./save/%s.txt" %file_name
    return name

def save(word, mistake, correct_num, wrong_word, wrong_alph):
    option="a"
    show_list()
    print("Do want to save the game? [y/n]")  # n을 쓸경우 처음 메뉴 화면으로 돌아감. y를 쓸 경우 게임을 저장함.
    user_chose=input("Choose: ")
    if user_chose == "y":
        while 1:
            name=file_name()
            if os.path.isfile(name):
                cover_choice=input("Cover? [y/n]")
                if cover_choice=="y":
                    option = "w"
                    break
            else:
                break
        save_file=open(name, option)
        save_file.write("Word:" + word + "\n")

        save_file.write("Mistake:" + str(mistake) + "\n")

        save_file.write("Correct number:")
        for i in correct_num:
            save_file.write(str(int(i)))
        save_file.write("\n")

        save_file.write("Wrong word:")
        for i in wrong_word:
            save_file.write(i + ",")
        save_file.write("\n")

        save_file.write("Wrong Alphabet:")
        for i in wrong_alph:
            save_file.write(i)
        save_file.write("\n")

        save_file.close()

def choose_file():
    file_list=show_list()
    file_num=int(input("file number: "))
    file=file_list[file_num-1]
    state=True
    return file, state

def load(file):
    save_data_file=open(file, "r")
    data=save_data_file.readlines()
    split_data=[]
    for i in data:
        split_data.append((i.split(":")[1]).split("\n")[0])
    save_word=split_data[0]
    save_mistake=int(split_data[1])

    save_check=[]
    for i in range(0,len(split_data[2])):
        save_check.append(int(split_data[2][i]))

    save_wrong_word=[]
    split_data[3].split(",")
    word=""
    for i in range(0,len(split_data[3])):
        if split_data[3][i]==",":
            save_wrong_word.append(word)
            word=""
        else:
            word=word + split_data[3][i]

    save_wrong_alph=[]
    for i in range(0,len(split_data[4])):
        save_wrong_alph.append(split_data[4][i])

    slice_data=[]
    for i in save_word:
        slice_data.append(i)
    #print(save_word, save_mistake, save_check, save_wrong_word, save_wrong_alph)
    return save_word, slice_data, len(save_word), 6-save_mistake, save_mistake, save_wrong_alph, save_wrong_word, save_check
