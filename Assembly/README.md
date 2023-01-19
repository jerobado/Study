# Assembly Language
- is a low-level programming language for a specific computer architecture

### Assemblers
- GNU Assembler (GAS)
- Netwide Assembler (NASM)

### Sections of an Assembly program
- an assembly program can be divided into three (3) sections: **data**, **bss** and **text**

#### `data` section
- is used for declaraing initialized data or constant
- you can declare various constant values, files names, or buffer size, and other in this section
    ```assembly
    section.data
    ```

#### `bss` section
- is used for declaring variables
    ```assembly
    section.bss
    ```

#### `text` section
- is used for keeping the actual code
- this section must begin with the declaration `global _start`, which tells the kernel where the program execution begins
    ```assembly
    section.text
        global _start
    _start:
    ```


# Resources
- [Assembly Programming Tutorials](https://www.tutorialspoint.com/assembly_programming/index.htm)