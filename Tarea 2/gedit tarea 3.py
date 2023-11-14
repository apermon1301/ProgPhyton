num1=int(input("Introduce un número positivo:"))
if num1>0:
    if num1<100:
        if num1>=10:
                    print("Tiene dos dígitos")
        else:
            print("Solo tiene un dígito")
    else:
        print("El número tiene dos diígitos")
else:print("El número es negativo")
