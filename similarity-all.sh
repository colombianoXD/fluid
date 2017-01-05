#!/bin/bash

echo -e "\n###\n### Analizando similitud de programas.\n###\n"

READY=$(egrep -R githubusercontent | cut -d":" -f1 | grep "codeeval\|codeabbey" | uniq | rev | cut -d"/" -f2- | rev | sort)

MIN=${1:-5}

for ready in $READY; do 
  ./similarity.sh $ready $MIN
done
