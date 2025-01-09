# Import des librairies nécessaires
import datetime, time, threading, unidecode

# Bouts de phrases à insérer par rapport à l'info donnée par datetime
# print_fr_day = ('Dimanche', 'Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi')
# print_fr_month = (None, 'Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre')
print_fr_unit = ("l'heure", "les minutes", "les secondes")
print_fr_input_type = ("Heure :", "Alarme :")

# Variables faussement boléennes, mode permet de désigner l'index 0 ou 1 en étant %2
off = False
paused = False
alarm_snoozed = False
alarm_stopped = False
set_clock_running = False
set_alarm_running = False
automatic = False
convention = 1

# Infos nécessaires pour l'input des unités H S M : bouts de phrases pour print, unit_b pour placer le curseur au bon espace, et le maximum
unit_cursor_back = [11,7,3]
unit_max_values = [23,60,60]

#codes ansi pour les prints \033[
cursor_line_1 = "\033[1;0H"
cursor_line_2 = "\033[2;0H"
cursor_line_3 = "\033[3;0H"
cursor_line_4 = "\033[4;0H"
cursor_line_5 = "\033[5;0H"
cursor_line_6 = "\033[6;0H"
cursor_line_7 = "\033[7;0H"
cursor_print_clock = "\033[1;15H"
cursor_input_commande = "\033[5;20H"

cursor_save = "\033[s"
cursor_load = "\033[u"

cursor_line_clear = "\033[2K"
cursor_light_clear = "\033[0J"
cursor_heavy_clear = "\033[1;0H\033[0J"

cursor_bold_start = "\033[1m"
cursor_bold_end = "\033[22m"
cursor_style_finish = "\033[0m"

cycle = ("AM", "PM")
clock = ("--","--","--")
alarm = ("--","--","--")
unset = ("--","--","--")

custom_hours = ("--")
custom_minutes = ("--")
custom_seconds = ("--")
alarm_hours = ("--")
alarm_minutes = ("--")
alarm_seconds = ("--")

def define_clock():
    global clock
    while True:
        if paused == True:
            continue
        elif automatic == True:
            current_time = datetime.datetime.now()
            clock = (current_time.strftime("%H"), current_time.strftime("%M"), current_time.strftime("%S"))
        elif automatic == False:
            clock = (str(custom_hours), str(custom_minutes), str(custom_seconds))
        if off == True:
            return

def clock_ticking():
    global custom_hours, custom_minutes, custom_seconds
    while True:
        if custom_seconds != "--" and set_clock_running == False and paused == False:
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
        if off == True:
            return

def check_alarm():
    global alarm
    if clock == alarm:
        return True

def display_clock():
    while True:
        print(
            f"{cursor_save}{cursor_print_clock}{cursor_line_clear}",
            f"{clock[0]} : {clock[1]} : {clock[2]}",
            f"{cursor_load}", sep="", end="", flush=True)
        if automatic == False and clock == unset:
            print(
                f"{cursor_save}{cursor_line_2}{cursor_line_clear}",
                f"Aucune heure n'a été définie :(",
                f"{cursor_load}", sep="", end="", flush=True)
        else: print(f"{cursor_save}{cursor_line_2}{cursor_line_clear}{cursor_load}", end="", flush=True)
        time.sleep(0.9)
        if off == True:
            return

def display_alarm():
    while True:
        global alarm_snoozed, alarm_stopped
        if alarm == unset or set_alarm_running == True:
            print(
                f"{cursor_save}{cursor_line_3}{cursor_line_clear}",
                f"Aucune alarme définie.",
                f"{cursor_load}", sep="", end="", flush=True)
        elif alarm != unset and set_alarm_running == False:
            print(
                f"{cursor_save}{cursor_line_3}{cursor_line_clear}",
                f"! Alarme définie à {alarm[0]} : {alarm[1]} : {alarm[2]} !"
                f"{cursor_load}", sep="", end="", flush=True)
        if alarm != unset and set_alarm_running == False and check_alarm() == True:
            print(
                f"{cursor_save}{cursor_line_3}{cursor_line_clear}"\
                f"{cursor_bold_start}DRING DRING{cursor_bold_end}"\
                f"{cursor_load}", sep="", end="", flush=True)
            while alarm_stopped != True and alarm_snoozed != True:
                if alarm_stopped == True:
                    set_alarm_reset()
                if alarm_snoozed == True:
                    alarm_snooze()
            alarm_snoozed = alarm_stopped = False
        if off == True:
            return
        time.sleep(0.9)

