/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int goodNodes(TreeNode root) {
        if(root != null)
            return dfs(root, -10000);
        return 0;
    }
    
    private int dfs(TreeNode node, int maxValue){
        int count = 0;
        if(node.val >= maxValue)
            count += 1;
        
        if(node.left != null)
            count += dfs(node.left,Math.max(maxValue,node.val));
        
        if(node.right != null)
            count += dfs(node.right,Math.max(maxValue,node.val));
                
        return count;    
    }
}