
#########################Listas#########################
nombres = []
lista_productos = []
lista_talles_productos = []
lista_precio_productos = []

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
            print("El numero de producto no esta entre las disponibles, por favor vuelva a intentarlo: ")
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
            print("El numero de producto no esta entre las disponibles, por favor vuelva a intentarlo: ")
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
            print("El numero de producto no esta entre las disponibles, por favor vuelva a intentarlo: ")
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
            print("El numero de producto no esta entre las disponibles, por favor vuelva a intentarlo: ")
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
            print("El numero de producto no esta entre las disponibles, por favor vuelva a intentarlo: ")
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



#Funcion Cantidad disponible
def consultar_cantidad():
    print("Cantidad disponible para este producto: 10 unidades (valor fijo simulado)")



#!!!La funcion se podria validar a traves de un ingreso de numero no texto como las otras variables, seguiria con el estilo de las anteriores
def consultar_talle(categoria):
    if categoria == 1:
        print(talles)
        talle = input("Seleccione un talle: ").upper()
        
        while talle != "XS" and talle != "S" and talle != "M" and talle != "L" and talle != "XL" :
            print("El talle no esta dentro de las opciones dadas")
            talle = input("Seleccione un talle: ").upper()
        
        lista_talles_productos.append(talle)
        
    elif categoria == 2:
        print(talles)
        talle = input("Seleccione un talle: ").upper()
        
        while talle != "XS" and talle != "S" and talle != "M" and talle != "L" and talle != "XL" :
            print("El talle no esta dentro de las opciones dadas")
            talle = input("Seleccione un talle: ").upper()
        
        lista_talles_productos.append(talle)
    
    elif categoria == 3:
        print(talles)
        talle = input("Seleccione un talle: ").upper()
        
        while talle != "XS" and talle != "S" and talle != "M" and talle != "L" and talle != "XL" :
            print("El talle no esta dentro de las opciones dadas")
            talle = input("Seleccione un talle: ").upper()

        lista_talles_productos.append(talle)
        
    elif categoria == 4:
        print(talles)
        talle = input("Seleccione un talle: ").upper()
        
        while talle != "XS" and talle != "S" and talle != "M" and talle != "L" and talle != "XL" :
            print("El talle no esta dentro de las opciones dadas")
            talle = input("Seleccione un talle: ").upper()
    
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
    opcion = input("¿Desea seguir comprando? (s/n): ")
    if opcion == "s" or opcion == "S":
        return True
    return False    #si no se cumple el If retorna en Falso

#Funcion Seleccion metodo de pago
def seleccionar_metodo_pago():
    print("\nSeleccione método de pago:")
    print(mediospago)
    opcion = input("Opción: ")
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

#funcion que suma el total de la lista donde estan guardados los precios unitarios en un total 
def Suma_Precio_Total(precio): 
    iteraciones = len(lista_precio_productos)
    preciototal = 0
    for i in range (iteraciones):
        preciototal = preciototal + lista_precio_productos[0+i]
    print (preciototal)
    print (iteraciones)
    return preciototal
#--------------------------programa

salir = True


while salir :

    nombre = input("Ingrese su nombre: ")
    nombres.append(nombre)

    seguircomprando = True

    while seguircomprando : 

        categoria = mostrar_menu()

        productofin = mostrar_productos_categoria(categoria)

        consultar_cantidad()

        consultar_talle(categoria)

        precio = agregar_al_carrito(productofin, categoria)

        preciototal = Suma_Precio_Total(precio)

        print(f"""
        {nombre} su resumen de compra es
        Sus productos son: {lista_productos}
        Sus respectivos precios son: {lista_precio_productos}
        Sus respectivos talles son: {lista_talles_productos}
        La precio total de su compra es: {preciototal}
        """)

        seguircomprando = desea_seguir_comprando()

    metodo_de_pago = seleccionar_metodo_pago()

    finalizar_compra()

    salir = desea_salir()

