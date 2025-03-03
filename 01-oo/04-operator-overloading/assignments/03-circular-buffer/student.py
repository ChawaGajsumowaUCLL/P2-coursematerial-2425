class CircularBuffer():
    def __init__(self, lengthList):
        self.__lengthList = lengthList
        self.list = []

    
    
    def add(self, item):
        if len(self.list) == self.__lengthList:
            self.list.pop(0)
            self.list.append(item)
        else:
            self.list.append(item)
    
    def __len__(self):
        count = 0
        for i in self.list:
            count += 1
        return count
    
    def __getitem__(self, index):
        if len(self.list) != 0:
            return self.list[index]