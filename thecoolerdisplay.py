# Import des librairies nécessaires
import datetime, time, threading, unidecode

# Bouts de phrases à insérer par rapport à l'info donnée par datetime
# print_fr_day = ('Dimanche', 'Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi')
# print_fr_month = (None, 'Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre')
print_fr_unit = ["l'heure", "les minutes", "les secondes"]

# Variables faussement boléennes, mode permet de désigner l'index 0 ou 1 en étant %2
stop = False
paused = False
set_clock_running = False
automatic = False
convention = 1

# Infos nécessaires pour l'input des unités H S M : bouts de phrases pour print, unit_b pour placer le curseur au bon espace, et le maximum
unit_cursor_back = [11,7,3]
unit_max_values = [23,60,60]

#codes ansi pour les prints \033[
cursor_line_1 = "\033[s\033[H\033[2K"
cursor_line_2 = "\033[s\033[H\033[1B\033[2K"
cursor_line_3 = "\033[H\033[2B\033[2K"
cursor_line_4 = "\033[H\033[3B\033[2K"
cursor_line_5 = "\033[H\033[4B\033[2K"
cursor_line_6 = "\033[H\033[5B\033[2K"

cursor_save = "\033[s"
cursor_load = "\033[u"
cursor_linecls = "\033[2K"
cursor_lightcls = "\033[0J"
cursor_heavycls = "\033[H\033[0J"

cursor_bold_start = "\033[1m"
cursor_bold_end = "\033[22m"
cursor_style_finish = "\033[0m"

cycle = ("AM", "PM")
clock = ("__","__","__")
alarm = ("__","__","__")
custom_hours = ("--")
custom_minutes = ("--")
custom_seconds = ("--")

def define_clock():
    global clock
    while True:
        if paused == True:
            continue
        elif automatic == True:
            current_time = datetime.datetime.now()
            clock = (current_time.strftime("%H"), current_time.strftime("%M"), current_time.strftime("%S"))
            time.sleep(0.05)
        elif automatic == False:
            if set_clock_running == False:
                clock = (custom_hours, custom_minutes, custom_seconds)
                time.sleep(0.9)
        if stop == True:
            return

def clock_ticking():
    global custom_hours, custom_minutes, custom_seconds
    while True:
        if custom_hours != "--" and set_clock_running == False:
            if int(custom_seconds) < 59:
                custom_seconds = int(custom_seconds)+1
            else:
                custom_seconds = "00"
                if int(custom_minutes) < 59:
                    custom_minutes = int(custom_minutes)+1
                else:
                    custom_minutes = "00"
                    if int(custom_hours) < 23:
                        custom_hours = int(custom_hours)+1
                    else:
                        custom_hours = "00"
            if len(str(custom_hours)) <2:
                custom_hours = "0" + str(custom_hours)
            if len(str(custom_minutes)) <2:
                custom_minutes = "0" + str(custom_minutes)
            if len(str(custom_seconds)) <2:
                custom_seconds = "0" + str(custom_seconds)
            time.sleep(1)

def display_clock():
    while True:
        print(f"{cursor_line_1}{clock[0]} : {clock[1]} : {clock[2]}{cursor_load}", end="", flush=True)
        time.sleep(1)
        if stop == True:
            time.sleep(0.3)
            print(f"{cursor_heavycls}", end="")
            return

def display_terminal():
    while True:
        global convention, stop, automatic, set_clock_running
        commande = input(f"{cursor_line_4}{cursor_lightcls}Commande : ").strip(" ").lower()
        if commande == "convention":
            convention +=1
            continue
        if commande == "stop":
            stop = True
            break
        if commande == "automatique":
            automatic = True
            threading.Thread(target=unset_warning).start()
        if commande == "manuel":
            automatic = False
            threading.Thread(target=unset_warning).start()
        if unidecode.unidecode(commande) == "regler":
            automatic = False
            set_clock_running = True
            set_clock()
            set_clock_running = False
            if threading.Thread(target=clock_ticking).is_alive() == False:
                threading.Thread(target=clock_ticking).start()
            threading.Thread(target=unset_warning).start()
        else: continue

def unset_warning():
    if automatic == False and custom_hours == "--" and set_clock_running == False:
        print(f"{cursor_line_3}Aucune heure n'a été définie :(", end="", flush=True)
    else: print(f"{cursor_save}{cursor_line_3}{cursor_load}", end="", flush=True)

def set_clock():
    global custom_hours, custom_minutes, custom_seconds
    custom_hours = str(set_values("hours"))
    custom_minutes = str(set_values("minutes"))
    custom_seconds = str(set_values("secondes"))

def set_values(unit):
    if unit == "hours": unit = 0
    elif unit == "minutes": unit = 1
    else: unit = 2
    print(f"{cursor_line_5}Entrez {print_fr_unit[unit]}")
    while True:
        value = "__"
        value = input(f"{cursor_line_4}Alarme : {custom_hours}H {custom_minutes}M {custom_seconds}S\033[{unit_cursor_back[unit]}D").strip("- ,.")
        try: test = int(value)
        except Exception: 
            print(f"{cursor_line_6}/!\ Entrez une valeur numérique sous la forme '00'", end="")
            continue
        if 1 == len(str(value)) or len(str(value)) >=3 :
            print(f"{cursor_line_6}/!\ Entrez une valeur constituée de 2 chiffres '00'", end="")
            continue
        elif test >= unit_max_values[unit]+1:
            print(f"{cursor_line_6}/!\ Entrez une valeur correcte à l'unité (entre 00 et {unit_max_values[unit]})", end="")
            continue
        elif len(str(value)) == 2:
            print(f"{cursor_line_4}{cursor_lightcls}", end="")
            return value


print(f"{cursor_heavycls}", end="")
threading.Thread(target=define_clock).start()

threading.Thread(target=display_terminal).start()
threading.Thread(target=unset_warning).start()
threading.Thread(target=display_clock).start()