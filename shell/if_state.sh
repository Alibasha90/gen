#! /bin/bash


#VAR ="Ali"
#unset VAR
#echo $VAR

#date


#NAME="Zara Ali"
#readonly NAME  # this varible is readonly cant modify...

#NAME="Qadiri"
#echo $NAME'

#echo "hiii"

#echo "File Name: $0"
#echo "First Parameter : $1"
#echo "Second Parameter : $2"
#echo "Quoted Values: $@"
#echo "Quoted Values: $*"
#echo "Total Number of Parameters : $#"


echo -e "Enter the filename : \c"
read filename

if [ -f $filename ]
then 
	echo " file found"

else 
	echo "file not found"
fi
















