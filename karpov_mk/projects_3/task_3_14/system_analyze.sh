#!/bin/bash

echo
df -h | awk 'NR>1 {
	use = $5 + 0
	printf "%-20s %8s\n", $1, $5

	if (use > 90) {
		print "	ВНИМАНИЕ: " $1 " заполнен более чем на 90% (" $5 ")!"
	}
}'
echo
