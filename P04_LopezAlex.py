from datetime import datetime
import random, time

def main():
    print("-------------------Menú---------------------")
    print("1. Motion sensor ")
    print("2. Temperature camera")
    print("3. Automatic sprinklers")
    print("4. Security cameras")
    print("5. Exit")
    print()

def menu_habitacions():
    print(f"Per activar-ho has d'introduir el numero d'habitació")
    time.sleep (0.5)
    print()
    print("0. Totes les habitacions")
    print("1. Menjador ")
    print("2. Cuina")
    print("3. Lavabo")
    print("4. Habitació")
    print("5. Sortir")
    print()

def motion_escollir( living_room, kitchen, bathroom, bedroom, sortir):
    while not sortir:
        escull = str(input("A quin sensor vols cambiar l'estat? "))
        match escull:
            case "0":
                time.sleep (0.5)
                living_room = not living_room
                kitchen = not kitchen
                bathroom = not bathroom
                bedroom = not bedroom
                if living_room == True and kitchen == True and bathroom == True and bedroom == True:
                    print ("Tots els sensors estan activats a les habitacions.")
                    time.sleep (0.5)
                else:
                    sortir = False
                    living_room = False
                    kitchen = False
                    bathroom = False 
                    bedroom = False
                    print ("Tots els sensors estan desactivats a les habitacions")
                    time.sleep (0.5)
            case "1":
                time.sleep (0.5)
                living_room = not living_room
                if living_room == True:
                    print ("S'ha activat el sensor al menjador.")
                    time.sleep (0.5)
                else:
                    print ("S'ha desactivat el sensor al menjador.")
                    time.sleep (0.5)
            case "2":
                time.sleep (0.5)
                kitchen = not kitchen
                if kitchen == True:
                    print ("S'ha activat el sensor a la cuina.")
                    time.sleep (0.5)
                else:
                    print ("S'ha desactivat el sensor a la cuina")
                    time.sleep (0.5)
            case "3":
                time.sleep (0.5)
                bathroom = not bathroom
                if bathroom == True:
                    print ("S'ha activat el sensor al lavabo.")
                    time.sleep (0.5)
                else:
                    print ("S'ha desactivat el sensor al lavabo")
                    time.sleep (0.5)
            case "4":
                time.sleep (0.5)
                bedroom = not bedroom
                if bedroom == True:
                    print ("S'ha activat el sensor a l'habitació.")
                    time.sleep (0.5)
                else:
                    print ("S'ha desactivat el sensor a l'habitació.")
                    time.sleep (0.5)
            case "5":
                time.sleep (0.5)
                print ("Sortint...")
                time.sleep (0.5)
                sortir = True
                
            case _:
                print ()
                print ("Opció no valida")
                time.sleep (0.5)
    return living_room, kitchen, bathroom, bedroom, sortir

def motion_deteccio(hora, living_room, kitchen, bathroom, bedroom):
    time.sleep(0.5)
    num_aleatori= 0
    num_aleatori = random.randint (0, 100)
    if num_aleatori < 25 and living_room == True:
        print (f"Els sensors han detectat moviment al Menjador a les \033[31m{hora}\033[0m")
    elif num_aleatori > 25 and num_aleatori < 50 and kitchen == True:
        print (f"Els sensors han detectat moviment a la Cuina a les \033[31m{hora}\033[0m")
    elif num_aleatori > 50 and num_aleatori < 75 and bathroom == True:
        print (f"Els sensors han detectat moviment al Lavabo a les \033[31m{hora}\033[0m")
    elif num_aleatori > 75 and bedroom == True:
        print (f"Els sensors han detectat moviment a l'Habitació a les \033[31m{hora}\033[0m")
    else:
        print (f"No s'ha detectat cap moviment")

