class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            current_num = nums[i]
            complement = target - current_num
    
            if complement in hashmap:
                return [hashmap[complement],i]
            hashmap[current_num] = i