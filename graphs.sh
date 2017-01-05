#!/bin/bash

echo -e "\n###\n### Generando estadisticas del repositorio.\n###\n"

sudo apt-get install -y gitstats
gitstats . artifacts/gitstats
