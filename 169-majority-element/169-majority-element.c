

int majorityElement(int* nums, int numsSize){
    int number = -1;
    int count = 0;
    
    for (int i = 0; i < numsSize; i ++)
    {
        if (count == 0)
        {
            number = nums[i];
            count++;
        }
        else
        {
            if (number == nums[i])
            {
                count++;
            }
            else
            {
                count--;
            }
        }
    }
    return number;
}