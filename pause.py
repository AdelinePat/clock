#ZA WARUDO
import keyboard
import time

def main():
    clock = (1,2,3)
    while True:
        time.sleep(1)
        clock = (1,2,clock[2]+1)
        print(clock, end="\r")
        try:
            if keyboard.is_pressed('a'):
                print(clock, end='\r')
        except:
            print("error")

main()