class Node:
    def __init__(self, name, num):  #data만 입력시 next 초기값은 None
        self.name = name
        self.num = num
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.count = 0
        self.head = None
        self.next = None
    
    def add(self, node):
        if self.head == None:
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node
    def get_count(self, name, num):
        cur = self.head
        cnt = 1
        while cur:
            if cur.name == name:
                if cur.num == num:
                    return cnt
            cur = cur.next
            cnt += 1
        return -1
    
    def delete(self, name, num):
        idx = 0
        cur = self.head        
        prevP = None
        nextP = self.head.next
        cnt = self.get_count(name, num) - 1
        if cnt == 0:
            self.head = nextP
        else:
            while idx < cnt:
                if cur.next:
                    prevP = cur
                    cur = nextP
                    nextP = nextP.next
                else:
                    break
                idx += 1
            if idx == cnt:
                prevP.next = nextP
            else:
                return -1
    
    def entry(self):
        cur = self.head
        name = cur.name            
        self.head = self.head.next
        return name
        

# if __name__ == "__main__" :
#    Li = LinkedList()
#    Li.add(Node("Kevin", "01044442222"))
#    Li.add(Node("Dong", "01044453332"))
#    Li.add(Node("Eun", "01044442111"))
#    Li.add(Node("KimChi", "01044442345"))
#
#    print(Li.get_count("Dong", "01044453332"))
#    print(Li.get_count("KimChi", "01044442345"))
#
#    print(Li.entry())
#    print(Li.get_count("Dong", "01044453332"))
#    Li.delete("Dong", "01044453332")
#    print(Li.get_count("KimChi", "01044442345"))