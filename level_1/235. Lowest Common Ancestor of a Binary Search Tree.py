class Solution(object):
    def lowestCommonAncestor(self, root, p, q):

        result = root
        while result:
            if result.val > p.val and result.val > q.val and result.left:
                result = result.left 
                continue
            elif result.val < p.val and result.val < q.val and result.right:
                result = result.right
                continue
            break
        return result
