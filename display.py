# Import des librairies nécessaires
import datetime, time, threading

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
    if input_unit_alarm(int(mode%2)) == 0:
        return
    input_unit_alarm(2)
    input_unit_alarm(3)
    if mode%2 == 0:
        print(f"{cursor_line_5}Entrez {unit[4]}", end="")
        while True:
            alarm[4] = input(f"{cursor_line_4}Alarme : {alarm[0]}H {alarm[2]}M {alarm[3]}S __\033[2D").strip(" ").upper()
            if alarm[4] not in ("AM", "PM"):
                continue
            else: break
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

def input_unit_alarm(valeur):
    global alarm, unit
    print(f"{cursor_line_5}Entrez {unit[valeur]}")
    while True:
        alarm[valeur] = "__"
        alarm[valeur] = input(f"{cursor_line_4}Alarme : {alarm[int(mode%2)]}H {alarm[2]}M {alarm[3]}S\033[{unit_b[valeur]}D").strip("- ,.")
        # if not alarm[0] and not alarm[1]:
        #     choix = input(f"\033[2K\033[F\033[2KAnnuler l'alarm ? o/n \n").strip().lower()
        #     if choix in ('o', 'oui'):
        #         print(f"\033[F\033[2K", end="")
        #         return 0
        #     else: continue
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
            return 1


print(f"{cursor_heavycls}", end="")
threading.Thread(target=command_terminal).start()
threading.Thread(target=display_clock).start()
time.sleep(0.5)
threading.Thread(target=display_alarm).start()