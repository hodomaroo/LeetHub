class Solution {
    public int[][] diagonalSort(int[][] mat) {
        
        ArrayList<Integer[]> arr = new ArrayList<Integer[]>();

        for(int i = 0 ; i < mat[0].length ; i++)
            arr.add(new Integer[]{0,i});
        
        
        for(int i = 1 ; i < mat.length ; i++)
            arr.add(new Integer[]{i,0});
        
        for(Integer[] array : arr){
            for(Integer v : array)
                System.out.print(v + " ");
            System.out.println();
        }
        
        for(Integer[] node : arr)
            sortPoint(mat, node[0], node[1]); 

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