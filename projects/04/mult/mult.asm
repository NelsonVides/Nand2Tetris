// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Adds 1+2+3...+100 \\ Adds a+...+a, b times
    @i      // i refers to some mem. location.
    M=1     // i=1
    @R2    // sum refers to some mem. location.
    M=0     // sum=0
(LOOP)
//; check if exit condition applies
    @i          //; we access the counter address...
    D=M         //; and put this value on D
    @R1         //; then take b value
    D=D-M       //; and substract it to D, which is growing    
    @END
    D;JGT       //; If (i-100)>0 goto END
//; do the operation
    @R0
    D=M     //; D=i
    @R2
    M=D+M   //; sum=sum+R1
    @i          //; this counter still applies :D
    M=M+1   //; i=i+1
//; Looping back to the line, to add 'a' again
    @LOOP   
    0;JMP   //; Goto LOOP
(END)
    @END
    0;JMP   // Infinite loop

