#!/bin/bash

sed -i 's|/mnt/ssd/mysql|/var/lib/mysql/data|g' settings.php

echo "Reversed!"
