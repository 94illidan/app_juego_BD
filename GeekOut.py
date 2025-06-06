#creamos el juego Geek 
import pandas as pd
import random

seguir_jugando = 'y'

puntuacion = [1,3,6,10,15,21,28,36,45,55]

puntos_a_calcular = 0
puntaje = 0

Dados = {
    'tipos_de_Dados': ['heroe', 'cohete', 'corazon', 'dragon', 'meple', '42'],
    'color': ['amarillo', 'verde', 'rojo','amarillo', 'verde', 'rojo'],
    'cantidad_activos': 7,
    'dados_activos': [],
    'cantidad_inactivos': 3,
    'cantidad_utilizados': 0
}

#Hago un dataframe para que sea mas facil encontrar las caras de los dados en la funcion heroe
Dados_df = pd.DataFrame({'tipos_de_Dados': Dados['tipos_de_Dados'], 'color': Dados['color']})


#funciones de cada cara del dado
def dragon():
    print('el dragon no tiene accion, si lo mantienes al final de la partida pierdes')

def numero():
    print('el 42 no tiene ninguna accion, junta todos los que puedas para puntuar')

# El cohete se elimna el dado utilizado y elimina otro de los activos, se suma 1 a cantidades
def cohete():
    Dados['dados_activos'].remove('cohete')
    Dados['cantidad_activos'] -= 1
    Dados['cantidad_utilizados'] += 1
    if len(Dados['dados_activos']) != 0:
        print('los dados activos son los siguientes ', Dados['dados_activos'])
        elegir_dado= input('¿que dado quieres destruir? ')
        while elegir_dado not in Dados['dados_activos']:
            elegir_dado= input('El dado no fue lanzado elegir otro dado nuevamente: ')
        Dados['dados_activos'].remove(elegir_dado)
        Dados['cantidad_activos'] -= 1
        Dados['cantidad_inactivos'] += 1
    else:
        print('Perdiste, el cohete te exploto')
        

#corazon toma un dado del area de inactivos y lo pone en area de activos, se elimina corazon al 
#si no hay inactivos se utiliza igual
#utilizarlo en dados utilizados
def corazon():
    Dados['dados_activos'].remove('corazon')
    Dados['cantidad_utilizados'] += 1
    if Dados['cantidad_inactivos'] > 0:
        Dados['cantidad_inactivos'] -= 1
        tirada = random.choice(Dados['tipos_de_Dados'])
        Dados['dados_activos'].append(tirada)
    else:
        Dados['cantidad_activos'] -= 1
        print('No hay dados inactivos')

# meple selecciona un dado del area de activos y lo vuelve a lanzar el meple se va al area de dados utilizados
#si no hay dados para volver a lazar se utiliza igual
def meple():
    Dados['dados_activos'].remove('meple')
    Dados['cantidad_activos'] -= 1
    Dados['cantidad_utilizados'] += 1
    if len(Dados['dados_activos']) != 0:
        print('los dados activos son los siguientes ', Dados['dados_activos'])
        elegir_dado= input('¿que dado quieres volver a lanzar? ')
        while elegir_dado not in Dados['dados_activos']:
            elegir_dado= input('El dado no fue lanzado elegir otro dado nuevamente: ')
        Dados['dados_activos'].remove(elegir_dado)
        tirada = random.choice(Dados['tipos_de_Dados'])
        Dados['dados_activos'].append(tirada)
    else:
        print('no hay dados activos')

#el heroe fue el mas dificil para mi, lo que hace es agarrar cualquier dado 
#del area de activos y mostrar la cara opuesta, lo converti en datafrae para que sea mas facil su utilizacion
def heroe():
    Dados['dados_activos'].remove('heroe')
    Dados['cantidad_activos'] -= 1
    Dados['cantidad_utilizados'] += 1
    if len(Dados['dados_activos']) != 0:
        print('los dados activos son los siguientes ', Dados['dados_activos'])
        elegir_dado= input('¿que dado quieres dar vuelta? ')
        while elegir_dado not in Dados['dados_activos']:
            elegir_dado= input('El dado no fue lanzado elegir otro dado nuevamente: ')
        tirada = Dados_df['tipos_de_Dados'][(Dados_df['tipos_de_Dados'] != elegir_dado) & (Dados_df['color'] == Dados_df['color'][Dados_df['tipos_de_Dados'] == elegir_dado].values[0])].values [0]
        Dados['dados_activos'].remove(elegir_dado)
        Dados['dados_activos'].append(tirada)
    else:
        print('no hay dados activos')
        

#Tirada de los dados activos, la idea fue que tome la suma de dados activos y utilizados
#de esta forma puedo utilizar esta funcion varias veces y no hacer 2 al inicio y otra en el durante
def lanzar_dados ():
    for _ in range(Dados['cantidad_activos'] + Dados['cantidad_utilizados']):
        tirada = random.choice(Dados['tipos_de_Dados'])
        Dados['dados_activos'].append(tirada)
    Dados['cantidad_activos'] = Dados['cantidad_activos'] + Dados['cantidad_utilizados']
    Dados['cantidad_utilizados'] = 0
    
