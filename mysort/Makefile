CC = gcc
CFLAGS = -c


all:target
target:main.o insert.o bubble.o selection.o quick.o merge.o
	$(CC) insert.o bubble.o selection.o quick.o  merge.o main.o -o target

main.o:main.c
	$(CC) $(CFLAGS) main.c

insert.o:insertion.c
	$(CC) $(CFLAGS) insertion.c -o insert.o

bubble.o:bubble_sort.c
	$(CC) ${CFLAGS}  bubble_sort.c -o bubble.o

selection.o:selection.c
	$(CC) ${CFLAGS} selection.c -o selection.o

quick.o:quick.c
	$(CC) $(CFLAGS) quick.c -o quick.o

merge.o:
	$(CC) $(CFLAGS) merge.c -o merge.o

rm:
	rm -rf *.o  target

run:
	./target  


