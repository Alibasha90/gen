#!/bin/bash

echo -e "enter the filename:\c"
read filename

if [ -f $filename ]
then
	
	if [ -w $filename ]
	then
		echo "type data and cntrl+d "
		cat >> $filename

	else
		echo "The file hasn't write permissions"
	fi

else
	echo "file not found "
fi

