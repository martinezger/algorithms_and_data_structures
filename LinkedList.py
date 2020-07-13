class ListNode:
    
    def __init__(self, data):
        self.data= data
        self.next = None

    def __repr__(self):
        if not self.next:
            return f"data:{self.data} next:None"
        return f'data:{self.data} next:{self.next.data}'

class LinkedList:

    def __init__(self):
        self._head = None
        self._tail = None
        self._len = 0

            
    def __str__(self):
        s = ""

        if not self._head:
            return s
      
        current = self._head

        while current.next:
            s+= f' {current.data}'
            current = current.next
                        
        s+=f' {current.data}'
        return s

    
    def __repr__(self):
        return self.__str__()

    
    def __len__(self):
        return self._len

        def append(self, data):
        new_node = ListNode(data)
        self._len +=1
        
        if not self._head:
            self._tail = self._head = new_node
            return

        self._tail.next = new_node
        self._tail = new_node


    def extend(self, L):
        self._len += len(L)
        if not self._head:
            self._head = L

        self._tail.next = L._head
        self._tail = L._tail

    def pop(self):

        if not self._head:
            return None

        self._len -= 1
        
        if self._head == self._tail:
            ans = self._head
            self._head = self._tail = None
            return ans
        
        before = current = self._head
        while current.next:
            before = current
            current = current.next
        
        before.next = None
        self._tail = before

        return current


    def reverse_iterative(self):
        reversed = LinkedList()

        while self._head:
            reversed.append(self.pop().data)

        self._head = reversed._head
        self._tail = reversed._tail


    def reverse_recursive(self):

        def _reverse(prev, current):

            if not current.next: 
                current.next = prev
                self._head = current
                return
        
            nxt = current.next 
            prev.next = None
            current.next = prev
            prev = current

            _reverse(prev,nxt) 

        if not self._head:
            return None
                
        self._tail = self._head
        return _reverse(self._head, self._head.next)
