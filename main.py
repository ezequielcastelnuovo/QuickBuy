############################################################################# LISTAS #############################################################################


nombres = []  #nombres de clientes
lista_productos = [] #productos seleccionados 
lista_talles_productos = [] #talles de los productos que selecciona el usuario, almacena el talle (por producto)
lista_precio_productos = [] #precios de los productos (se almacena de manera general al precio GENERAL)
lista_id = [] #Ids de los productos

# Lista de Categorias
productos = ["1. Remeras","2. Pantalones","3. Camperas","4. Calzado","5. Accesorios"] 

# Lista de Talles
talles = ["XS","S","M","L","XL"]    #talles de ropa
talles_calzado = ["36","37","38","39","40","41","42","43","44","45"]   #talles de calzado

#Listas de productos dentro de la CATEGORIA SELECCIONADA (Remeras, Pantalones, Camperas, Calzados, Accesorios)
categoria1 = ["1. Camiseta Tape Type Medium Fit en Beige (USD 795)","2. Camiseta Soccer Balenciaga | Automobili Lamborghini Oversized (USD 1100)","3. Camiseta I Love Paris & Balenciaga Oversize en Blanco (USD 450)","4. Camiseta Cropped Diy Imprint en Verde Salvia (USD 695)","5. Camiseta Loop Sports Icon Medium Fit (USD 395)"]
categoria2 = ["1. Pantalón Baggy Azul Claro (USD 1300)","2. Pantalón De Chándal Balenciaga Nail Polish Cropped (USD 1100)","3. Pantalón Cargo Ancho Azul Oscuro (USD 1800)","4. Pantalón Cargo Flared Negro (USD 1590)","5. Pantalón Baggy Cut-up Azul (USD 1600)"]
categoria3 = ["1. Bomber - Basketball Series (USD 7500)","2. Chaqueta Round Loop Sports Icon Verde Ciprés (USD 3000)","3. Bomber Round Azul Marino Oscuro (USD 3200)","4. Chaqueta Varsity Lion Club Negro (USD 2600)","5. Chaqueta Tracksuit 3b Sports Icon Negro (USD 5000)"]
categoria4 = ["1. Zapatillas 3xl Gris (USD 975)","2. Zapatillas 6xl Negro/Gris (USD 995)","3. Zapatillas Runner Graffiti (USD 1100)","4. Bota Venom Negro (USD 1650)","5. Bota Giant Negro (USD 1990)"]
categoria5 = ["1. Gorra Loop Sports Icon Azul/blanco (USD 450)","2. Gafas De Sol Blade Rectangle Rojo (USD 465)","3. Casco Negro/blanco (USD 895)","4. Vaso Tumbler Plateado (USD 250)","5.Cinturón Skater Unity Negro (USD 325)"]

#Lista de medios de Pago DISPONIBLES
mediospago = [
    "1. MercadoPago",
    "2. Débito",
    "3. Crédito (Hasta 12 cuotas)",
    "4. Transferencia",
    "5. Efectivo (10% de Descuento)"
]


############################################################################# FUNCIONES #############################################################################


# FUNCION MENU
def mostrar_menu():
    print("\nSeleccione una categoría de producto:")
    print(productos)

    categoria = int(input("Seleccione una opción: "))

    while categoria <1 or categoria >5:
        print("El numero de categoria no esta entre las disponibles, por favor vuelva a intentarlo: ")
        categoria = int(input("Seleccione una opción: "))

    return categoria




