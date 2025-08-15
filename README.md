# 🛒 Clothing Store Simulator (Console)

This project is a Python console application that simulates a shopping experience in a luxury clothing and accessories store.
The user can select a category, choose products, indicate sizes, add products to the cart, and select a payment method.
The system calculates the total price with possible discounts or surcharges depending on the chosen payment method.

# 📌 Main Features

* Interactive menu with product category selection.
* Display of products by category with their prices.
* Size selection (clothing, footwear, or one-size).
* Calculation of the total cart price based on selected products.
* Discounts for cash payments.
* Surcharges for credit card installments (3, 6, or 12 payments).
* User input validation to avoid entry errors.

# 🧰 Technologies Used

* **Python 3**: Main programming language of the project.
* **Functions**: Logical separation of tasks such as displaying menus, checking sizes, adding items to the cart, and selecting the payment method.
* **Data structures**: Lists for storing customer names, products, sizes, and prices.
* **Flow control**: Conditionals and `while` loops to manage user options.

# 🔧 Methods and Structure

### Lists

Multiple lists are used to store user and product information:

* `lista_productos`, `lista_talles_productos`, `lista_precio_productos`: information about the shopping cart.
* `productos`, `categoria1` to `categoria5`: predefined lists of available products by category.
* `talles`, `talles_calzado`: available sizes depending on the product type.
* `mediospago`: available payment options.

### Key Functions

* **`mostrar_menu()`**: Displays the available categories and prompts the user for a selection.
* **`mostrar_productos_categoria(categoria)`**: Shows products based on the selected category.
* **`consultar_talle(categoria)`**: Allows the selection of the appropriate size depending on the product type.
* **`agregar_al_carrito(productofin, categoria)`**: Adds the price of the selected product to the total.
* **`seleccionar_metodo_pago(preciototal)`**: Applies discounts or surcharges depending on the payment method.

