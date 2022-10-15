class Node :
    def __init__(self,key,value) :
        self.key = key
        self.value = value
        self.prev = None
        self.next = None 
        
class LRUCache:
    
    def _add_to_head(self,node) :
        node.prev = self.head 
        node.next = self.head.next 
        self.head.next.prev = node 
        self.head.next = node 
    
    def _remove_node(self,node) :
        prevNode = node.prev 
        prevNode.next = node.next 
        node.next.prev = prevNode 
        
    def _pop_from_tail(self) :
        node = self.tail.prev 
        self._remove_node(node)
        return node 
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} 
        self.head = Node(0,0) 
        self.tail = Node(0,0)
        self.head.next = self.tail 
        self.tail.prev = self.head 
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache :
            return -1
        
        node = self.cache[key]
        self._remove_node(node)
        self._add_to_head(node)
        return node.value 
    
    def put(self, key: int, value: int) -> None:
        
        if key in self.cache :
            self.cache[key].value = value 
            self._remove_node(self.cache[key])
            self._add_to_head(self.cache[key])
        else :
            newNode = Node(key,value)
            self.cache[key] = newNode
            self._add_to_head(newNode)
            self.size+=1
            if self.size > self.capacity :
                n = self._pop_from_tail()
                del self.cache[n.key]
                self.size-=1
                
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)