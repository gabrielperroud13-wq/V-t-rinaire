# Gabriel Perroud
# Veterinaire
# 2026-09-15

#Interface des Information

Titre = "INFORMATION SUR LE SPÉCIMEN"
Tiret = "-"

print(f"{Titre:-^70}")
print(f"")
Nom = str(input("Nom de l'animal : "))
Espèce = int(input("Espèce de l'animal (1 = requin, 2 = tigre, 3 = gnou) : "))
Âge = int(input("Âge de l'animal (en mois) : "))
Masse = float(input("Masse de l'animal (en livres) : "))
Température =  float(input("Tempéraure corporelle de l'animal (en °F) : "))
print(f"")
print(f"{Tiret:-^70}")
print(f"")

#Conversion des donnée

Année = (Âge // 12)
Mois = (Âge % 12)
Kilogrammes = (Masse * 0.453592)
Celsius = ((Température - 32) * 0.555555556)
Celsius2f = (f"{Celsius:.2f}")
Kilogrammes2f = (f"{Kilogrammes:.2f}")
Masse2f = (f"{Masse:.2f}")
Température2f = (f"{Température:.2f}")
Indice_de_vitalité = 100

#Varriable fixe


TEMPERATURE_MIN_REQUIN = 21.0
TEMPERATURE_MAX_REQUIN = 26.0
MASSE_MIN_REQUIN = 60.0
MASSE_MAX_REQUIN = 150.0
AGE_MIN_ADULTE_REQUIN = 60
AGE_MAX_ADULTE_REQUIN = 239


TEMPERATURE_MIN_TIGRE = 37.5
TEMPERATURE_MAX_TIGRE = 39.0
MASSE_MIN_TIGRE = 100.0
MASSE_MAX_TIGRE = 260.0
AGE_MIN_ADULTE_TIGRE = 36
AGE_MAX_ADULTE_TIGRE = 143

TEMPERATURE_MIN_GNOU = 37.5
TEMPERATURE_MAX_GNOU = 39.0
MASSE_MIN_GNOU = 120.0
MASSE_MAX_GNOU = 270.0
AGE_MIN_ADULTE_GNOU = 36
AGE_MAX_ADULTE_GNOU = 180

# #IF et ELSE et MATCH Température/Masse ET Âge ET normes T/M
from colorama import init, Fore, Back, Style
import math
match Espèce:
    case 1:
        Type_espèce = "requin"
        normesT = "21,0-26,0"
        normesM = "60,0-150,0"
        if Celsius >= TEMPERATURE_MIN_REQUIN:
            Température_C = "Bonne"
            Mesure = (math.isclose(Celsius, TEMPERATURE_MIN_REQUIN))
            if Celsius <= TEMPERATURE_MAX_REQUIN:
                Température_C = "Bonne"
                Mesure = (math.isclose(Celsius, TEMPERATURE_MAX_REQUIN))
            else:
                Température_C = "Mauvaise"
        else:
            Température_C = "Mauvaise"
        if Kilogrammes >= MASSE_MIN_REQUIN:
            Poid = "Bon"
            Mesure = (math.isclose(Kilogrammes, MASSE_MIN_REQUIN))
            if Kilogrammes <= MASSE_MAX_REQUIN:
                Poid = "Bon"
                Mesure = (math.isclose(Kilogrammes, MASSE_MAX_REQUIN))
            else:
                Poid = "Mauvais"
        else:
            Poid = "Mauvais"
        if Âge >= AGE_MIN_ADULTE_REQUIN:
            Mesure = (math.isclose(Âge, AGE_MIN_ADULTE_REQUIN))
            if Âge <= AGE_MAX_ADULTE_REQUIN:
                Type_Age = "Adulte"
                Mesure = (math.isclose(Âge, AGE_MAX_ADULTE_REQUIN))
                
            else:
                Type_Age = "Senior"
        else:
            Type_Age = "Junévile"

        Indice_de_vitalité = 100

        if (Température_C == "Mauvaise"):
            Indice_de_vitalité -= 30
            if (Poid == "Mauvais"):
                Indice_de_vitalité -= 20

        elif (Poid == "Mauvais"):
            Indice_de_vitalité -= 20
            if (Température_C == "Mauvaise"):
                Indice_de_vitalité -= 30

        if Indice_de_vitalité < 100:
            if Température_C == "Mauvaise":
                verdict = (Back.RED + "URGENT" + Style.RESET_ALL)
            else:
                verdict = (Back.YELLOW + "SURVEILLANCE" + Style.RESET_ALL)
        else:
            verdict = (Back.GREEN + "NORMAL" + Style.RESET_ALL)

    case 2:
        Type_espèce = "tigre"
        normesT = "37,5-39,0"
        normesM = "100,0-260,0"
        if Celsius >= TEMPERATURE_MIN_TIGRE:
            Température_C = "Bonne"
            Mesure = (math.isclose(Celsius, TEMPERATURE_MIN_TIGRE))
            if Celsius <= TEMPERATURE_MAX_TIGRE:
                Température_C = "Bonne"
                Mesure = (math.isclose(Celsius, TEMPERATURE_MAX_TIGRE))
            else:
                Température_C = "Mauvaise"
        else:
            Température_C = "Mauvaise"
        if Kilogrammes >= MASSE_MIN_TIGRE:
            Poid = "Bon"
            Mesure = (math.isclose(Kilogrammes, MASSE_MIN_TIGRE))
            if Kilogrammes <= MASSE_MAX_TIGRE:
                Poid = "Bon"
                Mesure = (math.isclose(Kilogrammes, MASSE_MAX_TIGRE))
            else:
                Poid = "Mauvais"
        else:
            Poid = "Mauvais"
        if Âge >= AGE_MIN_ADULTE_TIGRE:
            Mesure = (math.isclose(Âge, AGE_MIN_ADULTE_TIGRE))
            if Âge <= AGE_MAX_ADULTE_TIGRE:
                Type_Age = "Adulte"
                Mesure = (math.isclose(Âge, AGE_MAX_ADULTE_TIGRE))
            else:
                Type_Age = "Senior"
        else:
            Type_Age = "Junévile"

        Indice_de_vitalité = 100

        if (Température_C == "Mauvaise"):
            Indice_de_vitalité -= 30
            if (Poid == "Mauvais"):
                Indice_de_vitalité -= 20

        elif (Poid == "Mauvais"):
            Indice_de_vitalité -= 20
            if (Température_C == "Mauvaise"):
                Indice_de_vitalité -= 30
        if Indice_de_vitalité < 100:
            if Température_C == "Mauvaise":
                if Poid == "Mauvais":
                    verdict = (Back.RED + "URGENT" + Style.RESET_ALL)
            else:
                verdict = (Back.YELLOW + "SURVEILLANCE" + Style.RESET_ALL)
            if Poid == "Mauvais":
                if Température_C == "Mauvaise":
                    verdict = (Back.RED + "URGENT" + Style.RESET_ALL)
            else:
                verdict = (Back.YELLOW + "SURVEILLANCE" + Style.RESET_ALL)
        else:
            verdict = (Back.GREEN + "NORMAL" + Style.RESET_ALL)  

    case 3:
        Type_espèce = "gnou"
        normesT = "37,5-39,0"
        normesM = "120,0-270,0"
        if Celsius >= TEMPERATURE_MIN_GNOU:
            Température_C = "Bonne"
            Mesure = (math.isclose(Celsius, TEMPERATURE_MIN_GNOU))
            if Celsius <= TEMPERATURE_MAX_GNOU:
                Température_C = "Bonne"
                Mesure = (math.isclose(Celsius, TEMPERATURE_MAX_GNOU))
            else:
                Température_C = "Mauvaise"
        else:
            Température_C = "Mauvaise"
        if Kilogrammes >= MASSE_MIN_GNOU:
            Poid = "Bon"
            Mesure = (math.isclose(Kilogrammes, MASSE_MIN_GNOU))
            if Kilogrammes <= MASSE_MAX_GNOU:
                Poid = "Bon"
                Mesure = (math.isclose(Kilogrammes, MASSE_MAX_GNOU))
            else:
                Poid = "Mauvais"
        else:
            Poid = "Mauvais"
        if Âge >= AGE_MIN_ADULTE_GNOU:
            Mesure = (math.isclose(Âge, AGE_MIN_ADULTE_GNOU))
            if Âge < AGE_MAX_ADULTE_GNOU:
                Type_Age = "Adulte"
                Mesure = (math.isclose(Âge, AGE_MAX_ADULTE_GNOU))
            else:
                Type_Age = "Senior"
        else:
            Type_Age = "Junévile"

        Indice_de_vitalité = 100

        if (Température_C == "Mauvaise"):
            Indice_de_vitalité -= 30
            if (Poid == "Mauvais"):
                Indice_de_vitalité -= 20

        elif (Poid == "Mauvais"):
            Indice_de_vitalité -= 20
            if (Température_C == "Mauvaise"):
                Indice_de_vitalité -= 30

        if Indice_de_vitalité < 100:
            if Température_C == "Mauvaise":
                if Poid == "Mauvais":
                    verdict = (Back.RED + "URGENT" + Style.RESET_ALL)
            else:
                verdict = (Back.YELLOW + "SURVEILLANCE" + Style.RESET_ALL)
            if Poid == "Mauvais":
                if Température_C == "Mauvaise":
                    verdict = (Back.RED + "URGENT" + Style.RESET_ALL)
                elif Type_Age == "Senior":
                    verdict = (Back.RED + "URGENT" + Style.RESET_ALL)
            else:
                verdict = (Back.YELLOW + "SURVEILLANCE" + Style.RESET_ALL)
        else:
            verdict = (Back.GREEN + "NORMAL" + Style.RESET_ALL)  

if Espèce >= 4:
    Type_espèce = "ERREUR"
    Température_C = "ERREUR"
    Poid = "ERREUR"
    Type_Age = "ERREUR"
    normesM = "ERREUR"
    normesT = "ERREUR"
    verdict = "ERREUR"
    Mesure = "ERREUR"
elif Espèce <= 0:
    Type_espèce = "ERREUR"
    Température_C = "ERREUR"
    Poid = "ERREUR"
    Type_Age = "ERREUR"
    normesM = "ERREUR"
    normesT = "ERREUR"
    verdict = "ERREUR"
    Mesure = "ERREUR"


if Mesure == True:
    Mesure_Verdict = "oui"
elif Mesure == False:
    Mesure_Verdict = "non"
elif Mesure == "ERREUR":
    Mesure_Verdict = "ERREUR"

# Interface des données


LigneÉgal = "="
Nom_Bâtiment = "CLINIQUE VÉTÉRINAIRE EXOTIQUE"
Lieux_Bâtiment = "DES ÎLES ST-MAURICE"

print(f"{LigneÉgal:=^70}")
print(f"{Nom_Bâtiment:^70}")
print(f"{Lieux_Bâtiment:^70}")
print(f"{LigneÉgal:=^70}")
print(f"{"Patient":<18}: {Nom} ({Type_espèce})")
print(f"{"Âge":<18}: {Année} ans et {Mois} mois ({Type_Age})")
print(f"{"Saisie":<18}: masse en lbs, température en °F")
print(f"{"Date":<18}: ")
print(f"{Tiret:-^80}")
print(f"{"Mesure":<30}{"Valeur":>20}{"":>5}{"Norme"}")
print(f"{"Température (°C)":<30}{Celsius2f:>20}{"":>5}{normesT}")
print(f"{"Masse (kg)":<30}{Kilogrammes2f:>20}{"":>5}{normesM}")
print(f"{Tiret:-^80}")
print(f"Conversions")
print(f"{"Masse":<15}:{Masse2f:>10} lbs ={Kilogrammes2f:>10} kg")
print(f"{"Température":<15}:{Température2f:>10} °F  ={Celsius2f:>10} °C")
print(f"{Tiret:-^80}")
print(f"{"Mesure à la limite":<30}: {Mesure_Verdict}")
print(f"{Tiret:-^80}")
print(f"Indice de vitalité : {Indice_de_vitalité} / 100")
print(f"VERDICT : {verdict}")
print(f"{LigneÉgal:=^80}")


#Verdict/Mesure ne semble pas marcher
#Problène Verdict trouvé
#Reste a faire Date