Clientes = {}
def Reg_Clientes (n,cont=1):
    if cont > n:
        return  0
    print(f"\nCliente #{cont}")
    codigo = int(input("Ingrese el codigo del cliente: "))
    nombre = input("Ingrese el nombre del cliente: ")

    while True:
        CantDestinos = int(input("Cuantos destinos desea registrar: "))
        if 1 <= CantDestinos <=3:
            break
        else:
            print("El maximo registro de destinos es 3!")

    destinos = []
    for i in range(CantDestinos):
        destino = input(f"Destino {i+1}: ")
        destinos.append(destino)

    Clientes[codigo] = {
        "Nombre": nombre,
        "destino" : destinos
    }

    Reg_Clientes(n, cont + 1)

'''*******************************************************************************'''

def ContDestinos (listClientes, claves=None, i=0):
    if claves is None:
        claves = list(listClientes.Keys())

    if i >= len(claves):
        return  0
    codigo = claves[i]
    NumDestinos = len(listClientes[codigo]['Destinos'])

    return  NumDestinos + ContDestinos(listClientes,claves,i+1)
'''*******************************************************************************'''

def ClienteConMasDestinos(claves,i=0,MaxCliente= None, MaxCantCliente =0):
    if i >=len(claves):
        return MaxCliente,MaxCantCliente
    codigo = claves[i]
    nombre = Clientes[codigo]['nombre']
    cantidad = len(Clientes[codigo]['Destinos'])

    if cantidad > MaxCantCliente:
        return  ClienteConMasDestinos(claves,i+1,nombre,cantidad)

'''*******************************************************************************'''
def MostrarResultados():
    print(f"\nBIENVENIDO AL LISTADO DE CLIENTES Y DESTINOS VISITADOS ")
    for codigo, datos in Clientes.items():
        print(f"Codigo: {codigo}")
        print(f"Nombre: {datos['nombre']}")
        print(f"Destinos: ")