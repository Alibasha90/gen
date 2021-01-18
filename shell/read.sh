#!/bin/bash

#echo $PATH   # standard path environment

#echo $BASH


#echo enter the number:
#read n
#echo your naumber is=$n"""


#read -p 'enter name:'name

#read -sp 'enter password:'password
#echo 
#echo "your name :$name"
#echo "passwoed:	$password" """




#echo "enter the names"
#read -a names 
#echo "names :${names[0]}, ${names[1]} , ${names[2]}"
#echo "names :$REPLY"



#echo $0 $1 $2 $3 > echo $0 $1 $2 $3
#args=("$@")
#echo ${args[0]}
#echo ${args[1]}
#echo ${args[2]}

#echo $@
#echo $#


#=============================================================
#  if condition statements
#=============================================================

#a=1
#if [ $a -le 10 ]
#then
#	echo "condition true"
#fi



#word='A'
#if [[ $word < 'B' ]]
#then 
#	echo "True"
#else
#	echo "fail"
#fi

#read file
args=("$@")

echo "filename:"${args[0]}

if [ -d ${args[0]} ]
then
	echo "file found"
else
	echo " not found"
fi




















































