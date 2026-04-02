#!/bin/bash

echo
awk '$2 > 80 {print $1, $2}' students.txt
echo

awk '$2 < 70 {print $1, $2}' students.txt
echo

awk 'NR==1 {print $0}' students.txt
echo


