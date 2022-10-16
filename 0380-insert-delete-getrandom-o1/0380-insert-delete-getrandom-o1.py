from random import choice
class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.key = [] 

    def insert(self, val: int) -> bool:
        if val in self.key :
            return False
        self.map[val] = len(self.key)
        self.key.append(val)
        return True
    def remove(self, val: int) -> bool:
        if val not in self.key :
            return False
        last_element, index = self.key[-1] , self.map[val]
        self.map[last_element], self.key[index] = index , self.key[-1]
        self.key.pop()
        del self.map[val]
        return True

    def getRandom(self) -> int:
        return choice(self.key)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()