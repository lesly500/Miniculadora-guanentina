input

import math
print("-----------------------------")
print("1)suma")
print("2)resta")
print("3)multiplicaion")
print("4)divicion")
print("5)potencia")
print("6)logaritm")
print("-----------------------------")

opc =int(input("dijite la peracion a realizar: "))

x = int(input("digite el primer numero de la operacion "))
y =int(input(" digite el segundo numero de la oercion "))

if opc == 1:
    print(f"el resultado de la sumaes {(x)+(y)}")

elif opc == 2:
    print(f"el resultado de la resta es {(x)- (y)}")

elif opc == 3:
    print(f"el resultado de la multiplicacion es {(x)*(y)}")

elif opc == 4:
    print(f" el resultado de la divicion es {(x)/(y)}")

elif opc == 5:
    print(f"el resultado  de la potencia es {(x)**(y)}")

elif opc == 6:
    print("el valor es: ",math .log(x,y))

else:
    print("opcion no valida")