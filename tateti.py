#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv

def registrar():
    # Pido los nombres de los participantes
    part1 = input(str('Particiapante 1 ingrese su nombre: '))
    part2 = input(str('Particiapante 2 ingrese su nombre: '))

    # Hago que el primer participante elija su item
    while True:    
        seleccion = input(str('{} Elegi Cruz(X) o Circulo(O): ').format(part1)).upper()
        # Valido segun la opcion elegida es el participante que empieza
        if(seleccion == 'x' or seleccion == 'X'):
            participantes = {seleccion: part1, 'O': part2}
            break
        elif(seleccion == 'o' or seleccion == 'O'):
            participantes = {'X': part2, seleccion: part1}
            break
        else:
            print('la opcion "{}" no es correcta'.format(seleccion))

    return participantes


def verificar(tablero):
    # Capturo cada una de las filas
    fila1 = tablero[0]
    fila2 = tablero[1]
    fila3 = tablero[2] 
    while True:
        # Pido que elija el casillo
        casillero = input(str('Elegi un casillero del C1 al C9: ')).upper()
        # Verifico que el dato ingresado sea correcto, coincida con el tablero y ademas este vacio
        if casillero in fila1:
            if fila1[casillero] == casillero:
                break
            else:
                print('El casillero {} ya esta ocuapdo por {}'.format(casillero, fila1[casillero]))    
        elif casillero in fila2:
            if fila2[casillero] == casillero:
                break
            else:
                print('El casillero {} ya esta ocuapdo por {}'.format(casillero, fila2[casillero]))    
        elif casillero in fila3:
            if fila3[casillero] == casillero:
                break
            else:
                print('El casillero {} ya esta ocuapdo por {}'.format(casillero, fila3[casillero]))    
        else:
            print('El casillero {} no existe'.format(casillero))
        
    return casillero

def modificar(tablero,turno):
    # Capturo el casillero verifcado
    casillero = verificar(tablero)
    if casillero:
        while True: 
            # Pido que ingrese el item que eligio y valido si es correcto
            item = input(str('Ingrese su item: ')).upper()
            if item == 'X' or item == 'O':
                for f in tablero:
                    try:
                        if f[casillero]:
                            # Relleno el casillero con el item ingresado
                            f[casillero] = item
                            # Guardo el dato
                            with open('tateti.csv','w') as archivo:
                                writer = csv.writer(archivo, delimiter='|',quotechar='|')
                                for c  in tablero:
                                    writer.writerow(c.values())
                    except KeyError:
                        pass
                break    
            else:
                print('El item ingresado no es valido.')    

def arbitro(tablero, participantes, turno, n_turno):
    # Esta funcion se encarga de definir cuando alguien gano si hay empate o si sigue el juego
   
    fila1 = tablero[0]
    fila2 = tablero[1]
    fila3 = tablero[2] 
    ganador = False
    if (fila1['C1'] == 'X' and fila2['C4'] == 'X' and fila3['C7'] == 'X') or (fila1['C2'] == 'X' and fila2['C5'] == 'X' and fila3['C8'] == 'X') or (fila1['C3'] == 'X' and fila2['C6'] == 'X' and fila3['C9'] == 'X') :
        ganador = participantes['X']
    elif (fila1['C1'] == 'X' and fila1['C2'] == 'X' and fila1['C3'] == 'X') or (fila2['C4'] == 'X' and fila2['C5'] == 'X' and fila2['C6'] == 'X') or (fila3['C7'] == 'X' and fila3['C8'] == 'X' and fila3['C9'] == 'X'):
        ganador = participantes['X']
    elif (fila1['C1'] == 'X' and fila2['C5'] == 'X' and fila3['C9'] == 'X') or (fila1['C3'] == 'X' and fila2['C5'] == 'X' and fila3['C7'] == 'X'):
        ganador = participantes['X']        
    elif (fila1['C1'] == 'O' and fila2['C4'] == 'O' and fila3['C7'] == 'O') or (fila1['C2'] == 'O' and fila2['C5'] == 'O' and fila3['C8'] == 'O') or (fila1['C3'] == 'O' and fila2['C6'] == 'O' and fila3['C9'] == 'O') :
        ganador = participantes['O']                
    elif (fila1['C1'] == 'O' and fila1['C2'] == 'O' and fila1['C3'] == 'O') or (fila2['C4'] == 'O' and fila2['C5'] == 'O' and fila2['C6'] == 'O') or (fila3['C7'] == 'O' and fila3['C8'] == 'O' and fila3['C9'] == 'O'):
        ganador = participantes['O']                
    elif (fila1['C1'] == 'O' and fila2['C5'] == 'O' and fila3['C9'] == 'O') or (fila1['C3'] == 'O' and fila2['C5'] == 'O' and fila3['C7'] == '0'):
        ganador = participantes['O']      
    
    if n_turno == 9:
        print('Fin del juego. Empate')
        tateti()
        exit
        
    if ganador:
        with open('tateti.csv', newline='') as archivo:
            reader = csv.reader(archivo, delimiter='|', quotechar='|')
            for row in reader:
                print('|'.join(row)) 
        with open('tateti.csv','w') as archivo:
            writer = csv.writer(archivo, delimiter='|',quotechar='|')
            writer.writerow(" ")
        print('Fin del juego. El ganador es {}'.format(ganador))
        tateti()
        exit

    turno = turnero(turno)
    return turno


def turnero(turno):
     # Define que particpante va
    if turno == 'X':
        turno = 'O'
    else:
        turno = 'X'
    
    return turno


def tateti():
    # Doy la bienvenida y pregunto si quiere jugar
    bienvenida = input(str('Bienvenido a Ta Te Ti: desea jugar? '))
    if bienvenida == 's' or bienvenida == 'si' or bienvenida == 'SI' or bienvenida == 'Si':
        pass
    elif  bienvenida == 'n' or bienvenida == 'no' or bienvenida == 'NO' or bienvenida == 'No':
        exit
    else:
        print('Por favor escriba una opcion valida Si o No')
    
    # Traigo los particiapantes con sus respectivos items
    participantes = registrar()
    
    # Defino el tablero nuevo y lo guardo en un csv
    tablero = [{'C1':'C1','C2':'C2','C3':'C3'},{'C4':'C4','C5':'C5','C6':'C6'},{'C7':'C7','C8':'C8','C9':'C9'}]   
    with open('tateti.csv','w') as archivo:
        writer = csv.writer(archivo, delimiter='|',quotechar='|')
        for c  in tablero:
            writer.writerow(c.values())

    # Defino el turno de quien va primero
    turno = 'X'
    # Defino el numero de turno
    n_turno = 0
    # Comienza el juego
    while True:
        # Aumento el turno en 1 cada vez que
        n_turno += 1
        
        #Imprimo el tablero
        with open('tateti.csv', newline='') as archivo:
            reader = csv.reader(archivo, delimiter='|', quotechar='|')
            for row in reader:
                print('|'.join(row))     
        
        # Muestro quien va y con que item
        for key , part in participantes.items():
            if key == turno:
                print('Es el turno de {} con el item {}'.format(part.upper(), key.upper()))
                break

        modificar(tablero, turno)
        resultado = arbitro(tablero, participantes,turno, n_turno)
        
        # Cambio de valor turno para siempre sea intercalado
        if resultado == 'X' or resultado == 'O':
            turno = resultado

tateti()

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))