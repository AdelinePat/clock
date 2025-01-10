# Import of needed libraries
import datetime, time, threading, unidecode

# Litteral sentences to be included in UI prints
print_fr_unit = ("l'heure", "les minutes", "les secondes")
print_fr_input_type = ("Heure :", "Alarme :")

# Needed infos about input units (H M S)
unit_cursor_back = [11,7,3]
unit_max_values = [23,59,59]

#ANSI escape sequences for prints \033[
cursor = {
    "line_1" : "\033[1;0H",
    "line_2" : "\033[2;0H",
    "line_3" : "\033[3;0H",
    "line_4" : "\033[4;0H",
    "line_5" : "\033[5;0H",
    "line_6" : "\033[6;0H",
    "line_7" : "\033[7;0H",
    "print_clock" : "\033[1;15H",
    "input_commande" : "\033[5;20H",

    "save" : "\033[s",
    "load" : "\033[u",

    "line_clear" : "\033[2K",
    "light_clear" : "\033[0J",
    "heavy_clear" : "\033[1;0H\033[0J",

    "bold_start" : "\033[1m",
    "bold_end" : "\033[22m",
    "red_start" : "\033[31m",
    "style_finish" : "\033[0m"
}

# Boleans variable to control functions states
off = False
paused = False
alarm_snoozed = False
alarm_stopped = False
typing_in_clock = False
typing_in_alarm = False
automatic = False

# Essential tuples
clock = ("--","--","--")
alarm = ("--","--","--")
unset = ("--","--","--")

# Tuples datas
custom_hours = "--"
custom_minutes = "--"
custom_seconds = "--"
alarm_hours = "--"
alarm_minutes = "--"
alarm_seconds = "--"

def define_clock():
    global clock
    while True:
        if paused:
            continue
        elif automatic:
            current_time = datetime.datetime.now()
            clock = (current_time.strftime("%H"), current_time.strftime("%M"), current_time.strftime("%S"))
        elif automatic == False:
            clock = (str(custom_hours), str(custom_minutes), str(custom_seconds))
        if off:
            return

def clock_ticking():
    global custom_hours, custom_minutes, custom_seconds
    while True:
        if custom_seconds != "--" and typing_in_clock == False and paused == False:
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
        if off:
            return

def check_alarm():
    if clock == alarm:
        return True

def display_clock():
    while True:
        print(
            f"{cursor["save"]}{cursor["print_clock"]}{cursor["line_clear"]}",
            f"{clock[0]} : {clock[1]} : {clock[2]}",
            f"{cursor["load"]}", sep="", end="", flush=True)
        if automatic == False and clock == unset:
            print(
                f"{cursor["save"]}{cursor["line_2"]}{cursor["line_clear"]}",
                f"Aucune heure n'a été définie :(",
                f"{cursor["load"]}", sep="", end="", flush=True)
        else: print(f"{cursor["save"]}{cursor["line_2"]}{cursor["line_clear"]}{cursor["load"]}", end="", flush=True)
        time.sleep(0.9)
        if off:
            return

def display_alarm():
    while True:
        global alarm_snoozed, alarm_stopped
        if alarm == unset or typing_in_alarm:
            print(
                f"{cursor["save"]}{cursor["line_3"]}{cursor["line_clear"]}",
                f"Aucune alarme définie.",
                f"{cursor["load"]}", sep="", end="", flush=True)
        elif alarm != unset and typing_in_alarm == False:
            print(
                f"{cursor["save"]}{cursor["line_3"]}{cursor["line_clear"]}",
                f"! Alarme définie à {alarm[0]} : {alarm[1]} : {alarm[2]} !"
                f"{cursor["load"]}", sep="", end="", flush=True)
        if alarm != unset and typing_in_alarm == False and check_alarm():
            alarm_snoozed = alarm_stopped = False            
            while alarm_stopped == False and alarm_snoozed == False:
                time.sleep(0.5)
                print(
                    f"{cursor["save"]}{cursor["line_3"]}{cursor["line_clear"]}"\
                    f"{cursor["load"]}", sep="", end="", flush=True)
                time.sleep(0.5)
                print(
                    f"{cursor["save"]}{cursor["line_3"]}{cursor["line_clear"]}",
                    f"{cursor["bold_start"]}{cursor["red_start"]}\a",
                    f"{"/!\ DRING DRING /!\ ":>30}{cursor["style_finish"]}",
                    f"{cursor["load"]}", sep="", end="", flush=True)
                if alarm_stopped:
                    alarm_reset()
                if alarm_snoozed:
                    alarm_snooze()
            alarm_snoozed = alarm_stopped = False
        if off:
            return
        time.sleep(0.9)

