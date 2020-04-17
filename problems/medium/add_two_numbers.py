class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
        """
        
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        
        """
        stack = []
        n_1 = ''
        n_2 = ''
        while l1:
            stack.append(l1.val)
            l1 = l1.next
        while stack:
            n_1 += str(stack.pop())
        while l2:
            stack.append(l2.val)
            l2 = l2.next
        while stack:
            n_2 += str(stack.pop())
        sum = str(int(n_1) + int(n_2))[::-1]
        head = ListNode(None)
        prev = ListNode(None)
        head = prev
        for s in sum:
            prev.next = ListNode(s)
            prev = prev.next
        return head.next