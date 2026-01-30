# ejercicio dia 2
#ejercicio 1
edad = int(input("Ingrese su edad: "))
if edad <12:
    print("Niño")
elif edad <18:
    print("Adolecente")
else:
    print("Adulto")

##########################

#ejersicio 2
Usuario = input("Usuario: ")
Clave = input("Clave: ")

if Usuario == "admin" and Clave == "1234":
    print("Acceso permitido")
else:
    print("Accesi denegado")

##################################
nombre_usuario = input("Ingrese tu nombre: ")
try:
    edad_usuario = int(input("ingrese su edad: "))
except ValueError:
    print("Error: la edad debe ser un numero.")
    exit()
if edad_usuario >= 18:
    print(f"{nombre_usuario}, sos mayor de edad.")
else:
    print(f"{nombre_usuario}, sos menor de edad.")