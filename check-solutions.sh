#!/bin/bash

FILES=$(find . -iname *.feature)

# apt-get install cucumber
echo "### Verificación sintactica"
cucumber -f progress -q -m -s $FILES


# apt-get install aspell aspell-es
echo ""
echo "### Verificación ortografica"
WORDS=$(aspell -l es list < $FILES)
if [ -z "$WORDS" ]; then
  echo "Sin errores de ortografia."
else
  echo "Con errores de ortografia."
  echo "$WORDS"
fi

