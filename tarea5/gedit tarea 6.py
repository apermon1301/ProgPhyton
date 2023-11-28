positivos=0
negativos=0
mult15=0
sumaPares=0
for x in range(10):
    n=int(input("Ingrese un número:"))
    if n>0:
        positivos=positivos+1
    else:
        negativos=negativos+1
    if n%15==0:
        mult15=mult15+1
    if n%2==0:
        sumaPares=sumaPares+n
print("Positivos:",positivos)
print("Negativos:",negativos)
print("Múltiplos de 15:",mult15)
print("Suma de los pares:",sumaPares)


        
        
        
          
