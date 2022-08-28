class Solution {
    public int[][] diagonalSort(int[][] mat) {
        for(int i = 0 ; i < mat[0].length ; i++)
            sortPoint(mat, 0,  i); 
        
        for(int i = 1 ; i < mat.length ; i++)
            sortPoint(mat, i,  0); 
    
       return mat;   
    }

    public void sortPoint(int[][] matrix, int sx, int sy){
        ArrayList<Integer> diagonalLine = new ArrayList<Integer>();
        
        for(int i = 0 ; i < matrix[0].length ; i++){
            if(sx + i >= matrix.length || sy + i >= matrix[0].length)
                break;
            diagonalLine.add(matrix[sx + i][sy + i]);
        }   
        Collections.sort(diagonalLine);
    
        for(int i = 0 ; i < diagonalLine.size() ; i++){
            if(sx + i >= matrix.length || sy + i >= matrix[0].length) 
                break;
            matrix[sx + i][sy + i] = diagonalLine.get(i);
        }   
    }
}