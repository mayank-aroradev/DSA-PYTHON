class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} 
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self,node):
        p=node.prev
        n=node.next
        n.prev=p
        p.next=n
    def _insert(self,node):
        n=self.head.next
        self.head.next=node
        node.prev=self.head
        node.next=n
        n.prev=node



    def get(self, key: int) -> int:
        if key in self.cache:
            node=self.cache[key]
            self._remove(node)
            self._insert(node)
            return node.val
        return -1
    

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node=Node(key,value)
        self._insert(node)
        self.cache[key]=node

        if len(self.cache)>self.capacity:
            lru=self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)