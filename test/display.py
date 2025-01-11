#TODO variable for each line (l) + the "clear line" separated + the "save cursor"

#TODO display available commands

#TODO center the display

# ANSI codes
dic_cursor = {
    "delete_line_1-clock": "\033[s\033[H\033[2K",
    "delete_line_2-alarm": "\033[s\033[H\033[1B\033[2K",
    "delete_line_3-message": "\033[H\033[2B\033[2K",
    "delete_line_4-command": "\033[H\033[3B\033[2K",
    "delete_line_5-input": "\033[H\033[4B\033[2K",
    "delete_line_6-error": "\033[H\033[5B\033[2K",

    "cursor_position_load": "\033[u",

    "cursor_move_left_2": "\033[2D",
    "cursor_move_left_8": "\033[8D",

    "delete_line": "\033[2K",
    "delete_all_after_position": "\033[0J",
    "delete_all": "\033[H\033[0J"
}

# Special actions
def all_clear():
    print(dic_cursor["delete_all"], end="")

# Line 1 - Clock
def clock_12h(clock_time):
    print(f"{dic_cursor["delete_line_1-clock"]}{clock_time.ampm_hour}:{clock_time.clock[1]}:{clock_time.clock[2]} {clock_time.format}{dic_cursor["cursor_position_load"]}", end="", flush=True)

def clock_24h(clock_time):
    print(f"{dic_cursor["delete_line_1-clock"]}{clock_time.clock[0]}:{clock_time.clock[1]}:{clock_time.clock[2]}{dic_cursor["cursor_position_load"]}", end="", flush=True)

# Line 3 - Message

def message_clock_valid():
    print(f"{dic_cursor["delete_line_3-message"]}Horloge changé avec succes!{dic_cursor["cursor_position_load"]}", end="")

def message_stop():
    print(f"{dic_cursor["delete_line_3-message"]}Horloge stoppé.", end="") #ZA WARUDO!!!

def message_start():
    print(f"{dic_cursor["delete_line_3-message"]}Horloge redémarré.", end="") #TOKI WO UGOKIDASU.

def message_help():
    print(f"{dic_cursor["delete_line_3-message"]}\"horloge\"\"alarme\"\"stop\"\"demarrer\"\"aide\"\"quitter\"", end="") #TOKI WO UGOKIDASU.

def message_byebye():
    print(f"{dic_cursor["delete_line_3-message"]}Le programme va quitter...", end="") #My final message.


# Line 4 - Commands
def input_command():
    input(f"{dic_cursor["delete_line_4-command"]}{dic_cursor["delete_all_after_position"]}Commande : ")

# Line 5 - Input
def input_clock_config():
    input(f"{dic_cursor["delete_line_5-input"]}{dic_cursor["delete_all_after_position"]}Configurer l'heure en: (M)anuel, (A)uto? ").lower()

def input_user_clock():
    input(f"{dic_cursor["delete_line_5-input"]}Veuillez entrer l'heure au format hh:mm:ss : ________{dic_cursor["cursor_move_left_8"]}").strip(" :.,/")

def input_user_format(user_clock):
    input(f"{dic_cursor["delete_line_5-input"]}Veuillez entrer AM ou PM : {user_clock[:2]}:{user_clock[2:4]}:{user_clock[4:]} __{dic_cursor["cursor_move_left_2"]}").upper()
# Line 6 - Errors
def error_invalid_time():
    print(f"{dic_cursor["delete_line_6-error"]}/!\Entrer une heure valide! (00-23):(00-59):(00-59)")

def error_NaN():
    print(f"{dic_cursor["delete_line_6-error"]}/!\Enter uniquement des chiffres!")

def error_number_length():
    print(f"{dic_cursor["delete_line_6-error"]}/!\Enter exactement 6 chiffres au total!")

def error_format():
    print(f"{dic_cursor["delete_line_6-error"]}/!\Enter AM ou PM!")




