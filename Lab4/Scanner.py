import re

class Scanner:
    def __init__(self):
        self.reservedWords = ['begin', 'end', 'def_char', 'def_short', 'def_int', 'def_long', 'def_float', 'def_double',
                         'def_void',
                         'break', 'continue', 'do', 'if', 'else', 'loop', 'aslongas', 'in', 'out', 'sqrt']
        self.operators = ['=', '+', '-', '*', '/', '%', '==', '!=', '>', '<', '>=', '<=', '++', '--', '~', '&', '|', '^',
                     '<<',
                     '>>', '!', '&&', '||']
        self.separators = ['(', ')', '[', ']', '{', '}', ';', ' ', ':', '\n', '\t', ',']
        self.reservedWords.sort(reverse=True)
        self.operators.sort(reverse=True)
        self.separators.sort(reverse=True)

    def detectReservedWord(self, line):
        # check if line at this point starts with a reserved word
        for e in self.reservedWords:
            if len(line) >= len(e):
                if line[:len(e)] == e:
                    if len(line) > len(e):
                        if re.match(r'[a-zA-Z0-9_]', line[len(e)]) is None:
                            return True, len(e)
        return False, 0

    def detectOperator(self, line):
        for e in self.operators:
            if len(line) >= len(e):
                if line[:len(e)] == e:
                    return True, len(e)
        return False, 0

    def detectSeparator(self, line):
        # check if line at this point starts with a separator
        for e in self.separators:
            if len(line) >= len(e):
                if line[:len(e)] == e:
                    return True, len(e)
        return False, 0

    def isReservedWord(self, token):
        return token in self.reservedWords

    def isOperator(self, token):
        return token in self.operators

    def isSeparator(self, token):
        return token in self.separators

    def isIdentifier(self, token):
        return re.match(r'^[a-zA-Z]([a-zA-Z]|[0-9]{,19})*$', token) is not None

    def isConstant(self, token):
        return re.match('^(0|[+-]{,1}[1-9][0-9]{,10})$', token) is not None or re.match('^".*"$', token) is not None

    def tokenize(self, line):
        index = 0
        tokens = []
        token = ""
        variableStart = True
        while index < len(line):
            if variableStart == True:
                check = self.detectReservedWord(line[index:])
            else:
                check = (False, None)

            if check[0] is True:
                if token != "":
                    tokens.append(token)
                    token = ""
                length = check[1]
                tokens.append(line[index:index+length])
                index += length
                variableStart = False
                continue

            check = self.detectOperator(line[index:])
            if check[0] is True:
                variableStart = True
                if token != "":
                    tokens.append(token)
                    token = ""
                length = check[1]
                tokens.append(line[index:index+length])
                index += length
                continue

            check = self.detectSeparator(line[index:])
            if check[0] is True:
                variableStart = True
                if token != "":
                    tokens.append(token)
                    token = ""
                length = check[1]
                tokens.append(line[index:index+length])
                index += length
                continue

            token += line[index]
            index += 1
            variableStart = False
        if token != "":
            tokens.append(token)
        return tokens
