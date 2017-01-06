#!/bin/bash

echo -e "\n###\n### Generando reportes (gitstats) del repositorio.\n###\n"

sudo apt-get install -y gitstats
gitstats . artifacts/gitstats 2>>artifacts/gitstats/errno.log

echo -e "\n###\n### Generando reportes (gitinspector html) del repositorio.\n###\n"

sudo -H pip install gitinspector
mkdir -p artifacts/gitinspector

gitinspector -T -m -F html > artifacts/gitinspector/index.html

echo -e "\n###\n### Generando reportes (gitinspector text) del repositorio.\n###\n"

gitinspector -T -m
