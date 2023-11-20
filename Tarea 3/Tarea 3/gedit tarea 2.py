nota=int(input("Introduce una nota:"))
if nota<5:
    print("Has suspendido")
else:
    nota>5 and nota<7
    print("Has aprobado y tienes un bien")
    if nota>7 and nota<9:
        print("Has aprobado y tienes un notable")
    else:
        nota>9
        print("Has aprobado y tienes un sobresaliente")
