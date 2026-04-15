\
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reorderList(head):
    if not head or not head.next:
        return
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    prev = None
    curr = slow.next
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    slow.next = None
    first_half = head
    second_half = prev
    while second_half:
        next_temp = first_half.next
        first_half.next = second_half
        second_half = second_half.next
        first_half.next.next = next_temp
        first_half = next_temp