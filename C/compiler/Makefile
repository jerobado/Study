# Rules
compiler: compiler.o
	gcc -o compiler compiler.o

main.o: compiler.c
	gcc -c compiler.c

clean:
	rm -f *.out *.o compiler
