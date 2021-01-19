# multiple makefiles building 

CC= gcc
CFLAGS= -c  -Wall 
OBJS= main.o   sub.o    ../dir2/add.o    ../dir3/mul.o
LIBS= -lc

INCLUD_mk= ../dir2/Makefile  ../dir3/Makefile 




all: $(OBJS)
	$(CC) -o all  $(OBJS)  

main.o: main.c sub.h ../dir2/add.h ../dir3/mul.h
	$(CC) $(CFLAGS)  main.c  -Idir2/  -Idir3/

sub.o:sub.c
	$(CC) $(CFLAGS) sub.c





include: $(INCLUD_mk)


rm:
	rm  *.o   all


install:all
	@cp all /usr/bin
	@chmod a+x /usr/bin/all
	@chmod og-w /usr/bin/all
	@echo "target successfully installed in path"

uninstall:
	@rm -f /usr/bin/all
	@echo "target uninstalled from path"
