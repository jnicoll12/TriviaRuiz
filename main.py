#Importar libreria avanzadas, libreria random, calculo aleatorio de numero segun rango
import random

#Declaracion de colores
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
print ("Bienvenido a mi trivia sobre el Perú")
print ("Pondremos a prueba tus conocimientos")
print ("Empecemos, ¿Cuál es tu nombre?")
# Almacenamos la respuesta del usuario en la variable "nombre para guardar su nomrbe"
nombre = input("\nTu respuesta:")
edad = int (input("¿Qué edad tienes?: "))

# Es importante dar instrucciones sobre cómo jugar:
print ("Perfecto, ahora", nombre," responderas las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Entrer' para enviar tu respuesta, cada pregunta tiene un valor de 5 puntos, por cada pregunta equivocada se te restará 1:\n")

#Creamos variable para controlar el puntaje, llamda "puntaje" asignandole un valor 0
puntaje = random.randint(0, 10)

#Indicamos con cuantos puntos inicia el juego
print("Comenzaras con ",puntaje," puntos \n")
# OJO, el \n al final de la línea 6 es para dar un "salto de línea"

# Pregunta 1
print ("1) ¿Cuántos colores tiene la bandera del Perú?")
print ("a) 2 - Rojo y Blanco")
print ("b) 3 - Rojo, Amarillo y Blanco")
print ("c) 6 - Blanco, Marron, Celeste, Negro, Verde y Azul")
print ("d) 1 - Rojo")

# Almacenamos la respuesta del usuario en la variable "respuesta_1"
respuesta_1 = input("\nTu respuesta: ")
if  respuesta_1 == "a" or respuesta_1 == "A":
  puntaje +=5
  print("Muy bien!", nombre, ", continuemos...\n")
else:
  puntaje -=1
  print("Incorrecto")

  
  # Pregunta 2
print("Actualmente tienes ", puntaje, " puntos")
print ("2) ¿En qué año oficial se proclama la independencia en el Perú?")
print ("a) 1932")
print ("b) 1541")
print ("c) 1617")
print ("d) 1821")

# Almacenamos la respuesta del usuario en la variable "respuesta_2"
respuesta_2 = input("\nTu respuesta: ")

while respuesta_2 not in ("a", "b","c","d", "z"):
  respuesta_2 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: \n")
  
if respuesta_2 =="a":
  print("Totalmente incorrecto!", nombre, "En 1932, inicia la Revolución de Trujillo. \n")
  puntaje / 2
elif respuesta_2 == "b":
  print ("Incorrecto!", nombre, "En 1541, es asesinado el conquistador del Tahuantisuyo, Francisco Pizarro, a manos de los almagristas. \n")
  puntaje + 5
elif respuesta_2 =="c":
  print ("Incorrecto!", nombre, "En 1617, fallece Santa Rosa de Lima. \n")
  puntaje -=5
elif respuesta_2 =="z":
  puntaje +=1000
  print("********************BONUS********************")
  print("********************BONUS********************")
  print("********************BONUS********************")
  print("********************BONUS********************")
  print ("Respuesta secreta!", nombre, " recibirás un bonus de 1000 puntos. \n")
else:
  #Al ser un respuesta correcto se multiplica los puntos actuales por su edad
  puntaje *=edad
  print("Muy bien",nombre,"! \n")
  
# Pregunta 3
print("Actualmente tienes ", puntaje, " puntos")
print ("3) ¿Cuántas millas de mar tiene el Perú?")
print ("a) 1500 millas")
print ("b) 1000 millas")
print ("c) 200 millas")
print ("d) 150 millas")

# Almacenamos la respuesta del usuario en la variable "respuesta_3"
respuesta_3 = input("\nTu respuesta: ")
if  respuesta_3 == "c" or respuesta_3 == "C":
  puntaje +=5
  print("Muy bien!", nombre, ", continuemos... \n")
else:
  puntaje -=1
  print("Incorrecto")

# Pregunta 4
print("Actualmente tienes ", puntaje, " puntos")
print ("3) ¿Cuántas regiones geofráficas tiene el Perú?")
print ("a) Costa, Sirra y Selva")
print ("b) Costa, Sierra y Selva")
print ("c) No tiene regiones geográficas")
print ("d) Costo, Sirra y Selva")

# Almacenamos la respuesta del usuario en la variable "respuesta_4"
respuesta_4 = input("\nTu respuesta: ")
if  respuesta_4 == "b" or respuesta_4 == "B":
  puntaje +=5
  print("Correcto!", nombre, "\n")
else:
  puntaje -=1
  print("Incorrecto")

print("Gracias", nombre, " por jugar mi trivia, alcanzaste ",puntaje," puntos.")