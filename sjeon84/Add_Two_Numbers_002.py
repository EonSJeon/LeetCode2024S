# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans=ListNode()
        runningNode=ans

        carry=0
        while(carry!=0 or (not((l1 is None) and (l2 is None)))):
            val1=l1.val if (l1 is not None) else 0
            val2=l2.val if (l2 is not None) else 0

            val=val1+val2+carry
            out ,carry= val%10, val//10

            runningNode.val=out

            l1=l1.next if (l1 is not None) else l1
            l2=l2.next if (l2 is not None) else l2

            if(carry!=0 or (not ((l1 is None) and (l2 is None)))):
                runningNode.next=ListNode()
                runningNode=runningNode.next
            
        

        return ans

            

        