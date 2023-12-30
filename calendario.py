#calendario 


#importamos funciones de modulos y un modulo 
from time import sleep
from calendar import month,prcal
from datetime import date
from os import system
import sys


#funcion la cual al detectar el nucleo del sistema borrara la consola con su comando nativo correspondiente
def limpiar_consola():
    
    '''
    esta funcion lo que hace es limpiar la consola con base al nucleo del sistema 
    '''
    systema_consulta=sys.platform.lower()
    
    #windows
    if systema_consulta == "win32":
        system("cls")

    #GNU/Linux y macOS
    elif systema_consulta in ["linux","darwin"]:
         system("clear")

    #si el nucleo no es ninguno de los anteriores imprime un mensaje y se cierra el programa
    else:
        print("arquitectura de sistema no soportado")  
        sys.exit()   

    return



#en esta funcion le damos opciones al usuario a elegir y despues se le retornara una salida
def consulta_calendario():
  
  '''
  creamos una funcion que le dara opciones de salida en pantalla al usuario con base al numero elegido por el y que esta relacionado a las preguntas dadas
  '''

  #usamos el manejo de excepciones con try: y except:
  try:
    

    #imprimimos en consola las opciones a elegir por el usuario
    print("""
Bienvenido a esta maravillosa app de calendario, que le gustaria hacer a continuacion:

1) ver la fecha de hoy?
          
2) ver la fecha de algun año, mes y dia?
                    
3) ver el calendario de este mes?
          
4) ver el calendario de este año?
          
5) ver el calendario de algun año en especifico?
          
NOTA: ingresa el valor numerico que esta al principio de las preguntas
          
""")
    
    #guardamos el dato ingresado por el usuario en la variable consulta y limpiamos consola 
    consulta=input(">>> ")
    limpiar_consola()

   
    #usamos la condicional if para elegir que opcion de retorno devolver con base al dato brindado por el usuario
    if consulta == "1":
        print(date.today())


    #el elif es como otra opcion adicional si el if dio False
    elif consulta == "2":
        
        def consulta_fecha():

          '''
          creamos una funcion para tomar los datos entrantes por el usuario, que seria el año, fecha y dia
          y tambien se trabaja la excepcion ValueError y un rango de numeros con base al año 
          '''

          #aqui usamos el Do while simulado con while True: para repetir toda esta linea de codigo dentro de la funcion consulta_fecha si el usuario dase un valor
          #invalido 
          while True:

            try: 
               
               #declaramos tres variables con valores entrantes por el usuario y al pasarle la funcion int() lo pasa a valor entero
               año,mes,dia=int(input("ingrese el año en base a este rango 1900 - 3000 >> ")),int(input("ingrese el mes en base a este rango 1 - 12 >> ")),int(input("ingrese el dia en base a este rango 1 - 31 >> "))
               if año >= 1900 and año <= 3000 and mes >= 1 and mes <= 12 and dia >= 1 and dia <= 31:
                  limpiar_consola()
                  print(f"""
año -> {date(año,mes,dia).year}
mes -> {date(año,mes,dia).month}
dia -> {date(año,mes,dia).day}
""")
                  #cierra el ciclo
                  break
               

               #si la condicional if y elif da False, se ejecuta el else
               else:
               
                 limpiar_consola()
                 print("valores incorrectos,vuelve a intentarlo ")
                 sleep(2)

            #si en try que lo que hace es correr el codigo dentro de el se da la excepcion ValueError se ejecutara este except
            except ValueError:
           
                limpiar_consola()
                print("valores incorrectos,vuelve a intentarlo ")
                sleep(2)

        consulta_fecha()        

            
    elif consulta == "3":
         print(month(2023,12))



    elif consulta == "4":
         prcal(2023)



    elif consulta == "5":
      
      
          def consulta_año():

            '''
            creamos una funcion para tomar los datos entrantes por el usuario, que seria el año en tipo de dato entero, tambien se maneja la excepcion ValueError
            y un rango numeros con base al año 
            '''

            while True:

              try:   
              
                 año_especifico=int(input("ingrese al año especifico en base a este rango 1900 - 3000 >> "))
                 if año_especifico >= 1900 and año_especifico <= 3000:
                    prcal(año_especifico)
                    break
            
                 else:
                
                    limpiar_consola()
                    print("valor incorrecto,vuelve a intentarlo")
                    sleep(2)
                 
                
              except ValueError:  
          
              
                 limpiar_consola()
                 print("valor incorrecto,vuelve a intentarlo ")
                 sleep(2)

          consulta_año()    
            
                 
    else:
        limpiar_consola()
        consulta2=input("valor invalido, desea intentarlo de nuevo o deseas salir, (\"SI\" continuar, \"NO\" salir): ").lower()
        if consulta2 == "si" :
             limpiar_consola()
             consulta_calendario()


        else:
            sys.exit()
  

  except KeyboardInterrupt:    
         print("bye")
         sys.exit()



'''
consultamos al usuario si quiere realizar otra consulta, si el usuario elige que si
llamamos otra ves a las funciones limpiar_consola, consulta_calendario, reinicio_programa,
y si es por el contrario se finaliza el programa
'''
def reinicio_programa():
    
    '''
      creamos una funcion para saber si el usuario quiere realizar otra accion en el programa 
    '''

    consulta_4=input("\n" + "le gustaria hacer otra consulta (SI o NO): ").lower()
    if consulta_4 == "si":
         limpiar_consola()
         consulta_calendario()
         reinicio_programa()


    else:
        limpiar_consola()
        print("bye")
       



#llamamos a las funciones
limpiar_consola()
consulta_calendario()
reinicio_programa()



#metadatos
__name__="calendario"
__version__="0.2"