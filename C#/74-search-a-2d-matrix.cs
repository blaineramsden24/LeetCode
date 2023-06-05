public class Solution(){
     public bool SearchMatrix(int[][] matrix, int target){
        if (matrix.length == 0) return false;
        const int ROWS = matrix.length;
        const int COLS = matrix[0].length;
        int upper = ROWS * COLS  ;
        int lower = 0;

        while (upper > lower){
            int mid = (low+high) / 2;
            if(matrix[mid/COLS][mid%COLS] == target){
                return true;
            }else if (matrix]mid/COLS)[mid%COLS] < target){
                low = mid+1;
            }else{
                upper = mid-1;
            }
        } 
        return false;
     }
}