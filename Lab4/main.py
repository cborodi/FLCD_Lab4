from SymbolTable import SymbolTable
from PIF import ProgramInternalForm
from Scanner import Scanner

def start():
    fileName = input("Scan file> ")

    scanner = Scanner()
    pif = ProgramInternalForm()
    st = SymbolTable()

    error = False
    lineNumber = 0
    file = open(fileName, 'r')
    for line in file:
        lineNumber += 1
        tokens = scanner.tokenize(line)
        for token in tokens:
            if scanner.isReservedWord(token) or scanner.isOperator(token) or scanner.isSeparator(token):
                pif.add(token, 0)
            elif scanner.isIdentifier(token):
                pos = st.get(token)
                if pos is None:
                    st.add(token)
                    pos = st.get(token)
                pif.add('identifier', pos)
            elif scanner.isConstant(token):
                pos = st.get(token)
                if pos is None:
                    st.add(token)
                    pos = st.get(token)
                pif.add('constant', pos)
            else:
                error = True
                print("Lexical Error at line " + str(lineNumber))
                break

    if error:
        return

    print("The program is lexically correct")

    print('Program Internal Form:\n', pif)
    print('Symbol Table:\n', st)


start()
