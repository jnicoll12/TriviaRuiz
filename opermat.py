n1 = int(input("Ingrese un número: "))
n2 = int(input("Iingrese otro número: "))
ope = input("Ingrese la operación: ")
while ope not in ("*", "+","-","/"):
  respuesta_2 = input("Operador invalidado, por favor ingrese *, +, -, /. Ingresa nuevamente tu respuesta: \n")
if ope == "*":
  print ("Resultado: ", n1 * n2)
elif ope == "+":
  print("Resultado: ", n1 + n2)
elif ope == "-":
  print ("Resultado: ", n1 - n2)
elif ope == "/":
  print ("Resultado: ", n1 / n2)
rs = n1