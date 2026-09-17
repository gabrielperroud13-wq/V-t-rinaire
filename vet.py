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

#Stupide Varriable fixe qui a du refaire le 3/4 de mes instruction if/else


TEMPERATURE_MIN_REQUIN = 22.0
TEMPERATURE_MAX_REQUIN = 26.0
MASSE_MIN_REQUIN = 60.0
MASSE_MAX_REQUIN = 150.0


TEMPERATURE_MIN_TIGRE = 37.5
TEMPERATURE_MAX_TIGRE = 39.0
MASSE_MIN_TIGRE = 100.0
MASSE_MAX_TIGRE = 260.0

TEMPERATURE_MIN_GNOU = 37.5
TEMPERATURE_MAX_GNOU = 39.0
MASSE_MIN_GNOU = 120.0
MASSE_MAX_GNOU = 270.0

# #IF et ELSE et MATCH Température/Masse ET Âge ET normes T/M

match Espèce:
    case 1:
        Type_espèce = "requin"
        normesT = "22,0-26,0"
        normesM = "60,0-150,0"
        if Celsius >= 22.0:
            Température_C = "Bonne"
            if Celsius <= 26.0:
                Température_C = "Bonne"
            else:
                Température_C = "Mauvaise"
        else:
            Température_C = "Mauvaise"
        if Kilogrammes >= 60.0:
            Poid = "Bon"
            if Kilogrammes <= 150.0:
                Poid = "Bon"
            else:
                Poid = "Mauvais"
        else:
            Poid = "Mauvais"
        if Âge >= 60:
            if Âge < 240:
                Type_Age = "Adulte"
            else:
                Type_Age = "Senior"
        else:
            Type_Age = "Junévile"
        if Indice_de_vitalité < 100:
            if Température_C == "Mauvaise":
                verdict = "URGENT"
            else:
                verdict = "SURVEILLANCE"
        else:
            verdict = "NORMAL"

    case 2:
        Type_espèce = "tigre"
        normesT = "37,5-39,0"
        normesM = "100,0-260,0"
        if Celsius >= 37.5:
            Température_C = "Bonne"
            if Celsius <= 39.0:
                Température_C = "Bonne"
            else:
                Température_C = "Mauvaise"
        else:
            Température_C = "Mauvaise"
        if Kilogrammes >= 100.0:
            Poid = "Bon"
            if Kilogrammes <= 260.0:
                Poid = "Bon"
            else:
                Poid = "Mauvais"
        else:
            Poid = "Mauvais"
        if Âge >= 36:
            if Âge < 144:
                Type_Age = "Adulte"
            else:
                Type_Age = "Senior"
        else:
            Type_Age = "Junévile"
        if Indice_de_vitalité < 100:
            if Température_C == "Mauvaise":
                if Poid == "Mauvais":
                    verdict = "URGENT"
            else:
                verdict = "SURVEILLANCE"
            if Poid == "Mauvais":
                if Température_C == "Mauvaise":
                    verdict = "URGENT"
            else:
                verdict = "SURVEILLANCE"
        else:
            verdict = "NORMAL"  

    case 3:
        Type_espèce = "gnou"
        normesT = "37,5-39,0"
        normesM = "120,0-270,0"
        if Celsius >= 37.5:
            Température_C = "Bonne"
            if Celsius <= 39.0:
                Température_C = "Bonne"
            else:
                Température_C = "Mauvaise"
        else:
            Température_C = "Mauvaise"
        if Kilogrammes >= 120.0:
            Poid = "Bon"
            if Kilogrammes <= 2700.0:
                Poid = "Bon"
            else:
                Poid = "Mauvais"
        else:
            Poid = "Mauvais"
        if Âge >= 36:
            if Âge < 180:
                Type_Age = "Adulte"
            else:
                Type_Age = "Senior"
        else:
            Type_Age = "Junévile"
        if Indice_de_vitalité < 100:
            if Température_C == "Mauvaise":
                if Poid == "Mauvais":
                    verdict = "URGENT"
            else:
                verdict = "SURVEILLANCE"
            if Poid == "Mauvais":
                if Température_C == "Mauvaise":
                    verdict = "URGENT"
            else:
                verdict = "SURVEILLANCE"
        else:
            verdict = "NORMAL"  

#Indice de Vitalité

Indice_de_vitalité = 100

if (Température_C == "Mauvaise"):
    Indice_de_vitalité -= 30
    if (Poid == "Mauvais"):
       Indice_de_vitalité -= 20

elif (Poid == "Mauvais"):
       Indice_de_vitalité -= 20
       if (Température_C == "Mauvaise"):
           Indice_de_vitalité -= 30

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
print(f"{Tiret:-^80}")
print(f"{"Mesure":<30}{"Valeur":>20}{"":>5}{"Norme"}")
print(f"{"Température (°C)":<30}{Celsius2f:>20}{"":>5}{normesT}")
print(f"{"Masse (kg)":<30}{Kilogrammes2f:>20}{"":>5}{normesM}")
print(f"{Tiret:-^80}")
print(f"Conversions")
print(f"{"Masse":<15}:{Masse2f:>10} lbs ={Kilogrammes2f:>10} kg")
print(f"{"Température":<15}:{Température2f:>10} °F  ={Celsius2f:>10} °C")
print(f"{Tiret:-^80}")
print(f"")
print(f"{Tiret:-^80}")
print(f"Indice de vitalité : {Indice_de_vitalité} / 100")
print(f"VERDICT : {verdict}")
print(f"{LigneÉgal:=^80}")