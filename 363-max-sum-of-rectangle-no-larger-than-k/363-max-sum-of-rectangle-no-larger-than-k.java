class Solution {
    public int maxSumSubmatrix(int[][] matrix, int limit) {
        int prefixSum[][] = new int[matrix.length + 1][matrix[0].length + 1];
        
        for(int i = 0 ; i < matrix.length ; i++){
            for(int j = 0 ; j < matrix[0].length ; j++){
                prefixSum[i + 1][j + 1] = matrix[i][j] + prefixSum[i + 1][j] + prefixSum[i][j + 1] - prefixSum[i][j];
            }
        }   
        
        
        
        for(int[] line : prefixSum){
            for(int v : line){
                System.out.print(v + " ");
            }
            System.out.println();
        }
        
        Integer maxVal = null;
        
        
    
        for(int i = 0 ; i < matrix[0].length ; i++){
            for(int j = i ; j < matrix[0].length ; j ++){ //구간을 정하고...
                TreeSet<Integer> set = new TreeSet<Integer>(Arrays.asList(0));
                
                for(int k = 0 ; k < matrix.length ; k++){
                    int value = prefixSum[k + 1][j + 1] - prefixSum[k + 1][i];
                    
                    Integer v = set.floor(limit - value);
                    
                    if(v != null && value + v <= limit && (maxVal == null || maxVal < value + v))
                        maxVal = value + v;
                        
                    set.add(-value);
                }
            }
        }   
        return maxVal;
    }
}