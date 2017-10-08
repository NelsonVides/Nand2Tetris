// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.


(AGAIN)             // here we come back to the infinite listening
    @KBD
        D=M     // check KBD value
    @VALBLACK
        D;JNE   // and jump to VALBLACK if it's not zero
    @val
        M=0     // load zero on VAL if we didn't scape the previous jump
    @PAINT
        0;JMP   // and jump to paint with val=0
(VALBLACK)
    @val
        M=-1    // set val=1 if we got here

//////////////////////////////////////////////
////////////////   PAINT   ///////////////////
//////////////////////////////////////////////
(PAINT)
    @SCREEN
		D=A         // D-register saves the screen address
	@addr
        M=D         // and we assing this value to the variable addr
// this sets the maximum number of iterations to 512 on the variable 'n'
    @8192
        D=A
    @n
        M=D
    @i
        M=0         // counter i is set to zero
//
    (LOOP)          
        @i          
            D=M     // we load the counter,
        @n
            D=D-M   // check the condition,
        @AGAIN      
            D;JGE   // and jump to AGAIN if it meets

        @val
            D=M        
        @addr
            A=M 
            M=D
    // increment address and counter
        @i
            M=M+1
        @addr
            M=M+1
        @LOOP
            0;JMP
/////////////////////////////////////////////////
@AGAIN
0;JMP