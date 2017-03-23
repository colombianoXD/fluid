#!/bin/bash

FILES=$(find . -iname "*.feature")

# apt-get install cucumber
echo "### Verificación sintactica"
#echo "$FILES"
for i in $FILES; do
  echo "### Compilacion Gherkin de $i"
  cucumber -f progress -q -m -s "$i"
  RESULT=$?
  test $RESULT -ne 0 && exit 1
done

exit 0
