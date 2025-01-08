# Import des librairies nécessaires
import datetime, time, threading

jour = ('Dimanche', 'Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi')
mois = (None, 'Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre')

stop = 0
mode = 1
unité = ["l'heure", "l'heure", "les minutes", "les secondes", "AM / PM"]
unité_b = [11,11,7,3]
unité_max = [12,23,60,60]
alarme = ["__","__","__","__","__"]

ansi_line1 = "\033[s\033[H\033[2K"

# Définition des fonctions clés
def afficher_date():
    calendrier = (jour[int(datetime.datetime.now().strftime("%w"))], datetime.datetime.now().strftime("%d"), mois[int(datetime.datetime.now().strftime("%m"))])
    return calendrier

def afficher_heure():
    horloge = (datetime.datetime.now().strftime("%I"), datetime.datetime.now().strftime("%H"), datetime.datetime.now().strftime("%M"), datetime.datetime.now().strftime("%S"), datetime.datetime.now().strftime("%p"))
    return horloge

def afficher_alarme():
    if alarme[0] != "__" and mode%2==1:
        print(f"\033[s\033[H\n\033[2K! Alarme définie pour {alarme[1]}:{alarme[2]}:{alarme[3]} !\033[u", end="", flush=True)
    elif alarme[0] != "__" and mode%2==0:
        print(f"\033[s\033[H\n\033[2K! Alarme définie pour {alarme[0]}:{alarme[2]}:{alarme[3]} {alarme[4]} !\033[u", end="", flush=True)
    else: print(f"\033[s\033[H\n\033[2KAucune alarme définie.\033[u", end="", flush=True)


def affichage():
    while True:
        if mode%2 == 0:
            print(f"{ansi_line1}{afficher_date()[0]} {afficher_date()[1]} {afficher_date()[2]}   \
{afficher_heure()[0]} : {afficher_heure()[2]} : {afficher_heure()[3]} {afficher_heure()[4]}\033[u", end="", flush=True)
        if mode%2 == 1:
            print(f"{ansi_line1}{afficher_date()[0]} {afficher_date()[1]} {afficher_date()[2]}   \
{afficher_heure()[1]} : {afficher_heure()[2]} : {afficher_heure()[3]}\033[u", end="", flush=True)
        time.sleep(0.99)
        if stop == 1:
            time.sleep(1)
            print(f"\033[H\033[2J", end="")
            return

def alerte():
    global alarme
    while True:
        if alarme[0] != "__":
            if afficher_heure()[int(mode%2)] == alarme[int(mode%2)] and afficher_heure()[2] == alarme[2] and afficher_heure()[3] == alarme[3]:
                print(f"\033[s\033[H\033[1A\033[2KRINGGGGG\033[u", end="", flush=True)
                time.sleep(5)
                alarme = ["__","__","__","__","__"]
                afficher_alarme()
        if stop == 1 or alarme[0] == "__":
            return
        time.sleep(0.2)

def terminal():
    while True:
        global mode, stop
        commande = input(f"\033[H\033[3B\033[0JCommande : ")
        if commande == "mode":
            mode +=1
            afficher_alarme()
            continue
        if commande == "alarme":
            lancer_alarme()
            threading.Thread(target=alerte).start()
        if commande == "stop":
            stop +=1
            break
        else: continue

def lancer_alarme():
    if vérifier_alarme(int(mode%2)) == 0:
        return
    vérifier_alarme(2)
    vérifier_alarme(3)
    if mode%2 == 0:
        print(f"\033[H\033[4B\033[2KEntrez {unité[4]}", end="")
        while True:
            alarme[4] = input(f"\033[H\033[3B\033[2KAlarme : {alarme[0]}H {alarme[2]}M {alarme[3]}S __\033[2D").strip(" ").upper()
            if alarme[4] not in ("AM", "PM"):
                continue
            else: break
        if alarme[4] == "PM" and str(alarme[0]) != "12":
            alarme[1] = str(int(alarme[0])+12)
        elif alarme[4] == "AM" and str(alarme[0]) == "12":
            alarme[1] = "00"
        else: alarme[1] = alarme[0]
    if mode%2 == 1:
        if alarme[1] == "00": alarme[0] = "12"; alarme[4] = "AM"
        elif 12 < int(alarme[1]) < 22:
            alarme[0] = "0"+str(int(alarme[1])-12)
            alarme[4] = "PM"
        elif 21 < int(alarme[1]):
            alarme[0] = int(alarme[1])-12
            alarme[4] = "PM"
        else: 
            alarme[0] = alarme[1]
            alarme[4] = "AM"
    print(f"\033[H\033[3B\033[0J", end="")
    afficher_alarme()

def vérifier_alarme(valeur):
    global alarme, unité
    print(f"\033[H\033[4B\033[2KEntrez {unité[valeur]}")
    while True:
        alarme[valeur] = "__"
        alarme[valeur] = input(f"\033[H\033[3B\033[2KAlarme : {alarme[int(mode%2)]}H {alarme[2]}M {alarme[3]}S\033[{unité_b[valeur]}D").strip("- ,.")
        # if not alarme[0] and not alarme[1]:
        #     choix = input(f"\033[2K\033[F\033[2KAnnuler l'alarme ? o/n \n").strip().lower()
        #     if choix in ('o', 'oui'):
        #         print(f"\033[F\033[2K", end="")
        #         return 0
        #     else: continue
        try: test = int(alarme[valeur])
        except Exception: 
            print("\033[H\033[5B\033[2K/!\ Entrez une valeur numérique sous la forme '00'", end="")
            continue
        if 1 == len(str(alarme[valeur])) or len(str(alarme[valeur])) >=3 :
            print("\033[H\033[5B\033[2K/!\ Entrez une valeur constituée de 2 chiffres '00'", end="")
            continue
        elif test >= unité_max[valeur]+1:
            print(f"\033[H\033[5B\033[2K/!\ Entrez une valeur correcte à l'unité (entre 00 et {unité_max[valeur]})", end="")
            continue
        elif len(str(alarme[valeur])) == 2:
            print(f"\033[H\033[3B\033[0J", end="")
            return 1


print(f"\033[H\033[2J", end="")
print(f"\n\033[mAucune alarme définie.\033[25m", end="")
threading.Thread(target=terminal).start()
threading.Thread(target=affichage).start()