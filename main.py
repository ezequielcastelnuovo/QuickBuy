#########################Listas#########################
nombres = []
lista_productos = []
lista_talles_productos = []
lista_precio_productos = []
lista_id = []



#Lista Productos (corregir luego la posicion con un -1?)
productos = ["1. Remeras","2. Pantalones","3. Camperas","4. Calzado","5. Accesorios"]

#Lista Talles (corregir luego la posicion con un -1?)
talles = ["XS","S","M","L","XL"]
talles_calzado = ["36","37","38","39","40","41","42","43","44","45"]

#Lista Medios de Pago (corregir luego la posicion con un -1?)
mediospago = ["1. MercadoPago","2. Credito (3, 6 o 12 cuotas)", "3. Debito", "4. Transferencia", "5. Efectivo (10% descuento)"]

#Listas Categorias (corregir luego la posicion con un -1?)
categoria1 = ["Remera 1","Remera 2","Remera 3","Remera 4","Remera 5"]
categoria2 = ["Pantalones 1","Pantalones 2","Pantalones 3","Pantalones 4","Pantalones 5"]
categoria3 = ["Campera 1","Campera 2","Campera 3","Campera 4","Campera 5"]
categoria4 = ["Zapatillas 1","Botas 2","Zapatos 3","Sandalias 4","Zapatillas 5"]
categoria5 = ["Gorro nombre 1","Bufanda 2","Riñonera 3","Lentes de sol nombre 4","Pulsera nombre 5"]

#########################Funciones#########################

#Funcion MENU
def mostrar_menu():
    print("\nSeleccione una categoría de producto:")
    print(productos)

    categoria = int(input("Seleccione una opción: "))

    while categoria <1 or categoria >5:
        print("El numero de categoria no esta entre las disponibles, por favor vuelva a intentarlo: ")
        categoria = int(input("Seleccione una opción: "))

    return categoria


#Funcion Categorias 
def mostrar_productos_categoria(categoria,):

    print("Productos disponibles:")
    if categoria == 1:
        print(categoria1)
        productofin = int(input("Ingrese el producto que desea elegir: "))

        while  productofin <1 or productofin >5:
            print("El número de producto ingresado no corresponde a los disponibles. Intentelo nuevamente.")
            productofin = int(input("Ingrese el producto que desea elegir: "))

        if productofin == 1: 
            lista_productos.append(categoria1[0])
        elif productofin == 2 :
            lista_productos.append(categoria1[1])
        elif productofin == 3 : 
            lista_productos.append(categoria1[2])
        elif productofin == 4 : 
            lista_productos.append(categoria1[3])
        elif productofin == 5 : 
            lista_productos.append(categoria1[4])
        return productofin

    elif categoria == 2:
        print(categoria2)
        productofin = int(input("Ingrese el producto que desea elegir: "))

        while  productofin <1 or productofin >5:
            print("El número de producto ingresado no corresponde a los disponibles. Intentelo nuevamente.")
            productofin = int(input("Ingrese el producto que desea elegir: "))

        if productofin == 1: 
            lista_productos.append(categoria2[0])
        elif productofin == 2 :
            lista_productos.append(categoria2[1])
        elif productofin == 3 : 
            lista_productos.append(categoria2[2])
        elif productofin == 4 : 
            lista_productos.append(categoria2[3])
        elif productofin == 5 : 
            lista_productos.append(categoria2[4])
        return productofin

    elif categoria == 3:
        print(categoria3)
        productofin = int(input("Ingrese el producto que desea elegir: "))

        while  productofin <1 or productofin >5:
            print("El número de producto ingresado no corresponde a los disponibles. Intentelo nuevamente.")
            productofin = int(input("Ingrese el producto que desea elegir: "))

        if productofin == 1: 
            lista_productos.append(categoria3[0])
        elif productofin == 2 :
            lista_productos.append(categoria3[1])
        elif productofin == 3 : 
            lista_productos.append(categoria3[2])
        elif productofin == 4 : 
            lista_productos.append(categoria3[3])
        elif productofin == 5 : 
            lista_productos.append(categoria3[4])
        return productofin

    elif categoria == 4:
        print(categoria4)
        productofin = int(input("Ingrese el producto que desea elegir: "))

        while  productofin <1 or productofin >5:
            print("El número de producto ingresado no corresponde a los disponibles. Intentelo nuevamente.")
            productofin = int(input("Ingrese el producto que desea elegir: "))

        if productofin == 1: 
            lista_productos.append(categoria4[0])
        elif productofin == 2 :
            lista_productos.append(categoria4[1])
        elif productofin == 3 : 
            lista_productos.append(categoria4[2])
        elif productofin == 4 : 
            lista_productos.append(categoria4[3])
        elif productofin == 5 : 
            lista_productos.append(categoria4[4])

        return productofin

    elif categoria == 5:
        print(categoria5)
        productofin = int(input("Ingrese el producto que desea elegir: "))

        while  productofin <1 or productofin >5:
            print("El número de producto ingresado no corresponde a los disponibles. Intentelo nuevamente.")
            productofin = int(input("Ingrese el producto que desea elegir: "))

        if productofin == 1: 
            lista_productos.append(categoria5[0])
        elif productofin == 2 :
            lista_productos.append(categoria5[1])
        elif productofin == 3 : 
            lista_productos.append(categoria5[2])
        elif productofin == 4 : 
            lista_productos.append(categoria5[3])
        elif productofin == 5 : 
            lista_productos.append(categoria5[4])
        return productofin



