class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class LinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        curr = self.head

        for i in range(index):
            if curr is None:
                return -1

            curr = curr.next

        if curr is None:
            return -1

        return curr.val

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)

        if self.head is None:
            self.head = new_node
            return

        curr = self.head

        while curr.next is not None:
            curr = curr.next

        curr.next = new_node

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False

        if index == 0:
            self.head = self.head.next
            return True

        curr = self.head

        for i in range(index - 1):
            if curr.next is None:
                return False

            curr = curr.next

        if curr.next is None:
            return False

        curr.next = curr.next.next
        return True

    def getValues(self) -> List[int]:
        values = []
        curr = self.head

        while curr is not None:
            values.append(curr.val)
            curr = curr.next

        return values