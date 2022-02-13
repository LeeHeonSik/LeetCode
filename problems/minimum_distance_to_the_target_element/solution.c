

int getMinDistance(int* nums, int numsSize, int target, int start){
    int ans = numsSize, k = 0;
    for (int i = 0; i <numsSize; i++)
    {
        if (nums[i] == target)
        {
            k = abs(i - start);
                if (ans > k) {
                    ans = k;
                }
        }
    }
    return ans;
}