class Solution {
    public int missingInteger(int[] nums) {
        int sum = 0;
        if (nums.length == 1) {
            return nums[0] + 1;
        }
        if (nums.length != 1 && nums[0] == nums[1] -1) {
            for (int i = 0; i < nums.length - 1; i++) {
                if (nums[i + 1] - nums[i] == 1) {
                    sum = sum + nums[i];
                }else {
                    sum = sum + nums[i];
                    for (int k = 0; k < nums.length; k++) {
                        if (nums[k] == sum) {
                            int search = sum;
                            for (int g = 0; g < nums.length; g++) {
                                if (nums[g] == search){
                                    search++;
                                    g = 0;
                                }
                            }
                            return search;
                        }
                    }
                    return sum;
                }
            }
            sum = sum + nums[nums.length-1];
            return sum;
        }else {
            int search = nums[0];
            for (int g = 0; g < nums.length; g++) {
                if (nums[g] == search){
                    search++;
                    g = 0;
                }
            }
            return search;
        }
    }
}