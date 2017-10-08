class ParserVM:

    def __init__(self, fileparse):
        self.inFile = open(fileparse,'r')
        self.outFile = open(fileparse.partition('.')[0] + '.prs','w')
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
        return False if x==y else True

    def advance(self):
        if self.hasMoreCommands():
            self.currentCommand = self.ignoreComments(self.infile.readline())


    def commandType(self):
        x = self.currentCommand.partition(' ')[0]
        if x == 'add' or x == 5 or x == 7:
            return 'C_ARITHMETIC'
        elif x == 'push':
            return 'C_PUSH'
        elif x == 'pop':
            return 'C_POP'
        elif x == 'label':
            return 'C_LABEL'
        elif x == 'goto':
            return 'C_GOTO'
        elif x == 'if':
            return 'C_IF'
        elif x == 'function':
            return 'C_FUNCTION'
        elif x == 'return':
            return 'C_RETURN'
        elif x == 'call':
            return 'C_CALL'

    def arg1(self, text):
        self.author = text

    def arg2(self, scale):
        self.x = self.x * scale
        self.y = self.y * scale