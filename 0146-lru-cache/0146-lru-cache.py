class Node() :
    def __init(self) :
        self.key = 0
        self.value = 0
        self.prev = None 
        self.next = None 
        
class LRUCache:
    def _add_node(self,node) :
        node.prev = self.head 
        node.next = self.head.next 
        self.head.next.prev = node 
        self.head.next = node
        
    def _pop_node(self,node) :
        prev = node.prev 
        new = node.next 
        prev.next = new 
        new.prev = prev 
    
    def _move_to_head(self,node) :
        self._pop_node(node)
        self._add_node(node)
    
    def _pop_tail(self) :
        n = self.tail.prev
        self._pop_node(n)
        return n
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.size = 0
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail 
        self.tail.prev = self.head 
        

    def get(self, key: int) -> int:
        if key in self.cache :
            self._move_to_head(self.cache[key])
            return self.cache[key].value
        else :
            return -1 
    def put(self, key: int, value: int) -> None:
        if key in self.cache :
            self.cache[key].value = value
            self._move_to_head(self.cache[key])
        else :
            newNode = Node()
            newNode.value = value
            newNode.key = key
            
            self.cache[key] = newNode
            self._add_node(newNode)
            self.size += 1
            
            if self.size > self.capacity :
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1 

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)