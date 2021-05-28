; Simple Hello world using Assembly
; target: x84-64-bit Linux
;
; build instruction:
;   nasm -f elf64 hello.asm     # compile using nasm targeting x86-64 bit Linux
;   ld hello.o -o hello         # link
;   ./hello                     # run the program
;
; Tutorials: https://cs.lmu.edu/~ray/notes/nasmtutorial/
;


global _start

section .text
_start: mov rax, 1          ; system call for write
        mov rdi, 1          ; file handle 1 is stdout
        mov rsi, message    ; address of string to output
        mov rdx, 20         ; number of bytes
        syscall             ; invoke operating system to do the write
        mov rax, 60         ; system call for exit
        xor rdi, rdi        ; exit code 0
        syscall             ; invoke operating system to exit

section .data
message: db "Hello Assembly!", 10      ; 10 is newline
