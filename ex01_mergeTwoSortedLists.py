class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    # Caso base
    if not l1:
        return l2
    elif not l2:
        return l1
    
    # Comparando os valores dos nós para determinar a ordem
    if l1.val < l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2