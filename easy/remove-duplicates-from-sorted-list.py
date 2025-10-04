class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        
        while current and current.next:
            if current.val == current.next.val:
                # Удаляем дубликат
                current.next = current.next.next
            else:
                current = current.next
        
        return head