# FUNCION Categoria 
def mostrar_productos_categoria(categoria,):

    print("\nProductos disponibles:")
    print("-------------------------------------")
    if categoria == 1:    # Remeras
        for producto in categoria1:
            print(producto)
        print("-------------------------------------")
        productofin = int(input("\nIngrese el producto que desea elegir: "))

        while  productofin <1 or productofin >5:
            print("El número de producto ingresado no corresponde a los disponibles. Intentelo nuevamente.")
            productofin = int(input("Ingrese el producto que desea elegir: "))

        if productofin == 1:
            lista_productos.append(categoria1[0])    # Funcion APPEND (Agregar a la lista)
        elif productofin == 2 :
            lista_productos.append(categoria1[1])    # Funcion APPEND (Agregar a la lista)
        elif productofin == 3 :
            lista_productos.append(categoria1[2])    # Funcion APPEND (Agregar a la lista)
        elif productofin == 4 :
            lista_productos.append(categoria1[3])    # Funcion APPEND (Agregar a la lista)
        elif productofin == 5 :
            lista_productos.append(categoria1[4])    # Funcion APPEND (Agregar a la lista)
        return productofin

    elif categoria == 2:    # Pantalones
        for producto in categoria2:
            print(producto)
        print("-------------------------------------")
        productofin = int(input("\nIngrese el producto que desea elegir: "))

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

    elif categoria == 3:     # Camperas
        for producto in categoria3:
            print(producto)
        print("-------------------------------------")
        productofin = int(input("\nIngrese el producto que desea elegir: "))

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

    elif categoria == 4:     # Calzado
        for producto in categoria4:
            print(producto)
        print("-------------------------------------")
        productofin = int(input("\nIngrese el producto que desea elegir: "))

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

    elif categoria == 5:     # Accesorios
        for producto in categoria5:
            print(producto)
        print("-------------------------------------")
        productofin = int(input("\nIngrese el producto que desea elegir: "))

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




# Funcion CONSULTAR TALLE
def consultar_talle(categoria):
    if categoria == 1:     # Remeras
        print(talles)
        talle = input("Seleccione un talle: ").upper()    # UPPER es una funcion integrada en python que convierte todas las letras de un string en MAYUSCULA

        while talle != "XS" and talle != "S" and talle != "M" and talle != "L" and talle != "XL" :
            print("El talle no se encuentra dentro de las opiones disponibles.")
            print("Intentelo nuevamente.")
            talle = input("Seleccione nuevamente el talle: ").upper()

        lista_talles_productos.append(talle)

    elif categoria == 2:     # Pantalones
        print(talles)
        talle = input("Seleccione un talle: ").upper()

        while talle != "XS" and talle != "S" and talle != "M" and talle != "L" and talle != "XL" :
            print("El talle no se encuentra dentro de las opiones disponibles.")
            print("Intentelo nuevamente.")
            talle = input("Seleccione un talle: ").upper()

        lista_talles_productos.append(talle)

    elif categoria == 3:      # Camperas
        print(talles)
        talle = input("Seleccione un talle: ").upper()

        while talle != "XS" and talle != "S" and talle != "M" and talle != "L" and talle != "XL" :
            print("El talle no se encuentra dentro de las opiones disponibles.")
            print("Intentelo nuevamente.")
            talle = input("Seleccione un talle: ").upper()

        lista_talles_productos.append(talle)

    elif categoria == 4:      # Calzado
        print(talles_calzado)
        talle = int(input("Seleccione un talle: "))

        while talle <36 or talle > 45 :
            print("El talle no esta dentro de las opciones disponibles.")
            print("Intentelo nuevamente.")
            talle = int(input("Seleccione un talle: "))

        lista_talles_productos.append(talle)

    else:                     # Accesorios (Talle Unico)
        print("Talle único")
        talle = "Talle unico"
        lista_talles_productos.append(talle)

    return talle




# FUNCION Agregar al carrito
def agregar_al_carrito(productofin, categoria):
    if categoria == 1:
        if productofin == 1 :
            precio = 795
            lista_precio_productos.append(precio)
        if productofin == 2 :
            precio = 1100
            lista_precio_productos.append(precio)
        if productofin == 3 :
            precio = 450
            lista_precio_productos.append(precio)
        if productofin == 4 :
            precio = 695
            lista_precio_productos.append(precio)
        if productofin == 5 :
            precio = 395
            lista_precio_productos.append(precio)

    elif categoria == 2:
        if productofin == 1 :
            precio = 1300
            lista_precio_productos.append(precio)
        if productofin == 2 :
            precio = 1100
            lista_precio_productos.append(precio)
        if productofin == 3 :
            precio = 1800
            lista_precio_productos.append(precio)
        if productofin == 4 :
            precio = 1590
            lista_precio_productos.append(precio)
        if productofin == 5 :
            precio = 1600
            lista_precio_productos.append(precio)

    elif categoria == 3:
        if productofin == 1 :
            precio = 7500
            lista_precio_productos.append(precio)
        if productofin == 2 :
            precio = 3000
            lista_precio_productos.append(precio)
        if productofin == 3 :
            precio = 3200
            lista_precio_productos.append(precio)
        if productofin == 4 :
            precio = 2600
            lista_precio_productos.append(precio)
        if productofin == 5 :
            precio = 5000
            lista_precio_productos.append(precio)

    elif categoria == 4:
        if productofin == 1 :
            precio = 975
            lista_precio_productos.append(precio)
        if productofin == 2 :
            precio = 995
            lista_precio_productos.append(precio)
        if productofin == 3 :
            precio = 1100
            lista_precio_productos.append(precio)
        if productofin == 4 :
            precio = 1650
            lista_precio_productos.append(precio)
        if productofin == 5 :
            precio = 1990
            lista_precio_productos.append(precio)

    elif categoria == 5:
        if productofin == 1 :
            precio = 450
            lista_precio_productos.append(precio)
        if productofin == 2 :
            precio = 465
            lista_precio_productos.append(precio)
        if productofin == 3 :
            precio = 895
            lista_precio_productos.append(precio)
        if productofin == 4 :
            precio = 250
            lista_precio_productos.append(precio)
        if productofin == 5 :
            precio = 325
            lista_precio_productos.append(precio)

    return precio




