#!/bin/bash

[[ -n ${APP_HOME} ]] && cd ${APP_HOME} || exit 1

python3 --version 2>&1 > /dev/null && \
	rm -f apikey
	python3 main.py