def temperature_escollir (living_room, kitchen, bathroom, bedroom, sortir):
    while sortir == False:
        escull = str(input("A quin sensor vols cambiar l'estat? "))
        match escull:
            case "0":
                time.sleep (0.5)
                print ("Aquesta opció queda excluida del menu en la Temperature Camera")
            case "1":
                time.sleep (0.5)
                living_room = not living_room
                if living_room == True:
                    print ("S'ha activat la camara al menjador.")
                    time.sleep (0.5)
                else:
                    print ("S'ha desactivat la camara al menjador.")
                    time.sleep (0.5)
            case "2":
                time.sleep (0.5)
                kitchen = not kitchen
                if kitchen == True:
                    print ("S'ha activat la camara a la cuina.")
                    time.sleep (0.5)
                else:
                    print ("S'ha desactivat la camara a la cuina")
                    time.sleep (0.5)
            case "3":
                time.sleep (0.5)
                bathroom = not bathroom
                if bathroom == True:
                    print ("S'ha activat la camara al lavabo.")
                    time.sleep (0.5)
                else:
                    print ("S'ha desactivat la camara al lavabo")
                    time.sleep (0.5)
            case "4":
                time.sleep (0.5)
                bedroom = not bedroom
                if bedroom == True:
                    print ("S'ha activat la camara a l'habitació.")
                    time.sleep (0.5)
                else:
                    print ("S'ha desactivat la camara a l'habitació.")
                    time.sleep (0.5)
            case "5":
                time.sleep (0.5)
                print ("Sortint...")
                time.sleep (0.5)
                sortir = True
                return living_room, kitchen, bathroom, bedroom, sortir
            case _:
                print ()
                print ("Opció no valida")
                time.sleep (0.5)

def temperatura_deteccio(hora, living_room, kitchen, bathroom, bedroom):
    time.sleep (0.5)
    num_aleatori = 0
    num_aleatori = round (random.uniform (10,20), 2)
    if living_room == True:
        num_aleatori = round (random.uniform (10,20), 2)
        print (f"El menjador te una temperatura de \033[31m{num_aleatori}º graus.\033[0m ")
        time.sleep (0.5)
    if kitchen == True:
        num_aleatori = round (random.uniform (10,20), 2)
        print (f"La cuina te una temperatura de \033[31m{num_aleatori}º graus.\033[0m ")
        time.sleep (0.5)
    if bathroom == True:
        num_aleatori = round (random.uniform (10,20), 2)
        print (f"El lavabo te una temperatura de \033[31m{num_aleatori}º graus.\033[0m ")
        time.sleep (0.5)
    if bedroom == True:
        num_aleatori = round (random.uniform (10,20), 2)
        print (f"L'habitació te una temperatura de \033[31m{num_aleatori}º graus.\033[0m ")
        time.sleep (0.5)
    else:
        time.sleep (0.5)
        print ("Cap habitació te encesa la camera.")
if __name__ == "__main__":
    sortir_menu_principal = False
    #MOTION SENSOR
    ms_sortir = False
    ms_living_room = False
    ms_kitchen = False
    ms_bathroom = False 
    ms_bedroom = False
    #TEMPERATURE CAMERA
    tc_sortir = False
    tc_living_room = False
    tc_kitchen = False
    tc_bathroom = False 
    tc_bedroom = False
    opcio = 0
    while not sortir_menu_principal:
        main()
        opcio = str(input("Quina opció vols escollir? "))

        match opcio:
            case "1":
                hora = datetime.now().strftime ("%H:%M:%S") #He cercat per internet per saber aquesta funcio de la llibreria
                print ()
                menu_habitacions ()
                ms_living_room, ms_kitchen, ms_bathroom, ms_bedroom, ms_sortir = motion_escollir(ms_living_room, ms_kitchen, ms_bathroom, ms_bedroom, ms_sortir)
                motion_deteccio(hora, ms_living_room, ms_kitchen, ms_bathroom, ms_bedroom)
            case "2":
                print ()
                menu_habitacions ()
                tc_living_room, tc_kitchen, tc_bathroom, tc_bedroom, tc_sortir = temperature_escollir (tc_living_room, tc_kitchen, tc_bathroom, tc_bedroom, tc_sortir)
                temperatura_deteccio (tc_living_room, tc_kitchen, tc_bathroom, tc_bedroom, tc_sortir)
            case "3":
                print ("Proximament...")
            case "4":
                print ("Proximament...")
            case "5":
                print ("Sortint del menu principal...")
                sortir_menu_principal = True
            case _:
                print ()
                print ("Opció no valida")

