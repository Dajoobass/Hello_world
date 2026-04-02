#!/bin/bash

rm -rf sequences/

echo
echo "Генерация случайных цепочек ДНК..."
mkdir -p sequences
echo

for i in {1..10}; do

	if [ $((RANDOM % 3)) -eq 0 ]; then
		touch "sequences/seq$i.fasta"
		echo  "		Генерация seq$i.fasta (ПУСТОЙ!)"

	else
		LEN=$((RANDOM % 451 + 50))
		echo "	Генерация seq$i.fasta (длина: $LEN)..."
		SEQUENCE=$(cat /dev/urandom | tr -dc 'ATGC' | head -c $LEN)
		{
			echo ">seq${i} random DNA sequence"
			echo "$SEQUENCE" | fold -w 80
		} > "sequences/seq$i.fasta"
	fi
done

echo
echo "Созданные файлы:"
ls sequences
echo

echo "		СВОДНАЯ ТАБЛИЦА"
echo
printf "%-18s %8s %8s %7s %7s %2s %10s\n" "Файл" "A" "T" "G" "C" " " "Всего"
echo "----------------------------------------------------------"

for file in sequences/*.fasta; do

	if [ ! -s "$file" ]; then
		printf "%-15s %7s\n" "$(basename "$file")" "ПУСТОЙ!"
		continue
	fi

	A=$(grep -v "^>" "$file" | tr -d '\n' | grep -o "A" | wc -l)
	T=$(grep -v "^>" "$file" | tr -d '\n' | grep -o "T" | wc -l)
	G=$(grep -v "^>" "$file" | tr -d '\n' | grep -o "G" | wc -l)
	C=$(grep -v "^>" "$file" | tr -d '\n' | grep -o "C" | wc -l)

	TOTAL=$((A + T + G + C))

	printf "%-15s %7d %7d %7d %7d %8d\n" "$(basename "$file")" $A $T $G $C $TOTAL
done

echo
read -p "Удалить сгенерированные цепочки?(y/n)" CONFIRM

if [ "$CONFIRM" == "y" ]; then
	rm -rf sequences/
fi
