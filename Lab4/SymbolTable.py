from HashTable import HashTable


class SymbolTable:
    def __init__(self):
        self.__hashTable = HashTable()

    def add(self, value):
        return self.__hashTable.add(value)

    def get(self, value):
        return self.__hashTable.get(value)

    def __str__(self):
        return str(self.__hashTable)