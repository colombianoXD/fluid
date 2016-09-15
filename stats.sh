#!/bin/bash

if [ -z "${1+x}" ]; then
  echo "Login no especificado."
  echo "Uso: $0 login"
  exit -1
else
  login="$1"
fi

challenges()
{
  local file="$1"
  local ext="$2"
  find challenges -iname $file$ext | wc -l
}

articles()
{

  local dir=articles/"$1"	
  if [ -d "$dir" ]; then
    ls -l "$dir" | wc -l
  else
    echo 0
  fi
}

echo "$login ha enviado"
echo "$(articles $login) articulos"
echo "$(challenges $login '*') retos"
echo "- $(challenges $login '.asc') esta(n) en palabras"
echo "- $(challenges $login '.py') esta(n) en Python"
echo "- $(challenges $login '.rb') esta(n) en Ruby"
echo "- $(challenges $login '.js') esta(n) en JavaScript"
echo "- $(challenges $login '.java') esta(n) en Java"
echo "- $(challenges $login '.cs') esta(n) en C#"
echo "- $(challenges $login '.clj') esta(n) en Clojure"
