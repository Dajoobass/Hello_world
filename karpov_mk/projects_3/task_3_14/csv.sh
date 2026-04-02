#!/bin/bash

echo
echo "Названия:"
awk -F, '{print $2}' data.csv
echo

echo "Дороже 20:"
awk -F, '$3 > 20 {print $2 " - " $3}' data.csv
echo

echo "Стоимость:"
awk -F, '{sum += $3} END {print sum}' data.csv
echo
