import datetime
import time

# update time in terminal
def display_time(Time):  
        current_time = Time.strftime('%H:%M:%S')
        print("\r" + current_time + " ", end="")
        
def main():
    i = 0
    # while True:

    # Loop displaying time for 10 seconds
    while i <= 10:
       time.sleep(1.0)
       Time = datetime.datetime.now()
       display_time(Time)
       i+=1
main()