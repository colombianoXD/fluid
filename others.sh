#!/bin/bash

echo -en "travis_fold:start:others\r"
echo "### Accesibilidad de soluciones externas"

SOLVED=$(find . -iname OTHERS.txt | sort)

for i in $SOLVED; do
  CHALLENGE=$(dirname $i | cut -d"/" -f3-)
  echo "--- CHALLENGE: $CHALLENGE"
  SOLUTIONS=$(cat $i)
  for url in $SOLUTIONS; do
    STATUS=$(curl -s -o /dev/null -w "%{http_code}" $url)
    echo $STATUS $url
  done
done

echo -en "travis_fold:end:others\r"
