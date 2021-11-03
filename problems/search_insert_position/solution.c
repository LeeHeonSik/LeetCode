

int searchInsert(int* nums, int numsSize, int target){
    
    // int *ans = malloc(sizeof(int));
    int i;
    
    for (i = 0; i < numsSize; i++) {
        if (target <= nums[i]) {
            return i;
        }
    }
    return i;
}