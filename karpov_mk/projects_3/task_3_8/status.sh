#!/bin/bash

USER=$(whoami)
DATE=$(date +%H:%M:%S)
WD=$(pwd)

echo
echo "	Текущий пользователь: $USER"
echo "		Текущая дата: $DATE"
echo 
echo "-----------------------------------------------------------"
echo
echo "	Рабочая директория: $WD"
echo "		Передано аргументов: $#"
echo
