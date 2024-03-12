#!/bin/bash
#make a copy directory
#Copy file
#Delete the copy

cp guess.sh ./backUp
if [ $? -eq 0 ]
then
	rm guess.sh
	echo "Sucess!"
fi