# FUNCION Selecciona metodo de pago
def seleccionar_metodo_pago(preciototal):
    print("\nMétodos de pago disponibles:")
    for medio in mediospago:    #Imprimir en Vertical 
        print(medio)

    opcion = 0
    while opcion < 1 or opcion > 5:
        print("\nIngrese el número de la opción elegida (1 a 5): ")
        texto = input("Seleccione una opción: ")
        if texto == "1":
            opcion = 1
        elif texto == "2":
            opcion = 2
        elif texto == "3":
            opcion = 3
        elif texto == "4":
            opcion = 4
        elif texto == "5":
            opcion = 5
        else:
            print("Opción inválida. Intente nuevamente.")

    if opcion == 5:      # Efectivo
        preciototal *= 0.90
        print("\nAplica 10% de descuento por pago en efectivo.")
        print(f"Total a pagar: ${preciototal:.2f}")     # :.2f PARA QUE CORTE EN 2 Decimales

    elif opcion == 3:    # Credito
        print("\n¿Desea pagar en cuotas?")
        print("1. 1 cuota (sin interés)")
        print("2. 3 cuotas (sin interés)")
        print("3. 6 cuotas (10% de recargo)")
        print("4. 12 cuotas (20% de recargo)")

        cuotas = 0
        while cuotas < 1 or cuotas > 4:
            texto_cuotas = input("Seleccione una opción de cuotas (1 a 4): ")
            if texto_cuotas == "1":
                cuotas = 1
            elif texto_cuotas == "2":
                cuotas = 2
            elif texto_cuotas == "3":
                cuotas = 3
            elif texto_cuotas == "4":
                cuotas = 4
            else:
                print("Opción de cuotas inválida. Intente nuevamente.")

        if cuotas == 1:
            total = preciototal
            cantidad_cuotas = 1
        elif cuotas == 2:
            total = preciototal
            cantidad_cuotas = 3
        elif cuotas == 3:
            total = preciototal * 1.10    # Recargo del %10 
            cantidad_cuotas = 6
        elif cuotas == 4:
            total = preciototal * 1.20    # Recargo del %20
            cantidad_cuotas = 12

        print(f"\nTotal a pagar: ${total:.2f}")
        print(f"En {cantidad_cuotas} cuotas de ${total / cantidad_cuotas:.2f} cada una.")

    else:
        print(f"\nTotal a pagar: ${preciototal:.2f}")




def Lista_ID():      # Se vacia la lista, esto es para que si se elimina un objeto se reasignen los numeros
    while len(lista_id) > 0:    
        lista_id.pop()     # Borra TODA la lista

    for i in range(len(lista_productos)):      # GENERAMOS Nuevos IDs para la Lista
        lista_id.append(i + 1)        # Se asignan un ID para c/producto en orden




