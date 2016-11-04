#!/bin/bash

if [ -z "${1+x}" ]; then
  echo "Login no especificado."
  echo "Uso: $0 login"
  exit -1
else
  login="$1"
fi

_style()
{
  local user="$1"
  local dir=people/"$user"/analysis

  local pyfiles=$(find challenges -iname "$user".py)
  if [ -n "$pyfiles" ]; then
    mkdir -p "$dir"
    echo "Analizando con flake8 ..."
    flake8 $(echo "$pyfiles") > "$dir"/flake8.log 2>&1
    echo "Analizando con pylint ..."
    pylint $(echo "$pyfiles") > "$dir"/pylint.log 2>&1
  else
    echo "No hay archivos de Python"
  fi

  local rbfiles=$(find challenges -iname "$user".rb)
  if [ -n "$rbfiles" ]; then
    mkdir -p "$dir"
    echo "Analizando con ruby-lint ..."
    ruby-lint $(echo "$rbfiles") > "$dir"/ruby-lint.log 2>&1
  else
    echo "No hay archivos de Ruby"
  fi

  local cfiles=$(find challenges -iname "$user".c)
  if [ -n "$cfiles" ]; then
    mkdir -p "$dir"
    echo "Analizando con splint ..."
    splint $(echo "$cfiles") > "$dir"/splint.log 2>&1
  else
    echo "No hay archivos de C"
  fi

  local jsfiles=$(find challenges -iname "$user".js)
  if [ -n "$jsfiles" ]; then
    mkdir -p "$dir"
    echo "Analizando con gjslint ..."
    gjslint $(echo "$rbfiles") > "$dir"/gjslint.log 2>&1
  else
    echo "No hay archivos de JavaScript"
  fi

  local shfiles=$(find challenges -iname "$user".sh)
  if [ -n "$shfiles" ]; then
    mkdir -p "$dir"
    echo "Analizando con shellcheck ..."
    gjslint $(echo "$shfiles") > "$dir"/shellcheck.log 2>&1
  else
    echo "No hay archivos de Shell"
  fi
}

_langs()
{
  local user="$1"
  find . -iname "$user".* -exec basename {} \; | sort | uniq | cut -d. -f2
}

echo "Lenguajes de "$login":"
_langs "$login"

echo "Comenzando analisis de programas"
_style "$login"
