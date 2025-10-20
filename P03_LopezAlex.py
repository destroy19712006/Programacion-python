# Prefereixo fer el codi amb el def, s'em fa més facil i mes "ameno" que fer-ho tot amb el match .El carles m'ha dit que si

import time
if __name__ == "__main__":
    print ("Has iniciat el Control de salut")

ANY_ACTUAL:int = 2025 #no es com una contsant en realitat pero si a la vegada
nom = ""
cognom = ""
edat = 0
pes = 0.0
altura = 0.0

#GLOBAL EN NUEVAS FUNCIONES Y CALCAR EL INTRODUCIR DATOS AL MODIFICAR!!!!!!!!!
def ensenyar_menu():
    print ()
    time.sleep (0.3)
    print ( "---------- Menú Personal ----------")
    print ( "1.) Introduir dades")
    print ( "2.) Modificar dades")
    print ( "3.) Visualitzar dades")
    print ( "4.) Sortir")
    print ("------------------------------------")

def introduir_dades():
    print()
    time.sleep(0.5)
    global nom, cognom, pes, altura, edat # He cercat informació i es per definir una variable en tot el codi i no nomes en aquesta funció el problema es que no em deixa especificar tipus de la variable
    
    nom = str (input("Intrdueix el teu nom: ")).strip()#str
    
    
    if not nom:
        time.sleep (0.3)
        print ("Has de introduir un nom. \nTornant al menú...")
        time.sleep (0.3)
        return
    elif nom.isdigit():
        print ("No s'admeten valors numerics")
        return
    elif len(nom) <= 1:
        print ("El nom ha de tenir més d'un caracter. \nTornant al menú...")
        time.sleep (0.3)
        return
    time.sleep (0.2)
    cognom = input ("Intrdueix el teu cognom: ")#str
    if not cognom:
        time.sleep (0.3)
        print ("Has de introduir un cognom. \nTornant al menú...")
        time.sleep (0.3)
        return
    elif cognom.isdigit():
        ("No s'admeten valors numerics")
        return
    elif len(cognom) <= 1:
        print ("El cognom ha de tenir més d'un caracter")
        time.sleep (0.3)
        return
    time.sleep (0.2)
    def obtener_edad(): #He preguntat a chat si es podia crear funcions dintre de funcions
        global nom, cognom, pes, altura, edat
        try:    
            edat = int(input ("Quina edat tens? "))#int
        except ValueError:
            time.sleep (0.5)
            print ("No es un caracter valid, torna-hi a provar...")
            time.sleep (0.5)
            return obtener_edad ()
        if edat < 12 or edat > 120: # He posat 12 anys perque un nen més petit no tindria tanta comprensio lectora per aixi dir-ho
            time.sleep (0.5)
            print ("Has d'introduir una edat que estigui dintre del varem \nentre 12 y 120")
            time.sleep (0.5)
            return obtener_edad ()
    
    obtener_edad ()
    
    def obtener_pes ():
        global nom, cognom, pes, altura, edat
        try:
            time.sleep (0.2)
            pes = float(input ("Introdueix el teu pes en kg: "))#float
            time.sleep (0.2)
        except ValueError:
            print ("No es un valor valid, torna-hi a provar...")
            return obtener_pes ()
        if pes <= 36 or pes >= 400: #36 es el pes promedi d'un nen de 12 anys
            print ("Has de posar un pes entre el varem de 36 Kg - 400 Kg. \nTorna-hi a provar...")
            return obtener_pes ()
    
    obtener_pes ()
    
    def obtener_altura ():
        global nom, cognom, pes, altura, edat
        try:
            time.sleep (0.3)
            altura = float(input ("Intrdueix la teva alçada en metres: "))#float
            time.sleep (0.5)
        except ValueError:
            print ("No es un valor valid, torna-hi a provar...")
            return obtener_altura ()
        if altura < 0.5 or altura > 2.5:
            print ("Introdeix la teva alçada entre el varem de 0.5m - 2.5m")
            return obtener_altura
    
    obtener_altura ()
    
    print ("Guardant les dades...")
    time.sleep (1)
    print ("Les teves dades s'han guardat correctament!")
    time.sleep (0.5)
    altura = round (altura, 2)
    pes = round (pes, 2)

