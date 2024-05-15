# -*- coding: utf-8 -*-
"""
Created on Mon May 13 15:05:00 2024

@author: isisa
"""

import random

# Definir listas de personajes, locaciones y armas
personajes = ['juan el cartero', 'julia la ama de llaves', 'robert el empresario', 'sofia la esposa de robert', 'josé criminólogo e hijo de robert y sofia']
locaciones = ['la sala de la casa', 'la alberca', 'el cuarto', 'la cocina', 'la terraza']
armas = ['cuchillo', 'pistola', 'jarrón roto', 'navaja', 'espada']

# Definir las historias
historias = [
    {'culpable': 'juan el cartero', 'locacion': 'la alberca', 'arma': 'navaja'},
    {'culpable': 'julia la ama de llaves', 'locacion': 'la terraza', 'arma': 'cuchillo'},
    {'culpable': 'robert el empresario', 'locacion': 'el cuarto', 'arma': 'pistola'},
    {'culpable': 'sofia la esposa de robert', 'locacion': 'la sala de la casa', 'arma': 'jarrón roto'},
    {'culpable': 'josé criminólogo e hijo de robert y sofia', 'locacion': 'la cocina', 'arma': 'espada'}
]

# Función para inicializar el juego
def iniciar_juego():
    # Seleccionar una historia aleatoria
    historia = random.choice(historias)
    culpable = historia['culpable']
    locacion = historia['locacion']
    arma = historia['arma']
    print("Se ha cometido un crimen. Debes descubrir quién lo hizo, dónde y con qué arma.")
    print("Los personajes son: ", ', '.join(personajes))
    print("Las locaciones son: ", ', '.join(locaciones))
    print("Las armas son: ", ', '.join(armas))
    print("\nComencemos la investigación...\n")
    return culpable, locacion, arma

# Función para que el jugador haga una suposición
def hacer_suposicion():
    print("\nHaz una suposición sobre el culpable, la locación y el arma utilizada.")
    suposicion_culpable = input("Culpable: ").lower()
    suposicion_locacion = input("Locación: ").lower()
    suposicion_arma = input("Arma: ").lower()
    return suposicion_culpable, suposicion_locacion, suposicion_arma

# Función para verificar la suposición del jugador
def verificar_suposicion(culpable, locacion, arma, suposicion_culpable, suposicion_locacion, suposicion_arma):
    if suposicion_culpable == culpable and suposicion_locacion == locacion and suposicion_arma == arma:
        return True
    else:
        print("¡Incorrecto! La suposición es incorrecta. Sigue investigando.")
        return False

# Función principal del juego
def jugar_clue():
    culpable, locacion, arma = iniciar_juego()
    intentos = 0
    while True:
        suposicion_culpable, suposicion_locacion, suposicion_arma = hacer_suposicion()
        intentos += 1
        if verificar_suposicion(culpable, locacion, arma, suposicion_culpable, suposicion_locacion, suposicion_arma):
            print("\n¡Felicidades! Has descubierto al culpable, la locación y el arma utilizada.")
            print("El culpable fue", culpable, "en", locacion, "con", arma)
            print("Número de intentos:", intentos)
            break

# Iniciar el juego
jugar_clue()
