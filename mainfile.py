import time, datetime, keyboard, os, threading

day = ('Dimanche', 'Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi')
month = (None, 'Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre')

stop = 0
mode = 1
unit = ["l'heure", "l'heure", "les minutes", "les secondes", "AM / PM"]
unit_b = [11,11,7,3]
unit_max = [12,23,60,60]
alarm = ["__","__","__","__","__"]


cursor_line_1 = "\033[s\033[H\033[2K"
cursor_line_2 = "\033[s\033[H\033[1B\033[2K"
cursor_line_3 = "\033[H\033[2B\033[2K"
cursor_line_4 = "\033[H\033[3B\033[2K"
cursor_line_5 = "\033[H\033[4B\033[2K"
cursor_line_6 = "\033[H\033[5B\033[2K"

cursor_load = "\033[u"
cursor_linecls = "\033[2K"
cursor_lightcls = "\033[0J"
cursor_heavycls = "\033[H\033[0J"

cursor_bold_start = "\033[1m"
cursor_bold_end = "\033[22m"
cursor_style_finish = "\033[0m"

# Définition des fonctions clés
def calendar():
    calendar = (day[int(datetime.datetime.now().strftime("%w"))], datetime.datetime.now().strftime("%d"), month[int(datetime.datetime.now().strftime("%m"))])
    return calendar

def clock():
    datetime_now_clock = (datetime.datetime.now().strftime("%I"), datetime.datetime.now().strftime("%H"), datetime.datetime.now().strftime("%M"), datetime.datetime.now().strftime("%S"), datetime.datetime.now().strftime("%p"))
    return datetime_now_clock

def display_alarm():
    global alarm
    while True:
        if alarm[0] != "__" and mode%2==1:
            print(f"{cursor_line_2}! Alarme définie pour {alarm[1]}:{alarm[2]}:{alarm[3]} !{cursor_load}", end="", flush=True)
        elif alarm[0] != "__" and mode%2==0:
            print(f"{cursor_line_2}! Alarme définie pour {alarm[0]}:{alarm[2]}:{alarm[3]} {alarm[4]} !{cursor_load}", end="", flush=True)
        elif alarm[0] != "__" and clock()[int(mode%2)] == alarm[int(mode%2)] and clock()[2] == alarm[2] and clock()[3] == alarm[3]:
                print(f"{cursor_line_2}RINGGGGG{cursor_load}", end="", flush=True)
                time.sleep(5)
                alarm = ["__","__","__","__","__"]
        else: print(f"{cursor_line_2}Aucune alarme définie.{cursor_load}", end="", flush=True)
        time.sleep(0.5)
        if stop == 1:
            return


def display_clock():
    while True:
        if mode%2 == 0:
            print(f"{cursor_line_1}{calendar()[0]} {calendar()[1]} {calendar()[2]}   \
{clock()[0]} : {clock()[2]} : {clock()[3]} {clock()[4]}{cursor_load}", end="", flush=True)
        if mode%2 == 1:
            print(f"{cursor_line_1}{calendar()[0]} {calendar()[1]} {calendar()[2]}   \
{clock()[1]} : {clock()[2]} : {clock()[3]}{cursor_load}", end="", flush=True)
        time.sleep(0.5)
        if stop == 1:
            time.sleep(1)
            print(f"{cursor_heavycls}", end="")
            return

def command_terminal():
    while True:
        global mode, stop
        commande = input(f"{cursor_line_4}{cursor_lightcls}Commande : ")
        if commande == "mode":
            mode +=1
            continue
        if commande == "alarme":
            set_alarm()
        if commande == "stop":
            stop +=1
            break
        else: continue

def set_alarm():
    alarm = (input_hours(),)
    if input_unit_alarm(int(mode%2)) == 0:
        return
    input_unit_alarm(2)
    input_unit_alarm(3)
    print(f"{cursor_line_5}Entrez {unit[4]}", end="")
    while True:
        alarm[4] = input(f"{cursor_line_4}Alarme : {alarm[0]}H {alarm[2]}M {alarm[3]}S __\033[2D").strip(" ").upper()
        if alarm[4] not in ("AM", "PM"):
            continue
        else: break
    if mode%2 == 0:
        if alarm[4] == "PM" and str(alarm[0]) != "12":
            alarm[1] = str(int(alarm[0])+12)
        elif alarm[4] == "AM" and str(alarm[0]) == "12":
            alarm[1] = "00"
        else: alarm[1] = alarm[0]
    if mode%2 == 1:
        if alarm[1] == "00": alarm[0] = "12"; alarm[4] = "AM"
        elif 12 < int(alarm[1]) < 22:
            alarm[0] = "0"+str(int(alarm[1])-12)
            alarm[4] = "PM"
        elif 21 < int(alarm[1]):
            alarm[0] = int(alarm[1])-12
            alarm[4] = "PM"
        else: 
            alarm[0] = alarm[1]
            alarm[4] = "AM"
    print(f"{cursor_line_4}{cursor_lightcls}", end="")

