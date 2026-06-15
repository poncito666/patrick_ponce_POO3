# patrick_ponce_POO3
Proyecto asignado en clases 
# Nombre del proyecto

**Juegos Real No Feik Store**

# Descripción del sistema

El sistema desarrollado es una tienda virtual de videojuegos que permite el registro de usuarios como vendedores o clientes.

**Problema que resuelve:**
Permite administrar el registro de usuarios y la compra o publicación de videojuegos de manera sencilla.

**Tipo de usuario al que está dirigido:**
Está dirigido a personas que desean vender o comprar videojuegos dentro de una tienda virtual.

**Funcionalidades principales:**

* Registro de usuarios como vendedor o cliente.
* Registro de videojuegos por parte de los vendedores.
* Compra de videojuegos por parte de los clientes.
* Visualización de la información de los videojuegos.
* Identificación del rol de cada usuario.

# Conceptos de POO utilizados

**Encapsulamiento:**
Se aplicó en la clase `Usuario`, donde los atributos `nombre`, `correo` y `contraseña` fueron declarados privados mediante el uso de doble guion bajo (`__`). El acceso al nombre se realiza mediante el método `get_nombre()`.

**Herencia:**
Las clases `Vendedor` y `Cliente` heredan de la clase `Usuario`, reutilizando sus atributos y comportamientos.

**Abstracción:**
La clase `Usuario` es una clase abstracta, ya que contiene el método abstracto `mostrar_rol()`, el cual debe ser implementado por las clases hijas.

**Polimorfismo:**
Las clases `Vendedor` y `Cliente` implementan el método `mostrar_rol()` de manera diferente, permitiendo que un mismo método tenga distintos comportamientos según el objeto que lo utilice.

# Criterios de aceptación

* El sistema debe permitir registrar un usuario como vendedor.
* El sistema debe permitir registrar un usuario como cliente.
* El vendedor debe poder registrar un videojuego correctamente.
* El cliente debe poder comprar un videojuego.
* El sistema debe mostrar la información del videojuego registrado o comprado.
* El sistema debe mostrar el rol correspondiente del usuario registrado.

# Pruebas de usuario

| Acción realizada                      | Resultado esperado                                                  | Resultado obtenido                                              | Estado |
| ------------------------------------- | ------------------------------------------------------------------- | --------------------------------------------------------------- | ------ |
| Registrar un usuario como vendedor    | El sistema crea el usuario y muestra el mensaje de registro exitoso | El usuario se registró correctamente                            | Cumple |
| Registrar un videojuego como vendedor | El videojuego queda almacenado en la lista del vendedor             | El sistema muestra "Videojuego registrado correctamente"        | Cumple |
| Registrar un usuario como cliente     | El sistema crea el usuario y muestra el mensaje de registro exitoso | El usuario se registró correctamente                            | Cumple |
| Comprar un videojuego como cliente    | El videojuego se agrega a la lista de compras del cliente           | El sistema muestra "Has comprado..." y la información del juego | Cumple |