#!!!La funcion se podria validar a traves de un ingreso de numero no texto como las otras variables, seguiria con el estilo de las anteriores
def consultar_talle(categoria):
    if categoria == 1:
        print(talles)
        talle = input("Seleccione un talle: ").upper()

        while talle != "XS" and talle != "S" and talle != "M" and talle != "L" and talle != "XL" :
            print("El talle no se encuentra dentro de las opiones disponibles.")
            print("Intentelo nuevamente.")
            talle = input("Seleccione nuevamente el talle: ").upper()

        lista_talles_productos.append(talle)

    elif categoria == 2:
        print(talles)
        talle = input("Seleccione un talle: ").upper()

        while talle != "XS" and talle != "S" and talle != "M" and talle != "L" and talle != "XL" :
            print("El talle no se encuentra dentro de las opiones disponibles.")
            print("Intentelo nuevamente.")
            talle = input("Seleccione un talle: ").upper()

        lista_talles_productos.append(talle)

    elif categoria == 3:
        print(talles)
        talle = input("Seleccione un talle: ").upper()

        while talle != "XS" and talle != "S" and talle != "M" and talle != "L" and talle != "XL" :
            print("El talle no se encuentra dentro de las opiones disponibles.")
            print("Intentelo nuevamente.")
            talle = input("Seleccione un talle: ").upper()

        lista_talles_productos.append(talle)

    elif categoria == 4:
        print(talles_calzado)
        talle = int(input("Seleccione un talle: "))

        while talle <36 or talle > 45 :
            print("El talle no esta dentro de las opciones disponibles.")
            print("Intentelo nuevamente.")
            talle = int(input("Seleccione un talle: "))

        lista_talles_productos.append(talle)

    else:
        print("Talle único")
        talle = "Talle unico"
        lista_talles_productos.append(talle)


    return talle


#Funcion agregar al carrito
def agregar_al_carrito(productofin, categoria):
    if categoria == 1:
        if productofin == 1 : 
            precio = 101
            lista_precio_productos.append(precio)
        if productofin == 2 : 
            precio = 102
            lista_precio_productos.append(precio)
        if productofin == 3 : 
            precio = 103
            lista_precio_productos.append(precio)
        if productofin == 4 : 
            precio = 104
            lista_precio_productos.append(precio)
        if productofin == 5 : 
            precio = 105
            lista_precio_productos.append(precio)

    elif categoria == 2:
        if productofin == 1 : 
            precio = 201
            lista_precio_productos.append(precio)
        if productofin == 2 : 
            precio = 202
            lista_precio_productos.append(precio)
        if productofin == 3 : 
            precio = 203
            lista_precio_productos.append(precio)
        if productofin == 4 : 
            precio = 204
            lista_precio_productos.append(precio)
        if productofin == 5 : 
            precio = 205
            lista_precio_productos.append(precio)

    elif categoria == 3:
        if productofin == 1 : 
            precio = 301
            lista_precio_productos.append(precio)
        if productofin == 2 : 
            precio = 302
            lista_precio_productos.append(precio)
        if productofin == 3 : 
            precio = 303
            lista_precio_productos.append(precio)
        if productofin == 4 : 
            precio = 304
            lista_precio_productos.append(precio)
        if productofin == 5 : 
            precio = 305
            lista_precio_productos.append(precio)

    elif categoria == 4:
        if productofin == 1 : 
            precio = 401
            lista_precio_productos.append(precio)
        if productofin == 2 : 
            precio = 402
            lista_precio_productos.append(precio)
        if productofin == 3 : 
            precio = 403
            lista_precio_productos.append(precio)
        if productofin == 4 : 
            precio = 404
            lista_precio_productos.append(precio)
        if productofin == 5 : 
            precio = 405
            lista_precio_productos.append(precio)

    elif categoria == 5:
        if productofin == 1 : 
            precio = 501
            lista_precio_productos.append(precio)
        if productofin == 2 : 
            precio = 502
            lista_precio_productos.append(precio)
        if productofin == 3 : 
            precio = 503
            lista_precio_productos.append(precio)
        if productofin == 4 : 
            precio = 504
            lista_precio_productos.append(precio)
        if productofin == 5 : 
            precio = 505
            lista_precio_productos.append(precio)

    return precio


