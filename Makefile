all: aes_demo

aes_demo: aes.c main.c aes.h
	gcc -O2 -o aes_demo aes.c main.c -march=native

clean:
	rm -f aes_demo
