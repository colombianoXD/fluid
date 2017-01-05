#!/bin/bash

echo -e "\n###\n### Totales del repositorio.\n###\n"

echo "Total de retos unicos:"
find challenges -type f | grep -v txt | rev | cut -d/ -f2- | rev | sort | uniq | wc -l

echo "Retos unicos de hacking:"
find challenges -type f | grep -v txt | rev | cut -d/ -f2- | rev | sort | uniq | grep -v codeeval | wc -l

echo "Total de retos resueltos:"
find challenges -type f | grep -v txt | wc -l

echo "Retos de hacking:"
find challenges -type f | grep -v txt | grep -v codeeval | wc -l

echo "Total de articulos:"
tree -L 2 articles | wc -l
