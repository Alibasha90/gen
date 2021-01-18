all:add

add:add.o
	gcc add.o -o add

add.o:add.c
	gcc -c add.c -o add.o

rm:
	rm *.o

run:
	@./add 10 20
