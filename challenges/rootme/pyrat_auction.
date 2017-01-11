# language: es

Característica: resolver reto realistic
  Del sitio Root-me
  De la categoría Realistic
  Con mi usuario b1nary

  Antecedentes:
    Dado un link a un sitio web simple
    
  Escenario: Explorando el sitio
    Dada una url
    Cuando cuando veo un parámetro que hace referencia a una página en la url
    Y lo cambio por index.php
    Entonces puedo ver el error típico de Local File Inclusion

  Escenario: Obteniendo el codigo fuente
    Dada una url vulnerable a LFI
    Cuando utilizo los filtros de php para imprimir el código fuente en base64
    Y decodifico el código base64
    Entonces veo el código fuente de las páginas index.php y encheres.php

  Escenario: Solución
    Dados los códigos fuentes de las páginas
    Cuando leo detalladamente el código fuente de index.php
    Y veo que se importa una configuración de config.php
    Y utilizó nuevamente los filtros de php para leer el código fuente
      de config.php
    Entonces encuentro la contraseña