def input_hours():
    global alarm, unit, mode
    print(f"{cursor_line_5}Entrez {unit[(mode%2)]}")
    while True:
        value = "__"
        value = input(f"{cursor_line_4}Alarme : {value}H {alarm[2]}M {alarm[3]}S\033[{unit_b[0]}D").strip("- ,.")
        try: test = int(value)
        except Exception: 
            print(f"{cursor_line_6}/!\ Entrez une valeur numérique sous la forme '00'", end="")
            continue
        if 1 == len(str(value)) or len(str(value)) >=3 :
            print(f"{cursor_line_6}/!\ Entrez une valeur constituée de 2 chiffres '00'", end="")
            continue
        elif test >= unit_max[(mode%2)]+1:
            print(f"{cursor_line_6}/!\ Entrez une valeur correcte à l'unité (entre 00 et {unit_max[(mode%2)]})", end="")
            continue
        elif len(str(value)) == 2:
            print(f"{cursor_line_4}{cursor_lightcls}", end="")
            
            return value
            


def input_unit_alarm(valeur):
    global alarm, unit
    print(f"{cursor_line_5}Entrez {unit[valeur]}")
    while True:
        alarm[valeur] = "__"
        alarm[valeur] = input(f"{cursor_line_4}Alarme : {alarm[int(mode%2)]}H {alarm[2]}M {alarm[3]}S\033[{unit_b[valeur]}D").strip("- ,.")
        try: test = int(alarm[valeur])
        except Exception: 
            print(f"{cursor_line_6}/!\ Entrez une valeur numérique sous la forme '00'", end="")
            continue
        if 1 == len(str(alarm[valeur])) or len(str(alarm[valeur])) >=3 :
            print(f"{cursor_line_6}/!\ Entrez une valeur constituée de 2 chiffres '00'", end="")
            continue
        elif test >= unit_max[valeur]+1:
            print(f"{cursor_line_6}/!\ Entrez une valeur correcte à l'unité (entre 00 et {unit_max[valeur]})", end="")
            continue
        elif len(str(alarm[valeur])) == 2:
            print(f"{cursor_line_4}{cursor_lightcls}", end="")


print(f"{cursor_heavycls}", end="")
threading.Thread(target=command_terminal).start()
threading.Thread(target=display_clock).start()
time.sleep(0.5)
threading.Thread(target=display_alarm).start()



def cls():
     os.system('cls' if os.name=='nt' else 'clear')

def clock_ticking(clock):
    
    if len(clock) == 4:
        if clock[2] < 59:
            clock = (clock[0], clock[1], clock[2]+1, clock[3])
        else:
            clock = (clock[0], clock[1], 0, clock[3])
            if clock[1] < 59:
                clock = (clock[0], clock[1]+1, clock[2], clock[3])
            else:
                clock = (clock[0], 0, clock[2], clock[3])
                if clock[0] < 13:
                    clock = (clock[0]+1, clock[1], clock[2], clock[3])
                
                if clock[0] == 12 and clock[1] == 0 and clock[2] == 0:
                    if clock[3] == "AM":
                        clock = (clock[0], clock[1], clock[2], "PM")
                    else:
                        clock = (clock[0], clock[1], clock[2], "AM")

                if clock[0] == 13:
                    clock = (1, clock[1], clock[2], clock[3]) 

    else:
        if clock[2] < 59:
            clock = (clock[0], clock[1], clock[2]+1)
        else:
            clock = (clock[0], clock[1], 0)
            if clock[1] < 59:
                clock = (clock[0], clock[1]+1, clock[2])
            else:
                clock = (clock[0], 0, clock[2]) 
                if clock[0] < 23:
                    clock = (clock[0]+1, clock[1], clock[2]) 
                else:
                    clock = (0, clock[1], clock[2]) 
    
    return clock

