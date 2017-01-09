#!/bin/bash

# apt-get install cucumber
echo "### Verificación sintactica"
cucumber -f progress -q -m -s $1


# apt-get install aspell aspell-es
echo ""
echo "### Verificación ortografica"
WORDS=$(aspell -l es list < $1)
if [ -z "$WORDS" ]; then
  echo "Sin errores de ortografia."
else
  echo "Con errores de ortografia."
  echo "$WORDS"
fi

