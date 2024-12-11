class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def splitNode(self):
        m = len(self.val) // 2
        l = Node(str(int(self.val[0:m])))
        r = Node(str(int(self.val[m:])))
        l.prev = self.prev
        l.next = r
        r.prev = l
        if self.prev:
            self.prev.next = l
        r.next = self.next
        if self.next:
            self.next.prev = r
        return l


    def processNode(self):
        if self.val == "0":
            self.val = "1"
        elif len(self.val) % 2 == 0:
            return self.splitNode()
        else:
            self.val = str(int(self.val)*2024)
        return None


def printNodes(head):
    s = ""
    while head:
        s = s + head.val + " "
        head = head.next
    print(s)

f = open("11.txt", "r")

s = f.read().strip()

stones = s.split()
head = cur = Node("0")
count = 0
for stone in stones:
    count += 1
    prev = cur
    cur = Node(stone, None, prev)
    prev.next = cur

head = head.next

for i in range(25):
    # printNodes(head)
    print(count)
    cur = head
    while cur:
        ret = cur.processNode()
        if ret:
            if cur == head:
                head = ret
            count += 1
            cur = ret.next
        cur = cur.next
print(count)