def display_terminal():
    while True:
        global convention, off, automatic, paused, alarm_stopped, alarm_snoozed
        print(
            f"{cursor_line_5}{cursor_light_clear}",
            f"\t{cursor_bold_start}Commande :{cursor_bold_end}\n",
            f"{"pause":<18}- Met l'horloge en pause\n",
            f"{"automatique":<18}- Affiche l'heure système\n",
            f"{"manuel":<18}- Affiche l'heure personnalisée\n",
            f"{"regler":<18}- Règle une heure personnalisée\n",
            f"{"alarme":<18}- Règle une alarme\n",
            f"{"retarder":<18}- Ajoute 5 minutes à l'alarme\n"
            f"{"stop alarme":<18}- Arrête l'alerte de l'alarme\n"
            f"{"reset":<18}- Réinitialise toutes les données\n",
            f"{"reset alarme":<18}- Réinitialise l'alarme\n",
            f"{"reset horloge":<18}- Réinitialise l'heure personnalisée\n",
            f"{"off":<18}- Eteint l'appareil\n",
            sep="", end="", flush=True)
        commande = input(f"{cursor_input_commande}").strip(" ").lower()

        if commande == "pause":
            if paused == False: paused = True
            elif paused == True: paused = False
        if commande == "automatique":
            automatic = True
        if commande == "manuel":
            automatic = False
        if unidecode.unidecode(commande) == "regler":
            automatic = False
            set_clock()
        if commande == "alarme":
            set_alarm()
        if commande in ("retarder", "snooze"):
            alarm_snoozed = True
        if commande in ("stop alarme", "stop"):
            alarm_stopped = True


        if commande == "reset":
            set_reset()
            paused = False
            print(f"{cursor_heavy_clear}", end="", flush=True)
        if commande == "reset horloge":
            set_clock_reset()
        if commande == "reset alarme":
            set_alarm_reset()
        else: continue
        if commande == "off":
            off = True
            time.sleep(1)
            print(f"{cursor_heavy_clear}", end="", flush=True)
            break

def set_reset():
    global custom_hours, custom_minutes, custom_seconds, alarm
    custom_hours = custom_minutes = custom_seconds = "--"
    alarm = ("--","--","--")

def set_clock():
    global custom_hours, custom_minutes, custom_seconds, set_clock_running
    custom_hours = custom_minutes = custom_seconds = "--"
    set_clock_running = True
    set_hours = custom_hours = str(set_values("hours", "--", "--", "--"))
    set_minutes = custom_minutes = str(set_values("minutes", set_hours, "--", "--"))
    custom_seconds = str(set_values("seconds", set_hours, set_minutes, "--"))
    set_clock_running = False
def set_clock_reset():
    global custom_hours, custom_minutes, custom_seconds
    custom_hours = custom_minutes = custom_seconds = "--"

def set_alarm():
    global alarm_hours, alarm_minutes, alarm_seconds, alarm, set_alarm_running
    set_alarm_running = True
    set_hours = alarm_hours = str(set_values("hours", "--", "--", "--"))
    set_minutes = alarm_minutes = str(set_values("minutes", set_hours, "--", "--"))
    alarm_seconds = str(set_values("seconds", set_hours, set_minutes, "--"))
    alarm = (alarm_hours, alarm_minutes, alarm_seconds)
    alarm_hours = alarm_minutes = alarm_seconds = "--"
    set_alarm_running = False
def set_alarm_reset():
    global alarm
    alarm = ("--","--","--")
def alarm_snooze():
    global alarm
    snoozed_minutes = int(alarm[1]) + 5
    if len(str(snoozed_minutes)) == 1:
        snoozed_minutes = "0"+str(snoozed_minutes)
    alarm = ((alarm[0]), (snoozed_minutes), (alarm[2]))

def set_values(unit, print_hours, print_minutes, print_seconds):
    if unit == "hours": unit = 0
    elif unit == "minutes": unit = 1
    elif unit == "seconds": unit = 2
    if set_clock_running == True: input_type = 0
    else: input_type = 1
    print(
        f"{cursor_line_6}{cursor_light_clear}",
        f"Entrez {print_fr_unit[unit]}",
        sep="", end="", flush=True)
    while True:
        value = "--"
        print(
            f"{cursor_line_5}{cursor_line_clear}",
            f"\t{cursor_bold_start}{print_fr_input_type[input_type]}{cursor_bold_end}",
            f"{print_hours}H {print_minutes}M {print_seconds}S",
            sep="", end="", flush=True)
        value = input(f"\033[{unit_cursor_back[unit]}D").strip("- ,.")
        try: test = int(value)
        except Exception: 
            print(
                f"{cursor_line_7}{cursor_line_clear}",
                f"/!\ Entrez une valeur numérique sous la forme '00'",
                sep="", end="", flush=True)
            continue
        if 1 == len(str(value)) or len(str(value)) >=3 :
            print(
                f"{cursor_line_7}{cursor_line_clear}",
                f"/!\ Entrez une valeur constituée de 2 chiffres '00'",
                sep="", end="", flush=True)
            continue
        elif test >= unit_max_values[unit]+1:
            print(
                f"{cursor_line_7}{cursor_line_clear}",
                f"/!\ Entrez une valeur correcte à l'unité (entre 00 et {unit_max_values[unit]})",
                sep="", end="", flush=True)
            continue
        elif len(str(value)) == 2:
            print(f"{cursor_line_5}{cursor_light_clear}", end="", flush=True)
            return value


print(f"{cursor_heavy_clear}", end="", flush=True)

threading.Thread(target=define_clock).start()
threading.Thread(target=clock_ticking).start()

threading.Thread(target=display_terminal).start()
time.sleep(3)
threading.Thread(target=display_clock).start()
time.sleep(0.5)
threading.Thread(target=display_alarm).start()