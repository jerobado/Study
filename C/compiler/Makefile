TARGET = compiler

# Rules
$(TARGET): compiler.o
	gcc -o $(TARGET) compiler.o

main.o: compiler.c
	gcc -c compiler.c

clean:
	rm -f *.out *.o $(TARGET)
