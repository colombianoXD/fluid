#!/bin/bash

echo -e "\n###\n### Retos de programación sin set de datos.\n###\n"

find challenges/codeeval challenges/codeabbey \
	-type d '!' \
        -exec test -e "{}/DATA.txt" ';' \
        -print
