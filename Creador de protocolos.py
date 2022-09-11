print("Bienvenido")
print(" ")

Milista=()

num = int(input("Introduce el tamaño del protocolo: "))
elems = len(Milista)
num1 = num+1

for elems in range (1,num1):
    e=int(input("Introduce el número del paso: "))
    elem = str(input("Introduce el paso a añadir: "))
    ele=str(e)+".-"+elem
    mitup=list(Milista)
    mitup.append((ele))
    Milista=tuple(mitup)
    print(" ")
print(Milista)
print(" ")
    
def menu():
    print("""Indique la operación a realizar:
    
    1) Añadir un paso siguiente
    2) Insertar elemento anidado
    3) Borrar elementos
    4) Salir
    """)
menu();
opc="si"
op=" "
while opc=="si":
    op = int(input("Elige una opción: "))
        
    if op == 1:
        print(" ")
        e=int(input("Introduce el número del paso: "))
        elem = str(input("Introduce el paso a añadir: "))
        ele=str(e)+".-"+elem
        mitup=list(Milista)
        mitup.append((ele))
        Milista=tuple(mitup)
        print(" ")
        print(Milista)
        print(" ")
            
    elif op == 2:
        e=int(input("Introduce el número del paso: "))
        nom = int(input("Introduce el número del subpaso: "))
        elem = str(input("Introduce el paso a añadir: "))
        el2=str(e)+".-"+str(nom)+"."+elem
        e1=e+1
        mitup=list(Milista)
        mitup.insert (e,(el2))
        Milista=tuple(mitup)
        print(" ")
        print(Milista)
        print(" ")
    elif op == 3:
        elem = str(input("Introduce el paso a eliminar: "))
        mitup=list(Milista)
        mitup.remove((elem))
        Milista=tuple(mitup)
        print(" ")
        print(Milista)
        print(" ")
    elif op == 4:
        print("Hasta pronto!")
        break    
    else:
        print(" ")
        print("Opción inválida")
        print(" ")
        
    print("Desea ingresar otra opción? si/no")
    opc=input("")
