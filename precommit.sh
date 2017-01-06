git diff --name-only HEAD $(git merge-base HEAD master) | tee /dev/stdout | xargs pre-commit run --files