#verifica que los dados activos se queden en 0 y lanza los dados nuevamente 
def lista_vacia():
    if len(Dados['dados_activos']) == 0:
        print('Cantidad de dados inactivos: ', Dados['cantidad_inactivos'], ', Cantidad de dados utilizados: ', Dados['cantidad_utilizados'])
        seguir_jugando = input('quiere seguir jugando Y/N ?: ')
        if seguir_jugando == 'y' or seguir_jugando == 'Y':
            lanzar_dados()

#simplemente anota los puntos sacados de una lista, si tenes un total de 2 dados "42" equivale a 3 puntos, etc
def anotar_puntos():
    todos_42 = all(elemento == '42' for elemento in Dados['dados_activos'])
    if todos_42:
        puntaje = puntuacion[len(Dados['dados_activos']) - 1]
        print('Quedaste con todos 42 tu puntaje es de: ', puntaje)
        print('dados inactivos: ', Dados['cantidad_inactivos'], ' Dados utilizados: ', Dados['cantidad_utilizados'])
        seguir_jugando = input('quieres seguir jugando Y/N?: ')
        return seguir_jugando


############### Comienza el juego ###############

print('---Bienvenido al juego Geek, el objetivo es puntuar la mayor cantidad de puntos posibles sin perder')
print('---Para jugar debes elegir un dado de los dados activos, si el dado no fue lanzado no lo puedes usar')
print('---Si el dado es un cohete debes elegir otro dado activo para eliminarlo, si es un corazon debes elegir un dado inactivo para activarlo')
print('---Si el dado es un meple debes elegir un dado activo para volver a lanzarlo, si es un heroe debes elegir un dado activo para mostrar su cara opuesta')
print('---Si el dado es un dragon no tiene accion, si al final de la partida te quedan todos los dados con dragones perdiste')
print('---Si el dado es un 42 no tiene accion, pero si al final de la partida te quedan todos los dados con 42 puntuas')
print('---Si el dado es un cohete y es el ultimo dado que te queda perdiste')
print('---IMPORTANTE, si deseas salir escribe "exit" en el dado que quieres usar para salir del juego')


lanzar_dados()

while seguir_jugando == 'y' or seguir_jugando == 'Y':
    
    #Consulto si los dados jugados son todos dragones, si es asi termine el programa
    todos_dragones = all(elemento == 'dragon' for elemento in Dados['dados_activos'])
    if todos_dragones:
        print('Perdiste tenes todos los dados con dragones', Dados['dados_activos'])
        seguir_jugando = 'n'
    else:
        
        print('Puntaje hasta el momento: ', puntaje)
        print('Cantidad de dados inactivos: ', Dados['cantidad_inactivos'], ', Cantidad de dados utilizados: ', Dados['cantidad_utilizados'])
        print('esta es tu jugada de dados: ', Dados['dados_activos'])
        
        
        #que dado quiere elegir el usuario
        dados_del_usuario = input('que dado quieres usar? ')
        if dados_del_usuario == 'exit':
            seguir_jugando = 'n'
        else:
            
            # consulto si el dado lanzado esta activo sino lo imprimo y consulto nuevamente
            if dados_del_usuario in Dados['dados_activos']:
                #esto lo hice porque la funcion no puede ser un numero
                if dados_del_usuario == '42':
                    dados_del_usuario = 'numero'
                #utilizo el input del usuario para llamar directo a la funcion del propio dado (lo encontre en chatgpt)
                if dados_del_usuario in locals() and callable(locals()[dados_del_usuario]):
                    locals()[dados_del_usuario]()
                else:
                    print('El dado no existe')
            else:
                print('El dado no fue lanzado')        
            
            unico_cohete = all(elemento == 'cohete' for elemento in Dados['dados_activos'])
            if unico_cohete and len(Dados['dados_activos']) == 1:
                print('Perdiste,tu ultimo dado fue el cohete y te exploto')
                seguir_jugando = 'n'
            
            
            lista_vacia()
            
            #si salen todos 42 puntuo y/o sigo tirndo los dados que queden
            #lo quise hacer una funcion pero al hacerlo no me devolvia lo que yo queria 
            todos_42 = all(elemento == '42' for elemento in Dados['dados_activos'])
            if todos_42:
                puntos_a_calcular = puntos_a_calcular + len(Dados['dados_activos'])
                puntaje = (puntuacion[puntos_a_calcular - 1])
                print('Quedaste con todos 42 tu puntaje es de: ', puntaje)
                print('dados inactivos: ', Dados['cantidad_inactivos'], ' Dados utilizados: ', Dados['cantidad_utilizados'])
                Dados['cantidad_activos'] -= len(Dados['dados_activos'])
                Dados['dados_activos'] = []
                lanzar_dados()
                seguir_jugando = input('quieres seguir jugando Y/N?: ')
            
            #si salen dragones y 42 ambos dados no tienen una funcion mas que terminar la partida o puntuar, en este caso 
            #es perdida del  juego
            todos_dragones_42 = all(elemento == 'dragon' or elemento == '42' for elemento in Dados['dados_activos'])
            if todos_dragones_42:
                print('Perdiste no tenes mas opciones y tenes dragones', Dados['dados_activos'])
                seguir_jugando = 'n'




