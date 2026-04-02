#!/bin/bash

for i in {1..20}; do
	if [ $((i % 2)) -eq 0 ]; then
		echo "$i"
	elif [ $i -eq 15 ]; then
		echo
		echo "$i"
		echo "Счетчик достиг 15!"
		echo
		break
	else
		continue
	fi
done
