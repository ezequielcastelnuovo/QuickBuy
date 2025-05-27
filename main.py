                    #            FUNCIONES          #


#Funcion Ingresar nombre
nombres = []

def ingresar_nombre():
    nombre = input("Ingrese su nombre: ")
    nombres.append(nombre)
    return nombre


#########################Listas


#Lista Productos (corregir luego la posicion con un -1?)
productos = ["1. Remeras","2. Pantalones","3. Camperas","4. Calzado","5. Accesorios"]

#Lista Talles (corregir luego la posicion con un -1?)
talles = ["XS","S","M","L","XL"]

#Lista Medios de Pago (corregir luego la posicion con un -1?)
mediospago = ["1. MercadoPago","2. Credito (3, 6 o 12 cuotas)", "3. Debito", "4. Transferencia", "5. Efectivo (10% descuento)"]

#Listas Categorias (corregir luego la posicion con un -1?)
categoria1 = ["Remera 1","Remera 2","Remera 3","Remera 4","Remera 5"]
categoria2 = ["Pantalones 1","Pantalones 2","Pantalones 3","Pantalones 4","Pantalones 5"]
categoria3 = ["Campera 1","Campera 2","Campera 3","Campera 4","Campera 5"]
categoria4 = ["Zapatillas 1","Botas 2","Zapatos 3","Sandalias 4","Zapatillas 5"]
categoria5 = ["Gorro nombre 1","Bufanda 2","Riñonera 3","Lentes de sol nombre 4","Pulsera nombre 5"]

###################################


#example preguntar al profe
'''
productos = [
    ["Remera1", "Remera2", "Remera3", "Remera4", "Remera5"],
    ["Pantalón1", "Pantalón2", "Pantalón3", "Pantalón4", "Pantalón5"],
    ["Campera1", "Campera2", "Campera3", "Campera4", "Campera5"],
    ["Zapatillas1", "Botas2", "Zapatos3", "Zapatillas4", "Zapatillas5"],
    ["Gorro1", "Bufanda2", "Riñonera3", "Gorro4", "Gorro5"]
]

def mostrar_productos_categoria(categoria):
    categoria_idx = int(categoria) - 1
    print("\nProductos disponibles:")
    for i, producto in enumerate(productos[categoria_idx]):
        print(f"{i+1}. {producto}")

'''



#Funcion MENU
def mostrar_menu():
    print("\nSeleccione una categoría de producto:")
    print(productos)
    opcion = input("Seleccione una opción: ")
    return opcion

#Funcion Categorias 
def mostrar_productos_categoria(categoria):
    print("\nProductos disponibles:")
    if categoria == "1":
        print(categoria1)

    elif categoria == "2":
        print(categoria2)

    elif categoria == "3":
        print(categoria3)

    elif categoria == "4":
        print(categoria4)

    elif categoria == "5":
        print(categoria5)

    else:
        print("Categoría inválida.")

#Funcion Cantidad disponible
def consultar_cantidad(categoria):
    print("Cantidad disponible para este producto: 10 unidades (valor fijo simulado)")

#Funcion consultar talle
def consultar_talle(categoria):
    if categoria == "1":
        print(talles)
    elif categoria == "2":
        print(talles)
    elif categoria == "3":
        print(talles)
    elif categoria == "4":
        print(talles)
    else:
        print("Talle único")
    talle = input("Seleccione un talle: ")
    return talle

#Funcion agregar al carrito
def agregar_al_carrito(total_actual, categoria):
    if categoria == "1":
        precio = 700    #Precios expresados en USD
    elif categoria == "2":
        precio = 2000   #Precios expresados en USD
    elif categoria == "3":
        precio = 4000   #Precios expresados en USD
    elif categoria == "4":
        precio = 5000   #Precios expresados en USD
    elif categoria == "5":
        precio = 500    #Precios expresados en USD
    else:
        precio = 0
    print(f"Producto agregado. Precio: ${precio}")
    return 

#Funcion desea seguir comprando?
def desea_seguir_comprando():
    opcion = input("¿Desea seguir comprando? (s/n): ")
    if opcion == "s" or opcion == "S":
        return True
    return False    #si no se cumple el If retorna en Falso

#Funcion Seleccion metodo de pago
def seleccionar_metodo_pago():
    print("\nSeleccione método de pago:")
    print(mediospago)

    opcion = input("Opción: ")
    return opcion

#Funcion finalizacion de compra
def finalizar_compra():
    print("\n✅ Gracias por realizar la compra 🛍️")


#Funcion Desea Salir del programa? Al final
def desea_salir():
    opcion = input("¿Desea salir? (s/n): ").lower()
    if opcion == "s":
        return True
    return False




# Programa PRINCIPAL
####
####
####
####
####
####
###
###
###
###
##
##
##
##
#
#

print ("adsasd")