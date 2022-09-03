class Solution {
    public int n;
    public int k;
    public ArrayList<Integer> arr;
        
    public int[] numsSameConsecDiff(int n, int k) {
        arr = new ArrayList<Integer>();
        
        this.n = n;
        this.k = k;
        for(int i = 1 ; i < 10 ; i++)
            generateCase(i, 1);
        
        return arr.stream().mapToInt(i -> i).toArray();
    }
    
    public void generateCase(int value, int depth){
        if(depth == n){
                arr.add(value);
                return;
            }
        
        if(value % 10 >= k)
            generateCase(value * 10 + value % 10 - k, depth + 1);
        if(k > 0 && (value % 10) + k < 10)
            generateCase(value * 10 + value % 10 + k, depth + 1);
    }
}