def modificar_dades():
    global nom, cognom, pes, altura, edat 
    print()
    if nom == "":
        time.sleep(0.5)
        print ("Has de introduir dades primer!")
    else:
        print ("Has escollit: Modificar dades")
        nom_mod = input ("Introdueix el teu nom: ")#str
        time.sleep (0.2)
        if nom.isdigit():
            print ("No s'admeten valors numerics")
            return
        elif len(nom) <= 1:
            print ("El nom ha de tenir més d'un caracter")
            time.sleep (0.3)
            return
        if nom_mod != nom:
            nom = nom_mod

        cognom_mod = input ("Introdueix el teu cognom: ")#str
        time.sleep (0.2)
        if cognom.isdigit():
            print ("No s'admeten valors numerics")
        elif len(cognom) <= 1:
            print ("El nom ha de tenir més d'un caracter")
            time.sleep (0.3)
            return
        if cognom_mod != cognom:
            cognom = cognom_mod

    def obtener_edat_mod():
        global nom, cognom, pes, altura, edat
        
        time.sleep (0.2)
        try:
            edat_mod = int(input("Quina edat tens? "))#int
        except ValueError:
            print ("No es un valor valid. Torna-hi a provar... ")
            return obtener_edat_mod ()
        if edat_mod < 12 or edat_mod > 120: # He posat 12 anys perque un nen més petit no tindria tanta comprensio lectora per aixi dir-ho
            time.sleep (0.5)
            print ("Has d'introduir una edat que estigui dintre del varem \nentre 12 y 120")
            time.sleep (0.5)
            return obtener_edat_mod ()
        else:
            edat = edat_mod

    obtener_edat_mod()

    def obtener_pes_mod ():
        global nom, cognom, pes, altura, edat
        time.sleep (0.2)
        try:
            pes_mod = float(input ("Introdueix el teu pes en kg: "))#float
        except ValueError:
            print ("No es un valor valid. Torna-hi a provar... ")
            return obtener_pes_mod ()
        if pes_mod <= 36 or pes_mod >= 400: 
            print ("Has de posar un pes entre el varem de 36 Kg - 400 Kg. \nTorna-hi a provar...")
            return obtener_pes_mod ()
        else:
            pes = pes_mod
        time.sleep (0.2)

    obtener_pes_mod ()

    def obtener_altura_mod():
        global nom, cognom, pes, altura, edat
        try:
            altura_mod = float(input ("Introdueix la teva alçada en metres: "))#float
        except ValueError:
            print ("No es un valor valid. Torna-hi a provar... ")
            return obtener_altura_mod ()
        if altura_mod < 0.5 or altura_mod > 2.5:
            print ("Introdeix la teva alçada entre el varem de 0.5m - 2.5m")
            return obtener_altura_mod
        else:
            altura = altura_mod
    obtener_altura_mod()
    
    time.sleep (0.5)
    print ("Guardant les dades...")
    time.sleep (1)
    print ("Les teves dades s'han guardat correctament!")



def visualitzar_dades():
    
    print()
    time.sleep(0.5)
    print ("Has triat: Visualitzar dades")
    try:
        imc = pes / (altura**2)
    except ZeroDivisionError:
        print ("Eror de divisio")
    freq_cardiaca = 220 - edat
    zona_objectiu1 = freq_cardiaca * 0.5
    zona_objectiu2 = freq_cardiaca * 0.85
    zona_objectiu1 = round (zona_objectiu1, 0)
    zona_objectiu2 = round (zona_objectiu2, 0)
    aiguaml = 35 * pes
    aigua = aiguaml / 1000
    aigua = round (aigua, 2)
    imc = round (imc, 2)
    any_naixament = ANY_ACTUAL - edat
    if imc < 18.5:
        imc_categoria = ("Un pes baix")
    elif imc > 18.5 and imc < 24.9:
        imc_categoria = ("Un pes normal")
    elif imc > 25 and imc < 29.9:
            imc_categoria = ("Sobrepès")
    else:
        imc_categoria = ("Obesitat")
        #Tabla de resumen
    time.sleep (0.5)
    print ("Carregant les teves dades")
    time.sleep (1)
    print (f"Hola {nom.capitalize()} a continuació tindras un resumen de les teves dades:")
    print ("-----------------------------------------------")
    print (f"El teu nom complet és: {nom.capitalize()} {cognom.capitalize()}")
    print (f"Edat: {edat} anys | Pes: {pes}kg | Alçada: {altura}m")
    print (f"Index de Masa Corporal (IMC): {imc}, Tens {imc_categoria}")
    print (f"La freqüencia cardiaca màxima estimada és {freq_cardiaca}bpm i la teva zona objectiu es entre {zona_objectiu1}-{zona_objectiu2}")
    print (f"Aigua recomenada: {aigua}L ")
    print (f"Any de naixament aproximat: {any_naixament}")
    print ("-----------------------------------------------")

time.sleep (1)
print ("Carregant menu...")
while True:
    time.sleep (0.5)
    ensenyar_menu()
    opcio = input ("Tria una opció (1-4): ")
    
    match opcio:
        case "1":
            print ("Has escollit: Introduir dades  ")
            time.sleep (0.5)
            introduir_dades()
        case "2":
            modificar_dades()
        case "3":
            visualitzar_dades()
        case "4":
            time.sleep(2)
            print ("Sortint del programa...")
            time.sleep(0.5)
            break
        case _:
            print ("Opcio no valida, torna-ho a provar")