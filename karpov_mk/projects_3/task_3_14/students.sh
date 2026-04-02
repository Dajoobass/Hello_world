#!/bin/bash

echo
awk '{print $1}' students.txt
echo

echo
awk '{print $2}' students.txt
echo

echo
awk '{print NR ") " $1}' students.txt
echo
