# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 00:43:45 2017

@author: Nelson
"""
# !/usr/bin/python

import sys
import AssemblerParser

if len(sys.argv) != 2:
    exit
else:
    script, first = sys.argv

parser = AssemblerParser(sys.argv[1])

outFile = open(sys.argv[1].partition('.')[0] + '.asm', 'w')

while parser.hasMoreCommands():
    if parser.commandType() == 'A_COMMAND':
        y = '0' + bin(int(parser.currentCommand()))
    elif parser.commandType() == 'C_COMMAND':
        y = '111' + parser.dest() + parser.comp() + parser.jump()
    outFile.write(y)
