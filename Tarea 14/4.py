def cargar_candidatos():
    candidatos=[]
    for x in range(3):
        nombre=input("Introduce un nombre: ")
        provincias=[]
        otraProvincia="si"
        while otraProvincia=="si":
            provincia=input("Introduce nombre de la provincia: ")
            votos=int(input("Nº de votos de la provincia: "))
            provincias.append((provincia,votos))
            otraProvincia=input("Vas a introducir otra provincia(si/no)")
        candidatos.append((nombre,provincias))
    return candidatos

def visualizar_votos(candidatos):
    for candidato in candidatos:
        totalVotos=0
        for provincia in candidato[1]:
            totalVotos=totalVotos+provincia[1]
        print(candidato[0]," ha obtenido un total de votos de ",totalVotos)
        

candidatos=cargar_candidatos()
visualizar_votos(candidatos)
