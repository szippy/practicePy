class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] out = new int[2];
        for(int i = 0; i < nums.length; i++){
            int first = nums[i];
            for(int j = 0; j < nums.length; j++){
                if (j != i){
                    int second = nums[j];
                    if(first + second == target){
                        out[1] = i;
                        out[0] = j;
                        break;
                    }
                }
            }
        }
        return out;
    }
}
