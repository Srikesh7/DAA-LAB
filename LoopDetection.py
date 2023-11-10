class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def has_cycle(head):
    slow = head
    fast = head

    while fast is not None:
        slow = slow.next
        fast = fast.next

        if fast is not None:
            fast = fast.next

        if slow == fast:
            return True

    return False
