#!/bin/bash
while true
do
	echo "Enter a number 1-10:"
	read val
	if [ $val -eq3 ]
	then
		echo "You guess right!"
		break
	fi
	echo "Wrong guess!"
done
