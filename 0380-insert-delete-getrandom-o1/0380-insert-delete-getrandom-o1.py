from random import choice
class RandomizedSet:

    def __init__(self):
        self.set = {}
        self.keys = []
    def insert(self, val: int) -> bool:
        if val in self.set :
            return False
        self.set[val] = len(self.keys)
        self.keys.append(val)
        return True 
    def remove(self, val: int) -> bool:
        if val not in self.set :
            return False 
        else :
            last_element, idx = self.keys[-1], self.set[val]
            self.keys[idx], self.set[last_element] = last_element, idx
            self.keys.pop()
            del self.set[val]
            return True

    def getRandom(self) -> int:
        return choice(self.keys)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()