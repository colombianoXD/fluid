#!/bin/bash -x

CHANGED=$(git diff --name-only HEAD $(git merge-base HEAD master))

echo "### Archivos modificados en este cambio"
echo "$CHANGED"

pre-commit run --files $CHANGED
