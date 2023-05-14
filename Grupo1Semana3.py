from random import randint#importamos funcion del modulo random

jugar_denuevo = "si"
while jugar_denuevo == "si":
  
  nombre = input("Para comenzar a jugar ingresa tu nombre/nickname ʕ•́ᴥ•̀ʔっ \n")
  print(f"Bien {nombre} ahora debes adivinar un numero del 1 al 100, tienes 8 intentos. Mucha Suerte! (̶◉͛‿◉̶) \n")

  numero_adivinar    = randint(1,100) #funcion randit, guardamos en una variable un numero aleatorio del 1 al 100
  intentos           = 1 #contador de intentos, se inicializa en 1 para enviar un mensaje coherente si el usuario adivina a la primera. 
  intentos_restantes = 8 #inicializamos contador de intentos

  while intentos < 9: #bucle con 8 intentos para adivinar el numero aleatorio
   numero = input("Ingresa un numero entero: \n")
 
   if not numero.isdigit() or not numero.isdecimal(): #Detectando caracteres que no sean enteros
     print(f"{nombre} te dije que solo eran NUMEROS ENTEROS!(ง︡'-'︠)ง")
     continue
   else:
     numero = int(numero) #conversion de la variable 
     if numero < numero_adivinar: #Detecta si el numero a adivinar es MAYOR para posteriormente lanzar el mensaje 
      intentos += 1 #aumentamos el valor de "intentos" posterior a detectar que sea un numero entero el ingresado 
      intentos_restantes -=1 #calculamos los intentos que le quedan al usuario para posteriormente informarlo en un mensaje
      if intentos_restantes > 1: 
        print("El numero a adivinar es mayor al que elegiste")
        print(f"No te preocupes! te quedan {intentos_restantes} intentos")
      elif intentos_restantes == 1: 
        print("El numero a adivinar es mayor al que elegiste")
        print(f"Ahora si preocupate!  (っ-̶●̃益●̶̃)っ  Es Tu ultimo intento {nombre}!") #EXTRA: si solo queda 1 intento metemos presion al usuario
      else: 
        print(f"lo siento {nombre}, pero PERDISTE ¯\_(ツ)_/¯ el numero era {numero_adivinar} ")
     elif numero > numero_adivinar: #Detecta si el numero a adivinar es MENOR para posteriormente lanzar el mensaje
      intentos += 1
      intentos_restantes -=1
      if intentos_restantes > 1:
        print("El numero a adivinar es menor al que elegiste")
        print(f"No te preocupes! te quedan {intentos_restantes} intentos")
      elif intentos_restantes == 1: 
        print("El numero a adivinar es menor al que elegiste")
        print(f"Ahora si precupate!  (っ-̶●̃益●̶̃)っ  Es Tu ultimo intento {nombre}!")  #EXTRA: si solo queda 1 intento metemos presion al usuario
      else : 
        print(f"lo siento {nombre},pero PERDISTE ¯\_(ツ)_/¯ el numero era {numero_adivinar} ")   #Finalizado el bucle se informa el numero que debía adivinar el usuario

     if numero == numero_adivinar:
      print(f"Felicidades {nombre} adivinaste!! el numero era {numero} (>‿◠)")
      print(f"Lo lograste con {intentos} intentos")
      break #cortamos el bucle si el numero ingresado es igual al generado con la funcion randit
  
  jugar_denuevo = input("Quieres jugar de nuevo: si / no ᕙ(`▿´)ᕗ \n").lower() #EXTRA:ofrecemos al usuario repetir el juego
  
  while jugar_denuevo != "si" and jugar_denuevo != "no":
    jugar_denuevo = input("Seamos serios un minuto ಠ_ಠ Ingresa solamente si o no \n").lower()
    
  if jugar_denuevo == "no":
   print(f"nos vemos la proxima {nombre} ≧◠ᴥ◠≦")
   break 
  

 
   

 
    
         
  
   
   
   
   
