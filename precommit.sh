#!/bin/bash -x

CHANGED=$(git diff --name-only HEAD $(git merge-base HEAD master))

echo "Archivos modificados:"
echo $CHANGED

pre-commit run --files $CHANGED
