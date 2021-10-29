
class ProgramInternalForm:
    def __init__(self):
        self.__pif = []

    def add(self, token, id):
        self.__pif.append((token, id))

    def __str__(self):
        string = ''
        for e in self.__pif:
            string += str(e) + '\n'
        return string
