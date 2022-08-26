class Solution {
    ArrayList<Integer> array;
    boolean[] used;
    int count = 0;
    int tarV = 0;
    
    public boolean reorderedPowerOf2(int n) {
        array = new ArrayList<Integer>();
        
        while(n > 0){
            array.add(n % 10);
            n /= 10;
        }
        used = new boolean[array.size()] ;
        
        dfsFunction(0, 0);
        return count == 1;
    };    
    
    public void dfsFunction(int v, int depth){
        if(depth == array.size()){
            int cnt = 0;
            for(int i = 0 ; i < 30 ; i++){
                cnt += (v >> i) & 1;
            }
            
            if (cnt == 1 && v != tarV){
                tarV = v;
                count += 1;
            }
            return;
        }
        
        
        for(int i = 0 ; i < array.size() ; i ++){
            if(used[i] || (depth == 0 && array.get(i) == 0))    continue;
            used[i] = true;
            dfsFunction(v * 10 + array.get(i), depth + 1);
            used[i] = false;
        }
    }

}