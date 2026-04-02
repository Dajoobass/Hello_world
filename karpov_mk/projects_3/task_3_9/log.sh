#!/bin/bash

echo
read -p "Введите название файла для поиска: " FILE
FILE="./$FILE"

echo
echo "	ПОИСК: % $FILE %"
echo

if [ -f "$FILE" ]; then
	echo "ФАЙЛ НАЙДЕН"
	ERROR_CODE=0
else
	ERROR_CODE=1
fi

case $ERROR_CODE in
	0)
		echo ;;
	1)
		echo "!!!ERR:ФАЙЛ НЕ НАЙДЕН!!!" 
		echo ;;
	*)
		echo "НЕИЗВЕСТНАЯ ОШИБКА"
		echo ;;
esac
