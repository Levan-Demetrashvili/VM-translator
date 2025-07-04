# VM Translator

A Virtual Machine translator that converts VM code into Hack assembly language for the Nand2Tetris course.

## Overview

This translator converts intermediate VM code into Hack assembly language, handling arithmetic operations, memory access, program flow, and function calls.

## Usage

```bash
# Translate a single VM file
python vm_translator.py program.vm

# Translate all VM files in a directory
python vm_translator.py /path/to/directory
```

## Features

- Arithmetic and logical operations (add, sub, eq, gt, lt, and, or, not)
- Memory segment access (local, argument, this, that, constant, static, pointer, temp)
- Program flow control (label, goto, if-goto)
- Function definition and calling

## Installation

```bash
git clone https://github.com/Levan-Demetrashvili/VM-translator.git
cd VM-translator
```

## Example

**Input (SimpleAdd.vm):**
```vm
push constant 7
push constant 8
add
```

**Output (SimpleAdd.asm):**
```asm
@7
D=A
@SP
A=M
M=D
@SP
M=M+1
@8
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
A=A-1
M=M+D
```

# Development
Developed for Nand2Tetris Projects 7 and 8.
