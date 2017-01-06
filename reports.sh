#!/bin/bash

echo -e "\n###\n### Generando reportes (gitstats) del repositorio.\n###\n"

mkdir -p build/gitstats
gitstats . build/gitstats 2> build/gitstats/errno.log

echo -e "\n###\n### Generando reportes (gitinspector html) del repositorio.\n###\n"

mkdir -p build/gitinspector
gitinspector -T -m -F html > build/gitinspector/index.html

echo -e "\n###\n### Generando reportes (gitinspector text) del repositorio.\n###\n"

gitinspector -T -m
