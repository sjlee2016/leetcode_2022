class Node :
    def __init__(self,key,value) :
        self.key = key
        self.value = value
        self.prev = None
        self.next = None 
        self.count = 1
        
class NodeList :
    def __init__(self) :
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail 
        self.tail.prev = self.head 
        self.size = 0
        
    def _add_to_head(self,node) :
        prevNode = self.head.next 
        node.next = prevNode 
        prevNode.prev = node 
        node.prev = self.head
        self.head.next = node 
        self.size += 1 
    def _remove_node(self,node) :
        prevNode = node.prev 
        nextNode = node.next 
        prevNode.next = nextNode 
        nextNode.prev = prevNode 
        self.size -= 1
        
class LFUCache(NodeList): 

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.frequency = {}
        self.minFreq = 0 
        self.size = 0 
    
    def _update_freq(self,node) :
        del self.cache[node.key]
        nodelist = self.frequency[node.count]
        nodelist._remove_node(node)
        if node.count == self.minFreq and self.frequency[node.count].size == 0 :
            self.minFreq += 1 
        
        if (node.count + 1 ) in self.frequency :
            nextHigherFreqNodeList = self.frequency[node.count+1]
        else :
            nextHigherFreqNodeList = NodeList() 
        node.count += 1
        nextHigherFreqNodeList._add_to_head(node)
        self.frequency[node.count] = nextHigherFreqNodeList 
        self.cache[node.key] = node
        
    def get(self, key: int) -> int:
        if key in self.cache :
            node = self.cache[key]
            self._update_freq(node)
            return node.value 
        else :
            return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0 :
            return 
        if key in self.cache :
            node = self.cache[key]
            node.value = value 
            self._update_freq(node)
            return
        
        if self.size == self.capacity :
            nodelist = self.frequency[self.minFreq]
            del self.cache[nodelist.tail.prev.key]
            nodelist._remove_node(nodelist.tail.prev)
            self.size -= 1 
        self.size += 1
        self.minFreq = 1
        
        if self.minFreq in self.frequency :
            nodelist = self.frequency[self.minFreq]
        else :
            nodelist = NodeList()
        node = Node(key,value)
        nodelist._add_to_head(node)
        self.cache[key] = node
        self.frequency[self.minFreq] = nodelist 
        

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)