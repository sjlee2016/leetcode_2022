"""
1) O(1) in getting the value for the key => using a hashmap
2) so when the cache size goes over the capacity => delete the least recently used key =>  so the last element in the list indicates the least recently used. 
This means whenever I add a new key (put) or search that key (get) => move the element to the start of the list.
3) So this means I need to be able to pop elements from the list and move that element to the start of the list.
=> what's the most efficient way to do this? It would be using a doubly linked list.
4) use size variable to keep track of the length of the list. 
"""
"""
Define the class Node to use for doubly linked list
"""
class Node :
    def __init__(self,key,value) :
        self.key = key
        self.value = value 
        self.next = None 
        self.prev = None 

class LRUCache:
    def _add_to_front(self,node) :
        temp = self.head.next 
        node.next = temp 
        temp.prev = node 
        node.prev = self.head 
        self.head.next = node 
    
    def _delete_node(self,node) :
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev
        
    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.size = 0
        self.head , self.tail = Node(-1,-1), Node(-1,-1)
        self.head.next = self.tail 
        self.tail.prev = self.head 
        self.cache = {} 
        
    def get(self, key: int) -> int: 
    ## first check if the key exists
    ## if it doesn't, return -1 
        if key not in self.cache :
            return -1 
        ## if it exists, get the node and then move it to the front of the head 
        node = self.cache[key] 
        self._delete_node(node)
        self._add_to_front(node)
        return node.value 
    def _pop_from_tail(self) :
        node = self.tail.prev
        self._delete_node(self.tail.prev)
        return node 
    
    def put(self, key: int, value: int) -> None:
        ## if key already exists in the cache, update the value and move the node to the front of the head.
        if key in self.cache :
            node = self.cache[key]
            node.value = value 
            self.cache[key] = node 
            self._delete_node(node)
            self._add_to_front(node)
            
        ## if key doesn't exists yet, make a new node and add to the front of the linked list
        ## after adding the key, increment the size of list 
        ## check if the size > capacity, if it is , pop an element from the previous of tail 
        else :
            newNode = Node(key,value)
            self._add_to_front(newNode)
            self.size += 1 
            self.cache[key] = newNode
            if self.size > self.capacity :
                node = self._pop_from_tail() 
                del self.cache[node.key]
                self.size-=1
            
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)