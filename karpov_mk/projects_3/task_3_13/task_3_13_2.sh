#!/bin/bash

cat > sequences.txt << EOF
	>seq1 ATCGGTACGTTAG
	>seq2 GGCATGCTAGCTA
	>seq3 TTAGCGGATCGTA
	>seq4 CCGTATGCTAGGA
EOF

echo
cat sequences.txt

sed -i 's/ /\t/' sequences.txt

echo
echo "Замена:"
echo
cat sequences.txt
echo
