/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
    if(nums.length == 0){
        return 0;
    }
    max_val = nums[0]
    min_val = nums[0]
    global_max = nums[0]
    for(i = 1; i < nums.length; ++i){
        tmp_val = max_val;
        max_val = Math.max(nums[i] * max_val, nums[i], nums[i] * min_val);
        min_val = Math.min(nums[i] * tmp_val, nums[i], nums[i] * min_val);
        global_max = Math.max(max_val, global_max);
    }
    return global_max;
};
