class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Собираем значения из первого списка
        ls1 = []
        current1 = list1
        while current1:
            ls1.append(current1.val)
            current1 = current1.next
        
        # Собираем значения из второго списка
        ls2 = []
        current2 = list2
        while current2:
            ls2.append(current2.val)
            current2 = current2.next
        
        # Объединяем и сортируем
        ls = ls1 + ls2
        ls = sorted(ls)
        
        # Создаем новый связный список
        dummy = ListNode()
        current = dummy
        for val in ls:
            current.next = ListNode(val)
            current = current.next
        
        return dummy.next