#Funcion desea seguir comprando?
def desea_seguir_comprando():
    opcion = input("\n¿Desea seguir comprando? (s/n): ")
    if opcion == "s" or opcion == "S":
        return True 
    return False




#Funcion Seleccion metodo de pago
def seleccionar_metodo_pago(preciototal):
    print("\nMétodos de pago disponibles: ")
    print(mediospago)

    opcion = int(input("Ingrese el número de la opción elegida: "))
    
    while opcion < 1 or opcion > 5 : 
        print("El número ingresado no es válido. Intente nuevamente.")
        opcion = input("Ingrese el número de la opción elegida: ")
        
    if opcion == 5 : 
        preciototal = preciototal *0.90 
        print(f"El valor total de su compra es: ${preciototal:.2f}")
    else:
        print(f"El valor total de su compra es: ${preciototal:.2f}")              
    
    #se puede agregar meter datos del medio de pago para rolear
    return opcion


#Funcion finalizacion de compra
def finalizar_compra():
    print("\n✅ Gracias por realizar la compra 🛍️")


#Funcion Desea Salir del programa? Al final
def desea_salir():
    opcion = input("¿Desea salir? (s/n): ").lower()
    if opcion == "s":
        return False
    return True

#Funcion que suma el total de la lista donde estan guardados los precios unitarios en un total 
def Suma_Precio_Total(precio): 
    iteraciones = len(lista_precio_productos)
    preciototal = 0
    for i in range (iteraciones):
        preciototal = preciototal + lista_precio_productos[0+i]
    #print (preciototal)
    #print (iteraciones)
    return preciototal

def BuscarProducto(preciototal): 

    buscar = input("\n¿Desea eliminar algún producto de la lista? (s/n): ")

    while buscar != "s" and buscar != "S" and buscar != "n" and buscar != "N" : 
        print("La respuesta ingresada no es correcta vuelva a intentarlo: ")
        buscar = input("¿Desea eliminar algún producto de la lista? (s/n): ")

    if buscar == "S" or buscar == "s" :

        while True:
            producto = int(input("Ingrese el número del producto que desea eliminar: "))
            producto_encontrado = False

            for i in range(len(lista_id)):
                if lista_id[i] == producto:
                    producto_encontrado = True
                    print("-----------------------------------------------------")
                    print(f"""
Producto ELIMINADO ❌ : {lista_productos[i]}
Precio: ${lista_precio_productos[i]}
Talle: {lista_talles_productos[i]}
                    """)

                    lista_id.pop(i)
                    lista_productos.pop(i)
                    lista_talles_productos.pop(i)
                    lista_precio_productos.pop(i)
                    print("El producto fue eliminado con éxito. ✅")
                    return  True

            if producto_encontrado == False:
                print("El producto no existe. Intente con otro número.")

    return False

def Lista_ID():
    # Se vacia la lista, esto es para que si se elimina un objeto se reasignen los numeros 
    while len(lista_id) > 0:
        lista_id.pop()

    # Generamos nuevos Ids para la lista
    for i in range(len(lista_productos)):
        lista_id.append(i + 1)


def MatrizProductos (precio): 
    
    for i in range (len(lista_productos)):
        print("\nNumero de producto:",lista_id[i],"|",lista_productos[i],"|",lista_talles_productos[i],"|","$",lista_precio_productos[i])
    print("\n-----------------------------------------------------")    
    print("\nEl precio total es: $",Suma_Precio_Total(precio))


#-------------------------------------programa-----------------------------------------#

salir = True


while salir :
    
    lista_id = []
    lista_precio_productos = []
    lista_productos = []
    lista_talles_productos = []
    nombres = []
    
    nombre = input("Ingrese su nombre: ")
    nombres.append(nombre)

    seguircomprando = True

    while seguircomprando : 

        categoria = mostrar_menu()

        productofin = mostrar_productos_categoria(categoria)

        consultar_talle(categoria)

        precio = agregar_al_carrito(productofin, categoria)

        preciototal = Suma_Precio_Total(precio)

        seguircomprando = desea_seguir_comprando()


    Lista_ID()

#control de listas iguales 
#   print(len(lista_id), len(lista_productos), len(lista_talles_productos), len(lista_precio_productos))


    MatrizProductos(preciototal)


    eliminado = BuscarProducto(preciototal)
    
    if eliminado:
        preciototal = Suma_Precio_Total(precio) #se recalcula en caso de que se haya eliminado algun producto de la lista
        Lista_ID()
        MatrizProductos(precio)

    metodo_de_pago = seleccionar_metodo_pago(preciototal)

    finalizar_compra()

    salir = desea_salir()
