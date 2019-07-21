from option import option
import time
from game_play import game_loop

def main():
    file=""
    state=False
    while True:
        #score="Score: %d" %int(recieve_data()[2])  #3 번째에 점수가 저장된어 있음
        #print(score)
        print("1.PLAY GAME  2.OPTION   3.END")
        user_chose=int(input("Chose Number: "))

        if user_chose==1:
            game_loop(file,state)
        elif user_chose==2:
            file,state=option()
        elif user_chose==3:
            print("Bye~ ")
            time.sleep(2)
            break

if __name__=="__main__":
    main()
