🛒 Simulador de Tienda de Ropa (Consola)
Este proyecto es una aplicación de consola en Python que simula una experiencia de compra en una tienda de ropa y accesorios de lujo. El usuario puede seleccionar una categoría, elegir productos, indicar talles, agregar productos al carrito y seleccionar un medio de pago. El sistema calcula el precio total con posibles descuentos o recargos según el método de pago elegido.

📌 Funcionalidades principales
Menú interactivo con selección de categorías de productos.

Visualización de productos por categoría con sus precios.

Selección de talle (ropa, calzado o talle único).

Cálculo del total del carrito según productos elegidos.

Descuentos por pago en efectivo.

Recargos por financiación con tarjeta de crédito (3, 6 o 12 cuotas).

Validación de entradas del usuario para evitar errores de ingreso.

🧰 Tecnologías utilizadas
Python 3: Lenguaje principal del proyecto.

Funciones: Separación lógica de tareas como mostrar menús, consultar talle, agregar al carrito y seleccionar método de pago.

Estructuras de datos: Uso de listas para almacenar nombres de clientes, productos, talles y precios.

Control de flujo: Condicionales y bucles while para manejar las opciones del usuario.

🔧 Métodos y Estructura
Listas
Se utilizan múltiples listas para almacenar información del usuario y de los productos:

lista_productos, lista_talles_productos, lista_precio_productos: información sobre el carrito.

productos, categoria1 a categoria5: listas predefinidas de productos disponibles por categoría.

talles, talles_calzado: talles disponibles según tipo de producto.

mediospago: opciones de pago disponibles.

Funciones destacadas
mostrar_menu(): muestra las categorías disponibles y solicita la elección del usuario.

mostrar_productos_categoria(categoria): muestra productos según la categoría seleccionada.

consultar_talle(categoria): permite seleccionar el talle correspondiente según el tipo de producto.

agregar_al_carrito(productofin, categoria): añade el precio del producto seleccionado al total.

seleccionar_metodo_pago(preciototal): aplica descuentos o recargos según el método de pago.

🚀 Cómo ejecutar el programa
Asegurate de tener Python 3.x instalado.

Descargá el archivo .py del proyecto o cloná el repositorio:

bash
Copy
Edit
git clone https://github.com/tu-usuario/tu-repositorio.git
Ejecutalo desde la terminal o tu IDE favorito:

bash
Copy
Edit
python tienda_virtual.py
📌 Posibles mejoras a futuro
Implementar una interfaz gráfica con Tkinter o PyQt.

Añadir sistema de login de usuarios.

Guardar historial de compras.

Integración con base de datos para persistencia.
