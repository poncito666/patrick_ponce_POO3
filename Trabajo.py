from abc import ABC, abstractmethod
class Usuario(ABC):
    def __init__(self, nombre, correo, contraseña):
        self.__nombre = nombre
        self.__correo = correo
        self.__contraseña = contraseña


    def get_nombre(self):
        return self.__nombre


    @abstractmethod
    def mostrar_rol(self):
        pass




class Vendedor(Usuario):
    def __init__(self, nombre, correo ,contraseña):
        super().__init__(nombre, correo, contraseña)
        self.videojuegos = []


    def registrar_videojuego(self, videojuego):
        self.videojuegos.append(videojuego)
        print("Videojuego '" + videojuego.nombre + "' registrado correctamente.")


    def mostrar_rol(self):
        print("Rol: Vendedor")




class Cliente(Usuario):
    def __init__(self, nombre, correo, contraseña):
        super().__init__(nombre, correo, contraseña)
        self.compras = []


    def comprar_videojuego(self, videojuego):
        self.compras.append(videojuego)
        print("Has comprado '" + videojuego.nombre + "'.")


    def mostrar_rol(self):
        print("Rol: Cliente")




class Videojuego:
    def __init__(self, nombre, precio, genero):
        self.nombre = nombre
        self.precio = precio
        self.genero = genero


    def mostrar_info(self):
        print("\n Información del juego")
        print("Nombre:", self.nombre)
        print("Precio:", self.precio)
        print("genero:", self.genero)




class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.usuarios = []


    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(usuario.get_nombre() + " se registró correctamente.")




tienda = Tienda("juegos real no feik store")


tipo = input("¿quieres registrarte como vendedor o cliente?: ").lower()


if tipo == "vendedor":
    nombre = input("Nombre: ")
    correo = input("Correo: ")
    contraseña = input("Contraseña: ")


    vendedor = Vendedor(nombre, correo, contraseña)
    tienda.registrar_usuario(vendedor)


    vendedor.mostrar_rol()


    nombre_juego = input("Nombre del videojuego: ")
    precio = float(input("Precio: "))
    genero = input("Género: ")


    juego = Videojuego(nombre_juego, precio, genero)
    vendedor.registrar_videojuego(juego)


    juego.mostrar_info()


elif tipo == "cliente":
    nombre = input("Nombre: ")
    correo = input("Correo: ")
    contraseña = input("Contraseña: ")


    cliente = Cliente(nombre, correo, contraseña)
    tienda.registrar_usuario(cliente)


    cliente.mostrar_rol()


    juego = Videojuego("animal crossing new leaf", 30000, "simulador de vida")
    cliente.comprar_videojuego(juego)


    juego.mostrar_info()


else:
    print("Opción no válida.")

