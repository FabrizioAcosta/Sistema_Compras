from abc import ABC, abstractmethod

# 1. Abstracción: Clase abstracta Producto
class Producto(ABC):
    def __init__(self, nombre, precio):
        self._nombre = nombre  # Atributo privado
        self._precio = precio  # Atributo privado

    @abstractmethod
    def mostrar_precio(self):
        pass  # Método abstracto

    # Getter y Setter para el nombre y precio (Encapsulación)
    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        if precio > 0:
            self._precio = precio
        else:
            print("El precio debe ser positivo.")

# 2. Herencia: Subclases de Producto
class Camisa(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)  # Llamada al constructor de la clase base
        self._talla = talla  # Atributo privado

    def mostrar_precio(self):
        return f"El precio de la camisa {self._nombre} es ${self._precio}."

    # Getter y Setter para la talla (Encapsulación)
    @property
    def talla(self):
        return self._talla

    @talla.setter
    def talla(self, talla):
        if talla in ['S', 'M', 'L']:
            self._talla = talla
        else:
            print("Talla inválida.")

class Pantalon(Producto):
    def __init__(self, nombre, precio, largo):
        super().__init__(nombre, precio)
        self._largo = largo

    def mostrar_precio(self):
        return f"El precio del pantalón {self._nombre} es ${self._precio}."

    # Getter y Setter para el largo (Encapsulación)
    @property
    def largo(self):
        return self._largo

    @largo.setter
    def largo(self, largo):
        if largo > 0:
            self._largo = largo
        else:
            print("El largo debe ser un valor positivo.")

class Zapato(Producto):
    def __init__(self, nombre, precio, talla_zapato):
        super().__init__(nombre, precio)
        self._talla_zapato = talla_zapato

    def mostrar_precio(self):
        return f"El precio del zapato {self._nombre} es ${self._precio}."

    # Getter y Setter para la talla del zapato (Encapsulación)
    @property
    def talla_zapato(self):
        return self._talla_zapato

    @talla_zapato.setter
    def talla_zapato(self, talla_zapato):
        if talla_zapato > 0:
            self._talla_zapato = talla_zapato
        else:
            print("La talla de zapato debe ser positiva.")

# 3. Tienda (Gestión de productos y compras)
class Tienda:
    def __init__(self):
        self.productos = []  # Lista de productos en la tienda

    def agregar_producto(self, producto):
        if isinstance(producto, Producto):  # Verificación de polimorfismo
            self.productos.append(producto)

    def mostrar_catalogo(self):
        print("Catálogo de productos disponibles:")
        for producto in self.productos:
            print(producto.mostrar_precio())

    def procesar_compra(self):
        total = 0
        print("\nProcesando compra...")
        for producto in self.productos:
            total += producto.precio
            print(f"Producto: {producto.nombre} - ${producto.precio}")
        print(f"\nTotal a pagar: ${total}")

# 4. Simulación de compra
def main():
    # Crear productos
    camisa1 = Camisa("Camisa de algodón", 25, "M")
    pantalon1 = Pantalon("Pantalón de mezclilla", 40, 32)
    zapato1 = Zapato("Zapato deportivo", 60, 42)

    # Crear una tienda y agregar productos
    tienda = Tienda()
    tienda.agregar_producto(camisa1)
    tienda.agregar_producto(pantalon1)
    tienda.agregar_producto(zapato1)

    # Mostrar el catálogo de productos
    tienda.mostrar_catalogo()

    # Procesar compra
    tienda.procesar_compra()

if __name__ == "__main__":
    main()
