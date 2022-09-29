class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        //배열의 요소에 대해서 i랑 i+x인덱스에 접근
        //일단 연속된 i ~ i+x를 취하는게 반드시 더 효율적! 
        //그럼 평균차이가 가장 작아지는 연속된 부분이 정답!
        
        int partSum = 0;
        
        for(int i = 0 ; i < k - 1; i++)
            partSum += Math.abs(arr[i] - x);
        
        int minPartSum = 0, minIndex = 0;
        for(int i = 0 ; i < arr.length - k + 1; i++){
            partSum += Math.abs(arr[i + k - 1] - x);
            if(partSum < minPartSum)
                minIndex = i;
                minPartSum = partSum;
            //System.out.println(partSum);
            partSum -= Math.abs(arr[i] - x);
        }
        
        ArrayList<Integer> list = new ArrayList<Integer>();
        
        for(int i = 0 ; i < k ; i++)
            list.add(arr[i + minIndex]);
        
        return list;
    }
}