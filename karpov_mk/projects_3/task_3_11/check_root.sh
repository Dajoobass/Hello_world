#!/bin/bash

check_root() {
	if [ "$EUID" -eq 0 ]; then
		echo "Файл запущен от имени администратора!"
	else
		echo "!!!ОШИБКА!!!"
	fi
}

check_root
