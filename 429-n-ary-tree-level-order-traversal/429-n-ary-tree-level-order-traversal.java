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
        int front = 1, back = 0;
        
        
        List ans = new ArrayList();
       
        if(root == null)
            return ans;
        
        queue.add(root);
            
        List line = new ArrayList();
        
        while(queue.peek() != null){
            Node node = queue.poll();
            line.add(node.val);    
            front -= 1;

            for(Node child : node.children){
                queue.add(child);
                back += 1;
            }
            
            if(front == 0){
                front = back;
                back = 0;
                ans.add(line);
                line = new ArrayList();
            }
        }
        
        return ans;
    }
}