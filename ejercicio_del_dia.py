# ejercicio dia 2
#ejercicio 1
edad = int(input("Ingrese su edad: "))
if edad <12:
    print("Niño")
elif edad <18:
    print("Adolesente")
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