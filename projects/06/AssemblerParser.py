# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 21:22:57 2017

@author: Nelson
"""


class AssemblerParser:

    def __init__(self, fileparse):
        self.inFile = open(fileparse, 'r')
        self.currentCommand = ''

    def ignoreComments(line):
        line = line.partition('//')[0]
        line = line.rstrip()
        return line

    def hasMoreCommands(self):
        x = self.infile.tell()
        self.infile.readline()
        y = self.infile.tell()
        self.infile.seek(x)
        return False if x == y else True

    def advance(self):
        if self.hasMoreCommands():
            line = self.ignoreComments(self.inFile.readline())
            self.currentCommand = line.strip()
        if self.currentCommand == '':
            self.advance()

    def commandType(self):
        x = self.currentCommand
        if x[0] == '@' and x.find(' ') == -1:
            return 'A_COMMAND'
        elif x.find('=') > -1 or x.find(';') > -1:
            return 'C_COMMAND'
        elif x[0] == '@' == '(' and x.count("(") != x.count(")"):
            return 'L_COMMAND'
        else:
            return 'Not Valid'

    def symbol(self):
        x = self.commandType
        if x == 'A_COMMAND':
            return x[1:]
        elif x == 'L_COMMAND':
            return x[x.find("(")+1:x.find(")")]

    def dest(self):
        if self.commandType == 'C_COMMAND':
            y = self.currentCommand.find("=")
            if y != -1:
                return self.currentCommand[:y]
            else:
                return 'null'

    def jump(self):
        if self.commandType == 'C_COMMAND':
            y = self.currentCommand.find(";")
            if y != -1:
                return self.currentCommand[y+1:]
            else:
                return 'null'

    def comp(self):
        if self.commandType == 'C_COMMAND':
            x = self.currentCommand.find(";")
            x = x if x != -1 else len(self.currentCommand)-1
            y = self.currentCommand.find("=")
            y = y if y != -1 else 0
            return self.currentCommand[x:y]


