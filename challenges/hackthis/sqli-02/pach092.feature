# language: es

Característica: Resolver reto 2
  Del sitio hackthis
  De la categoría SQLi
  Con mi usuario pacho92

  Antecedentes:
    Dado que estoy registrado en el sitio hackthis
    Y tengo el sistema operativo Windows versión 10
    Y tengo acceso a internet
    Y he resuelto el reto SQLi 2

  Escenario: Solución fallida
    Dado un boton para navegar por los miembros
    Entonces escojo uno de los miembros que aparecen ahi
    Y lo copio en el campo usuarios
    Entonces realizo una inyeccion de SQL en el campo conraseña
    Entonces no resuelvo el reto
    Pero concluyo que no todos los usuarios son administradores

  Escenario: Solución fallida
    Dado un formulario para ingresar usuarios y contraseñas
    Entonces realizo una inyeccion en el campo usuario
    Y realizo la misma inyeccion en el campo contraseña
    Entonces no resuelvo el reto
    Pero concluyo que la inyeccion se realiza en la barra de direcciones

  Escenario: Solución exitosa
    Dado una consulta SQL en la barra de direcciones
    Entonces realizo una consulta para saber quien es el administrador
    Y me arroja un resultado
    Entonces realizo otra consulta para saber la contraseña de administrador
    Entonces resuelvo el reto
