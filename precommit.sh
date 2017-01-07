#!/bin/bash

CHANGED=$(git diff --name-only HEAD $(git merge-base HEAD master)) 

echo $CHANGED

pre-commit run --files $CHANGED
