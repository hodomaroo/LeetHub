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
        
        int x = sx, y = sy;
        
        for(int i = 0 ; i < matrix[0].length ; i++){
            if(x >= matrix.length || y >= matrix[0].length)
                break;
            diagonalLine.add(matrix[x][y]);
            x += 1;
            y += 1;
        }   
        Collections.sort(diagonalLine);
        
        x = sx;
        y = sy;
        
        for(int i = 0 ; i < diagonalLine.size() ; i++){
            if(x >= matrix.length || y >= matrix[0].length)   break;
            matrix[x][y] = diagonalLine.get(i);
            x += 1;
            y += 1; 
        }   
    }
}