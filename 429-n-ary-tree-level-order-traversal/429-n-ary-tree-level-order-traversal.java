/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    public List<List<Integer>> levelOrder(Node root) {
        Queue<Node> queue = new LinkedList<Node>();
        Queue<Node> nextQueue = new LinkedList<Node>();
        List ans = new ArrayList();
       
        if(root == null)
            return ans;
        
        queue.add(root);
        
        int depth = 0;
        while(queue.peek() != null){
            
            List line = new ArrayList();
            
            while(queue.peek() != null){
                Node node = queue.poll();
                line.add(node.val);
                
                for(Node child : node.children)
                    nextQueue.add(child);
            }
            ans.add(line);
            
            
            while(nextQueue.peek() != null)
                queue.add(nextQueue.poll());
            
        }
        
        return ans;
    }
}