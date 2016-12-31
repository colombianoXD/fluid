#!/bin/bash
find challenges/codeeval challenges/codeabbey \
	-type d '!' \
        -exec test -e "{}/DATA.txt" ';' \
        -print
