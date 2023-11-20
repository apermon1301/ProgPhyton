num1=int(input("Introduce un número:"))
num2=int(input("Introduce otro número:"))
num3=int(input("Introduce otro número:"))
if num1>num2 and num1>num3:
    print("El mayor es ",num1)
else:
    if num2>num3:
        print("El mayor es ",num2)
    else:
        print("El mayor es ",num3)

if num1<num2 and num1<num3:
    print("El menor es ",num1)
else:
    if num2<num3:
        print("El menor es ",num2)
    else:
        print("El menor es ",num3)
