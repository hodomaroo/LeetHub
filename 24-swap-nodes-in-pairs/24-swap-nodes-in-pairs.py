# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def swapPairs(self, head):
        if not head:    return head
        elif not head.next: return head   #TwoPare이상으로

        def swapAdjacent(cur,prev):
            global head
            nextCur = cur.next
            if nextCur:
                nextCurnext = nextCur.next

                if prev:    prev.next = nextCur
                elif not prev:  head = nextCur
                nextCur.next = cur
                cur.next = nextCurnext

                if cur.next:    swapAdjacent(cur.next,cur)
            return head
        return swapAdjacent(head,False)