# FUNCION     ELIMINAR PRODUCTOS             BUSQUEDA SECUENCIAL (LINEAL)
def BuscarProducto(buscar):
    if len(lista_id) != 0:     #Para que no te deje usar esta funcion si SOLO tenes 1 producto en el carrito
        buscar_input = True
        se_elimino_producto = False

        while buscar_input == True:
            if len(lista_id) != 0:
                buscar_choice = input("¿Desea eliminar algún producto del carrito?  (s/n): ").lower()

                while buscar_choice != "s" and buscar_choice != "n":
                    print("Error de digitación, vuelva a intentarlo. ")
                    buscar_choice = input("¿Desea eliminar algún producto del carrito? (s/n): ").lower()

                if buscar_choice == "s":
                    buscar_input = True

                    if not lista_id:
                        print("No hay productos en el carrito para eliminar.")
                        buscar_input = False
                        break

                    producto = int(input("Ingrese el número del producto que desea eliminar: "))
                    producto_encontrado = False
                    eliminado = False

                    for i, item_id in enumerate(lista_id):
                        if item_id == producto:
                            producto_encontrado = True
                            print("\n-----------------------------------------------------")
                            print(f"""
        Producto ELIMINADO  : {lista_productos[i]}
        Precio: ${lista_precio_productos[i]}
        Talle: {lista_talles_productos[i]}
                            """)

                            lista_id.pop(i)        # .pop se limina de la lista
                            lista_productos.pop(i)    # .pop se limina de la lista
                            lista_talles_productos.pop(i)   # .pop se limina de la lista
                            lista_precio_productos.pop(i)   # .pop se limina de la lista
                            print("El producto fue eliminado con éxito. ")
                            eliminado = True
                            se_elimino_producto = True
                            break

                    if not producto_encontrado:
                        print("El producto no existe, Intente con otro número.")

                else:
                    buscar_input = False
            else:
                print("El carrito está vacío. No hay productos para eliminar.")
                buscar_input = False
        return se_elimino_producto
    else:
        print("El carrito está vacío. No hay productos para eliminar.")
        return False




# FUNCION que Suma el total de la lista donde estan guardados los preicos unitarios en un total
def Suma_Precio_Total(precio_ignorado):
    iteraciones = len(lista_precio_productos)
    preciototal = 0
    for i in range (iteraciones):
        preciototal = preciototal + lista_precio_productos[0+i]
    return preciototal





def MatrizProductos (total_a_mostrar):

    for i in range (len(lista_productos)):
        print("\nNumero de producto:",lista_id[i],"|",lista_productos[i],"|",lista_talles_productos[i],"|","$",lista_precio_productos[i])
    print("\n-----------------------------------------------------")
    print("\nEl precio total es: $", total_a_mostrar)




# FUNCION Desea Salir del programa?
def desea_salir():
    opcion = input("¿Desea salir? (s/n): ").lower()
    if opcion == "s":
        return False
    return True



# FUNCION  Finalizar compra
def finalizar_compra():
    print("\n Gracias por realizar la compra ")



# FUNCION Desea seguir comprando?
def desea_seguir_comprando():
    opcion = input("\n¿Desea seguir comprando? (s/n): ")
    if opcion == "s" or opcion == "S":
        return True
    return False




#-------------------------------------------------------------------------Programa PRINCIPAL ----------------------------------------------------------------#    

salir = True

while salir :     # es lo mismo que decir while salir == True:

    lista_id = []     # Se vacian las listas para cada iteracion
    lista_precio_productos = []    # Se vacian las listas para cada iteracion
    lista_productos = []    # Se vacian las listas para cada iteracion
    lista_talles_productos = []    # Se vacian las listas para cada iteracion

    nombre_usuario = input("Ingrese su nombre: ")

    seguircomprando = True    # Se inicializa el ciclo, hace lo mismo que el "salir == True:""

    while seguircomprando :

        categoria = mostrar_menu()

        productofin = mostrar_productos_categoria(categoria)

        consultar_talle(categoria)

        agregar_al_carrito(productofin, categoria)

        seguircomprando = desea_seguir_comprando()   # Se define si, si o no el ciclo

    Lista_ID()    # Esta fuera del ciclo ya que ya estan definiados los productos 

    preciototal_final = Suma_Precio_Total(0)

    MatrizProductos(preciototal_final)      # Se muestra la lista de productos seleccionados

    se_elimino_algun_producto = BuscarProducto(preciototal_final)

    if se_elimino_algun_producto: # es igual que decir if se_elimino_algun_producto == True:
        preciototal_final = Suma_Precio_Total(0) # Se recalcula en caso de que se haya algun producto de la lista
        Lista_ID()  # Vuelve a crear la lista de IDs para que se reasignen los ordenes de la lista
        MatrizProductos(preciototal_final)  #Tira la matriz de productos actualizada

    seleccionar_metodo_pago(preciototal_final)

    finalizar_compra()   # Print "gracias por finalizar la compra"

    salir = desea_salir()