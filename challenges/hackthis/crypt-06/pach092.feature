# language: es

Característica: Resolver reto 6
  Del sitio hackthis
  De la categoría Crypt
  Con mi usuario pacho92

  Antecedentes:
    Dado que estoy registrado en el sitio hackthis
    Y tengo el sistema operativo Windows versión 10
    Y tengo acceso a internet
    Y tengo instalado el software audacity version 2.1.12
    Y he resuelto el reto Crypt 6

  Escenario: Solución fallida
    Dado un audio
    Entonces con audacity analiza el espectro
    Y descifro con una herramienta online de morse
    Entonces copio el codigo
    Entonces no resuelvo el reto
    Pero concluyo que la respuesta esta en simbologia

  Escenario: Solución fallida
    Dado un codigo numerico
    Entonces copio el codigo
    Entonces no resuelvo el reto
    Pero concluyo que es por simbologia ascii

  Escenario: Solución fallida
    Dado un codigo numerico
    Entonces busco su equivalente en ascii
    Y copio el codigo generado
    entonces no resuelvo el reto
    Pero concluyo que esta en base 16

  Escenario: Solución exitosa
    Dado un codigo numerico
    Entonces por medio de una herramienta online hago conversion a base decimal
    Y genero el codigo ascii con los numeros convertidos
    Y copio el nuevo codigo
    Entonces resuelvo el reto
