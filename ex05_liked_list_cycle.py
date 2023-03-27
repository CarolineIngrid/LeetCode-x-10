class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head: ListNode) -> bool:
    # Cria dois ponteiros, um que avança de um nó por vez e outro que avança de dois nós por vez
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        # Se os ponteiros se encontram, há um ciclo na lista
        if slow == fast:
            return True
    # Se não há ciclo, a lista é percorrida completamente e a função retorna False
    return False