def display_terminal():
    terminal_page = 1
    while True:
        global off, automatic, paused, alarm_stopped, alarm_snoozed
        if terminal_page == 1:
            print(
                f"{cursor["line_5"]}{cursor["light_clear"]}",
                f"\t{cursor["bold_start"]}Commande :{cursor["bold_end"]}\n",
                f"{"pause":<18}- Met l'horloge en pause\n",
                f"{"automatique":<18}- Affiche l'heure système\n",
                f"{"manuel":<18}- Affiche l'heure personnalisée\n",
                f"{"regler":<18}- Règle une heure personnalisée\n",
                f"{"alarme":<18}- Règle une alarme\n",
                f"{"stop alarme":<18}- Arrête l'alerte de l'alarme\n"
                f"{"retarder":<18}- Ajoute 5 minutes à l'alarme\n"
                f"{"page < 1/2 >":>20}",
                sep="", end="", flush=True)
        elif terminal_page == 2:
            print(
                f"{cursor["line_5"]}{cursor["light_clear"]}",
                f"\t{cursor["bold_start"]}Commande :{cursor["bold_end"]}\n",
                f"{"reset":<18}- Réinitialise toutes les données\n",
                f"{"reset alarme":<18}- Réinitialise l'alarme\n",
                f"{"reset horloge":<18}- Réinitialise l'heure personnalisée\n",
                f"{"off":<18}- Eteint l'appareil\n",
                f"{"page < 2/2 >":>20}",
                sep="", end="", flush=True)
        commande = unidecode.unidecode(input(f"{cursor["input_commande"]}").strip(" ").lower())

        match commande:
            # page 1
            case "page 1" | "1":
                terminal_page = 1
            case "page 2" | "2":
                terminal_page = 2
            case "pause":
                if paused == False: paused = True
                elif paused: paused = False
            case "automatique" | "auto":
                automatic = True
            case "manuel":
                automatic = False
            case "regler" | "horloge":
                automatic = False
                set_clock()
            case "alarme":
                set_alarm()
            case "stop alarme" | "stop":
                alarm_stopped = True
            case "retarder" | "snooze":
                alarm_snoozed = True
            
            # page 2
            case "reset":
                reset_all()
                paused = False
                print(f"{cursor["heavy_clear"]}", end="", flush=True)
            case "reset horloge":
                clock_reset()
            case "reset alarme":
                alarm_reset()
            case "off":
                off = True
                time.sleep(1)
                print(f"{cursor["heavy_clear"]}", end="", flush=True)
                break

            # debug
            case "print":
                print(f"{cursor["line_4"]}{cursor["line_clear"]}",
                    f"{clock} {alarm}",
                    sep="", end="", flush=True)
            # else
            case _:
                continue

def reset_all():
    global custom_hours, custom_minutes, custom_seconds, alarm
    clock_reset()
    alarm_reset()

def set_clock():
    global custom_hours, custom_minutes, custom_seconds, typing_in_clock
    clock_reset()
    typing_in_clock = True
    custom_hours = str(input_values("hours", "--", "--", "--"))
    custom_minutes = str(input_values("minutes", custom_hours, "--", "--"))
    custom_seconds = str(input_values("seconds", custom_hours, custom_minutes, "--"))
    typing_in_clock = False

def clock_reset():
    global custom_hours, custom_minutes, custom_seconds
    custom_hours = custom_minutes = custom_seconds = "--"

def set_alarm():
    global alarm_hours, alarm_minutes, alarm_seconds, alarm, typing_in_alarm
    typing_in_alarm = True
    alarm_hours = str(input_values("hours", "--", "--", "--"))
    alarm_minutes = str(input_values("minutes", alarm_hours, "--", "--"))
    alarm_seconds = str(input_values("seconds", alarm_hours, alarm_minutes, "--"))
    alarm = (alarm_hours, alarm_minutes, alarm_seconds)
    alarm_hours = alarm_minutes = alarm_seconds = "--"
    typing_in_alarm = False

def alarm_reset():
    global alarm
    alarm = ("--","--","--")

def alarm_snooze():
    global alarm
    if int(alarm[1]) < 55:
        snoozed_minutes = int(alarm[1]) + 5
        snoozed_hours = alarm[0]
    else:
        snoozed_minutes = 5 - (60 - int(alarm[1]))
        snoozed_hours = int(alarm[0]) + 1
        if snoozed_hours == 24:
            snoozed_hours = "00"
    if len(str(snoozed_minutes)) == 1:
        snoozed_minutes = "0"+str(snoozed_minutes)
    alarm = ((snoozed_hours), (snoozed_minutes), (alarm[2]))

def input_values(unit, print_hours, print_minutes, print_seconds):
    if unit == "hours": unit = 0
    elif unit == "minutes": unit = 1
    elif unit == "seconds": unit = 2
    if typing_in_clock: input_type = 0
    else: input_type = 1
    print(
        f"{cursor["line_6"]}{cursor["light_clear"]}",
        f"Entrez {print_fr_unit[unit]}",
        sep="", end="", flush=True)
    while True:
        value = "--"
        print(
            f"{cursor["line_5"]}{cursor["line_clear"]}",
            f"\t{cursor["bold_start"]}{print_fr_input_type[input_type]}{cursor["bold_end"]}",
            f"{print_hours}H {print_minutes}M {print_seconds}S",
            sep="", end="", flush=True)
        value = input(f"\033[{unit_cursor_back[unit]}D").strip("- ,.")
        try: test = int(value)
        except Exception: 
            print(
                f"{cursor["line_7"]}{cursor["line_clear"]}",
                f"/!\ Entrez une valeur numérique sous la forme '00'",
                sep="", end="", flush=True)
            continue
        if 1 == len(str(value)) or len(str(value)) >=3 :
            print(
                f"{cursor["line_7"]}{cursor["line_clear"]}",
                f"/!\ Entrez une valeur constituée de 2 chiffres '00'",
                sep="", end="", flush=True)
            continue
        elif test >= unit_max_values[unit]+1:
            print(
                f"{cursor["line_7"]}{cursor["line_clear"]}",
                f"/!\ Entrez une valeur correcte à l'unité (entre 00 et {unit_max_values[unit]})",
                sep="", end="", flush=True)
            continue
        elif len(str(value)) == 2:
            print(f"{cursor["line_5"]}{cursor["light_clear"]}", end="", flush=True)
            return value

def main():
    print(f"{cursor["heavy_clear"]}", end="", flush=True)

    threading.Thread(target=define_clock).start()
    threading.Thread(target=clock_ticking).start()

    threading.Thread(target=display_terminal).start()
    time.sleep(0.5)
    threading.Thread(target=display_clock).start()
    time.sleep(0.2)
    threading.Thread(target=display_alarm).start()

main()