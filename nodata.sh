#!/bin/bash

echo -en "travis_fold:start:nodata\r"

echo -e "\n###\n### Retos de programación sin set de datos.\n###\n"

find challenges/codeeval challenges/codeabbey \
	-type d '!' \
        -exec test -e "{}/DATA.txt" ';' \
        -print

echo -en "travis_fold:end:nodata\r"
