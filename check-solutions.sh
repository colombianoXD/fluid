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

# apt-get install aspell aspell-es
echo ""
echo "### Verificación ortografica"
WORDS=$(aspell --home-dir=conf --personal=ignore.txt -l es list < "$FILES")
if [ -z "$WORDS" ]; then
  echo "Sin errores de ortografia."
  RESULT=0
else
  echo "Con errores de ortografia."
  echo "$WORDS"
  RESULT=1
fi
test $RESULT -ne 0 && exit 1 || exit 0
