class Solution:
    def maxPathSum(self, root):
        max_sum = [float('-inf')]
        def dfs(node):
            if not node:
                return 0
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)
            price_newpath = node.val + left_gain + right_gain
            max_sum[0] = max(max_sum[0], price_newpath)

            return node.val + max(left_gain, right_gain)

        dfs(root)
        return max_sum[0]
