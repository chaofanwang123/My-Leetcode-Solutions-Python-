class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def reverse(start, end):
        newhead=ListNode(0); newhead.next=start
        while newhead.next!=end:
            tmp=start.next
            start.next=tmp.next
            tmp.next=newhead.next
            newhead.next=tmp
        return [end, start]

start=ListNode(0)
start.next=ListNode(1)
start.next.next=ListNode(2)
end=ListNode(3)
start.next.next.next=end

c=reverse(start,end)