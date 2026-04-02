#!/bin/bash

echo
sum=$(awk '{sum += $2} END {print sum}' students.txt)

avrg=$(awk '{sum += $2; n++} END {print sum/n}' students.txt)

max=$(awk 'NR==1 {MAX=$2} $2>MAX {max=$2} END {print max}' students.txt)

echo
echo "СУММА ОЦЕНОК:	$sum"
echo "СРЕДНЯЯ ОЦЕНКА:	$avrg"
echo "МАКСИМАЛЬНАЯ ОЦЕНКА:	$max"
echo
