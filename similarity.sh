#!/bin/bash

echo -e "\n###\n### Analizando similitud de programas.\n###\n"

READY=$(egrep -R githubusercontent | cut -d":" -f1 | grep "codeeval\|codeabbey" | uniq | rev | cut -d"/" -f2- | rev | sort)

TYPE=${1:-typea}

for ready in $READY; do 
  ./similarity-"$TYPE".sh $ready
done
