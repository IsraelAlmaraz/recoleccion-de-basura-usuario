import datossimulados

U1 = datossimulados.Camion("camion 1", 1)
U2 = datossimulados.Camion("camion 2", 2)
U3 = datossimulados.Camion("camion 3", 3)
U4 = datossimulados.Camion("camion 4", 4)

lista = [U1, U2, U3, U4]

lista = datossimulados.circular(lista)
print(lista)
