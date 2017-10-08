# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 00:30:03 2017

@author: Nelson
"""
class CodeModule:
    #SymbolTable[key] = value
    SymbolTable = {'SP':0,'LCL':1,'ARG':2,'THIS':3,'THAT':4,
                   'R0':0,'R1':1,'R2':2,'R3':3,
                   'R4':4,'R5':5,'R6':6,'R7':7,
                   'R8':8,'R9':9,'R10':10,'R11':11,
                   'R12':12,'R13':13,'R14':14,'R15':15,
                   'SCREEN':16384,'KBD':24576}
    destination = {'null':'000',
                   'M':'001',
                   'D':'010',
                   'MD':'011',
                   'A':'100',
                   'AM':'101',
                   'AD':'110',
                   'AMD':'111'}
    jumpaddress = {'null':'000',
                   'JGT':'001',
                   'JEQ':'010',
                   'JGE':'011',
                   'JLT':'100',
                   'JNE':'101',
                   'JLE':'110',
                   'JMP':'111'}
    computationCode = {'0':'0101010',
                       '1':'0111111',
                       '-1':'0111010',
                       'D':'0001100',
                       'A':'0110000',
                       '!D':'0001101',
                       '!A':'0110001',
                       '-D':'0001111',
                       '-A':'0110011',
                       'D+1':'0011111',
                       'A+1':'0110111',
                       'D-1':'0001110',
                       'A-1':'0110010',
                       'D+A':'0000010',
                       'D-A':'0010011',
                       'A-D':'0000111',
                       'D&A':'0000000',
                       'D|A':'0010101',
                       'M':'1110000',
                       '!M':'1110001',
                       '-M':'1110011',
                       'M+1':'1110111',
                       'M-1':'1110010',
                       'D+M':'1000010',
                       'D-M':'1010011',
                       'M-D':'1000111',
                       'D&M':'1000000',
                       'D|M':'1010101'}
    
    def dest(self,text):
        return self.destination[text]

    def jump(self,text):
        return self.jumpaddress[text]

    def comp(self,text):
        if self.commandType == 'C_COMMAND':
            x = self.currentCommand.find(";")
            x = x if x != -1 else len(self.currentCommand)-1
            y = self.currentCommand.find("=")
            y = y if y != -1 else 0
            return self.currentCommand[x:y]