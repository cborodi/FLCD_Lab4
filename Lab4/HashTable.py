
INITIAL_CAPACITY = 41

class HashValue:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        here = self
        str = here.value + " "
        while here.next != None:
            here = here.next
            str += here.value + " "
        return str

class HashTable:
    def __init__(self):
        self.__capacity = INITIAL_CAPACITY
        self.__list = [None] * self.__capacity
        self.__size = 0

    def hash(self, value):
        asciiSum = 0
        for i in range(len(value)):
            asciiSum += ord(value[i])
        return asciiSum % INITIAL_CAPACITY

    def add(self, value):
        self.__size += 1
        index = self.hash(value)

        hv = self.__list[index]

        if hv is None:
            self.__list[index] = HashValue(value)
            return

        prev = hv
        while hv is not None:
            prev = hv
            hv = hv.next

        prev.next = HashValue(value)

    def get(self, value):
        index = self.hash(value)

        hv = self.__list[index]

        internalPosition = 0
        while hv is not None and hv.value != value:
            hv = hv.next
            internalPosition += 1

        if hv is None:
            return None
        else:
            return (index, internalPosition)

    def __str__(self):
        string = ""
        for i in range(len(self.__list)):
            if self.__list[i] == None:
                continue
            string += str(self.__list[i]) + '-> ' + str(i) + '\n'
        return string
