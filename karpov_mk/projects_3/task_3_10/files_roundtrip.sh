#!/bin/bash

echo
echo "	Создание файлов..."
for i in {1..10}; do
	touch "test$i.txt"
done

echo
echo "	Содержимое папки: "
ls
echo

echo "	Удаление файлов..."
for i in {10..1}; do
	rm "test$i.txt"
done

echo
echo "Содержимое папки: "
ls
echo
