import time
import datetime
import keyboard

def get current_time():*


def set_time():
    """Demande à l'utilisateur de définir une heure personnalisée."""
    hour = int(input("Enter the hours (0-23): "))
    minute = int(input("Enter the minutes (0-59): "))
    second = int(input("Enter the seconds (0-59): "))
    return hour, minute, second


def set_alarm():
    """Demande à l'utilisateur de définir une alarme."""
    alarm_hours = int(input("Enter alarm hours (0-23): "))
    alarm_minutes = int(input("Enter alarm minutes (0-59): "))
    alarm_seconds = int(input("Enter alarm seconds (0-59): "))
    return alarm_hours, alarm_minutes, alarm_seconds


def choose_alarm():
    """Demande si l'utilisateur veut définir une alarme."""
    return input("Do you want to set an alarm? (yes/no): ").strip().lower()


def display_time(current_time, message, alarm_str):
    """Affiche l'heure actuelle avec un message ou l'alarme."""
    current_time_str = f"{current_time[0]:02}:{current_time[1]:02}:{current_time[2]:02}"
    if alarm_str:
        print(f"\r{current_time_str} {alarm_str} {message}", end="")
    else:
        print(f"\r{current_time_str} {message}", end="")


def display_alarm(current_time, alarm):
    """Déclenche l'alarme si l'heure actuelle correspond à l'heure définie."""
    if current_time == alarm:
        return "Ring ring! Ring ring!"
    return ""


def main():
    # Initialisation
    is_paused = False
    alarm = None
    alarm_str = ""
    
    # Choisir une alarme
    if choose_alarm() == "yes":
        alarm = set_alarm()
        alarm_str = f"alarm: {alarm[0]:02}:{alarm[1]:02}:{alarm[2]:02}"

    print("\nAppuyez sur 'p' pour mettre en pause ou reprendre, 'q' pour quitter.")

    while True:
        try:
            # Pause/reprise de l'horloge
            if keyboard.is_pressed("p"):
                is_paused = not is_paused
                print("\nHorloge mise en pause." if is_paused else "\nHorloge relancée.")
                time.sleep(1)  # Eviter les activations multiples

            # Quitter le programme
            if keyboard.is_pressed("q"):
                print("\nProgramme arrêté.")
                break

            # Afficher l'heure si l'horloge n'est pas en pause
            if not is_paused:
                clock = datetime.datetime.now()
                current_time = (clock.hour, clock.minute, clock.second)

                # Gérer l'alarme
                message = display_alarm(current_time, alarm)
                display_time(current_time, message, alarm_str)

                # Arrêter l'alarme en appuyant sur 's'
                if message:
                    print("\nDring Dring Dring! Appuyez sur 's' pour arrêter l'alarme.")
                    while True:
                        if keyboard.is_pressed("s"):
                            print("\nAlarme arrêtée.")
                            alarm = None  # Réinitialiser l'alarme
                            alarm_str = ""
                            break

            time.sleep(1)

        except KeyboardInterrupt:
            print("\nProgramme interrompu par l'utilisateur.")
            break


main()
