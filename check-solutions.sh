#!/bin/bash -x

FILES=$(find . -iname *.feature)

# apt-get install cucumber
echo "### Verificación sintactica"
#cucumber -f progress -q -m -s $FILES
cucumber $FILES
RESULT=$?
test $RESULT -ne 0 && exit 1 || exit 0

# apt-get install aspell aspell-es
echo ""
echo "### Verificación ortografica"
WORDS=$(aspell -l es list < $FILES)
if [ -z "$WORDS" ]; then
  echo "Sin errores de ortografia."
  RESULT=0
else
  echo "Con errores de ortografia."
  echo "$WORDS"
  RESULT=1
fi

test $RESULT -ne 0 && exit 1 || exit 0