def set_time(format):
    min_hour = 0
    max_hour = 23
    hour = -1
    minute = -1
    second = -1

    if format == "12h":
        half_day = ""
        while half_day != "AM" and half_day != "PM":
            half_day = input("AM or PM? ").upper().strip()
        min_hour = 1
        max_hour = 12
    
    while hour < min_hour or hour > max_hour:
        hour = int(input(f"Enter hours ({min_hour}-{max_hour}): "))
        if hour < 0 or hour > max_hour:
            print(f"Please enter a number between {min_hour} and {max_hour}!")

    while minute < 0 or minute > 59:
        minute = int(input("Enter minutes (0-59): "))
        if minute < 0 or minute > 59:
            print("Please enter a number between 0 and 59!")

    while second < 0 or second > 59:
        second = int(input("Enter seconds (0-59): "))
        if second < 0 or second > 59:
            print("Please enter a number between 0 and 59!")

    if format == "12h":
        time = (hour, minute, second, half_day)
    else:
        time = (hour, minute, second)

    return time

def choose_format():
    """ Ask the user to choose between 12h or 24h format """
    format_choice = input("Choose the time format (12h/24h): ")
    if format_choice != "12h" and format_choice != "24h":
        return choose_format()
    return format_choice

def choose_alarm(format):
    alarm_choice = input("Do you want to set an alarm ?(yes/no):").lower().strip()
    if alarm_choice != "yes" and alarm_choice != "y" and alarm_choice != "no" and alarm_choice != "n":
        return choose_alarm(format)
    elif alarm_choice == "yes" or alarm_choice == "y":
        alarm_clock = set_time(format)  
        return alarm_clock
    else:
        return None

def format_time(time):
    if len(str(time[0])) == 1:
        temp_str = "0" + str(time[0]) + ":"
    else:
        temp_str = str(time[0]) + ":"

    if len(str(time[1])) == 1:
        temp_str += "0" + str(time[1]) + ":"
    else:
        temp_str += str(time[1]) + ":"

    if len(str(time[2])) == 1:
        temp_str += "0" + str(time[2])
    else:
        temp_str += str(time[2])

    if len(time) == 4:
        temp_str += " " + time[3]
    
    return temp_str

# update time in terminal
def display_time(current_time, max_display, alarm, message=""):
    current_time_str = format_time(current_time)
   
    #current_time_str = str(current_time[0]) + ":" + str(current_time[1]) + ":" + str(current_time[2]) + " "
    if alarm:
        #alarm_str = "alarm : " + str(alarm[0]) + ":" + str(alarm[1]) + ":" + str(alarm[2]) + " " 
        alarm_str = " ; alarm : " + format_time(alarm)
    else:
        alarm_str = ""

    print("\r" + current_time_str + alarm_str + message + " ", end="")

    if alarm and current_time[0] * 3600 + current_time[1] * 60 + current_time[2] <= alarm[0] * 3600 + alarm[1] * 60 + alarm[2] + max_display:
        cls()
        print("\r" + current_time_str + alarm_str + message + " ", end="")

def display_alarm(clock, alarm, max_display):
    if alarm and clock[0] * 3600 + clock[1] * 60 + clock[2] >= alarm[0] * 3600 + alarm[1] * 60 + alarm[2] and clock[0] * 3600 + clock[1] * 60 + clock[2] <= alarm[0] * 3600 + alarm[1] * 60 + alarm[2] + max_display:
        ring = "Ring ring! Ring ring!"
        message = (f"{ring:>30}")
        # Blinking message
        #while clock[1] < alarm_time[1] + 1:
            #if clock[2] % 2 == 0:
                #return "Ring ring! Ring ring!"
            #else:
                #return ""   
        return message
    else:
        message = ""
        return message
        
def main():
    max_display = 10 #10 seconds

    format = choose_format() # value : "12h" / "24h"
    alarm = choose_alarm(format) # value: (h,m,s)
    clock = set_time(format) # value: (h,m,s)
    
    cls()
    while True :

        #clock = datetime.datetime.now()
        clock = clock_ticking(clock)

        #current_time = (clock.strftime('%H'), clock.strftime('%M'), clock.strftime('%S'))
        message = display_alarm(clock, alarm, max_display)
        display_time(clock, max_display, alarm, message)
        
        for i in range(10):
            time.sleep(0.1)
            try:
                if keyboard.is_pressed('space'):
                    keyboard.wait('space')
            except:
                print("error")

        #TODO need to not actualize clock variable when paused
        
# main()
