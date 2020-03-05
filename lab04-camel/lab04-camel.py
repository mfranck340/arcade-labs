import arcade
import random

def main():
    """none-->none
    OBJ:Mostrar las instrucciones del videojuego"""
    print("Bienvenido al Camello")
    print("Acabas de robar un camello para atravesar el gran desierto de Mobi.")
    print("¡Los nativos te han descubierto y quieren recuperar su camello!")
    print("Sobrevive a tu caminata por el desierto y despista a los nativos.\n")

    entra = input("**Presiona enter para continuar**")

    done = False

    recorrido_jugador = 0
    sed = 0
    cansancio_camello = 0
    cantimplora = 3
    recorrido_nativos = -20

    while not done:
        print("\nA.Bebe de tu cantinplora")
        print("B.Avanzar a velocidad moderada")
        print("C.Avanzar a toda velocidad")
        print("D.Detente por la noche")
        print("E.Verifica el estado")
        print("Q.Salir")

        opcion = input("\n¿Qué has decidido?: ")
        opcion = opcion.upper()

        #Opciones durante el viaje
        if opcion == "Q":
            print("\nHas salido del juego :(")
            done = True

        elif opcion == "A":
            if cantimplora != 0:
                print("Te has recuperado")
                sed = 0
                cantimplora -= 1
            else:
                print("Lo siento no te quedan cantimploras :O")

        elif opcion == "B":
            print("Avanzas con tranquilidad")
            recorrido_jugador += random.randint(5,12)
            print("Has avanzado", recorrido_jugador, "millas")
            sed += 1
            cansancio_camello += 1
            recorrido_nativos += random.randint(7, 14)
            if random.randrange(7) == 0:
                print("Has encontrado un oasis. Puedes descansar")
                sed = 0
                cansancio_camello = 0
                cantimplora = 3

        elif opcion == "C":
            print("Avanzas a gran velocidad")
            recorrido_jugador += random.randint(10,20)
            print("Has avanzado", recorrido_jugador, "millas")
            sed += 1
            cansancio_camello += random.randint(1,3)
            recorrido_nativos += random.randint(7, 14)
            if random.randrange(7) == 0:
                print("Has encontrado un oasis. Puedes descansar")
                sed = 0
                cansancio_camello = 0
                cantimplora = 3

        elif opcion == "D":
            cansancio_camello = 0
            print("Descansando...")
            print("El camello está contento :D")
            recorrido_nativos += random.randint(7,14)

        elif opcion == "E":
            print("Millas recorridas: ", recorrido_jugador)
            print("Cantinploras: ", cantimplora)
            print("Los nativos van ", (recorrido_jugador - recorrido_nativos), " millas detrás de ti")

        else:
            print("La opción introducida no es válida ")

        #Indicaciones del nivel de sed
        if sed > 4:
            print("Tienes sed, necesitas agua")
        if sed == 6:
            print("Has muerto de sed :(")
            done = True

        #Indicaciones del cansancio del camello
        if cansancio_camello > 5 and not estado_camello:
            print("Tu camello está cansado. Tal vez deberías descansar")
        if cansancio_camello == 8 and not estado_camello:
            print("Tu camello a muerto. Pronto te atraparan :(")
            print("Fin del juego")
            done = True

        #Indicaciones del recorrido de los nativos
        if recorrido_nativos >= recorrido_jugador:
            print("""Los nativos te han atrapado
            Has muerto""")
            done = True
        if recorrido_nativos > (recorrido_jugador - 15):
            print("""Los nativos te pisan los talones
            ¡Cuidado!""")

        #Indicaciones de victoria
        if recorrido_jugador >= 200:
            print("""Has salido del desierto con vida y despistado a los nativos
            ¡Felicidades, has ganado!""")
            done = True

main()

