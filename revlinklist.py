def revlinklist(head):
    if head is None or head.next is None:
        return head

    prev = None
    current = head

    while current is not None:
        next_node = current.next  # Store the next node
        current.next = prev       # Reverse the link
        prev = current            # Move prev to current
        current = next_node       # Move to the next node

    return prev  # New head of the reversed linked list