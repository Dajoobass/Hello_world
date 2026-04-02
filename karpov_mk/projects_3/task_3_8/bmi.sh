#!/bin/bash

read -p "Введите ваш рост(в сантиметрах): " HEIGHT
read -p "Введите ваш вес: " WEIGHT

HEIGHT_M=$(echo "scale=2; $HEIGHT / 100" | bc)

BMI=$(echo "scale=2; $WEIGHT / ($HEIGHT_M * $HEIGHT_M)" | bc)

echo
echo "Ваш Рост: $HEIGHT | Вес: $WEIGHT"
echo
echo "Ваш BMI: $BMI"
echo
