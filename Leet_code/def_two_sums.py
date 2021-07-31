def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]
                
def twoSum(self, nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for i in range(len(nums)):
        hashmap[nums[i]] = i
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap and hashmap[complement] != i:
            return [i, hashmap[complement]] 
              
def twoSum(self, nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [i, hashmap[complement]]
        hashmap[nums[i]] = i
        
def twoSum(self, nums: List[int], target: int) -> List[int]:
    prevMap = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        preMap[n] = i
            
def twoSum(self, nums: List[int], target: int) -> List[int]:
    dictionary = dict()
    pos = 0
    while pos < len(nums):
        if (target - nums[pos]) not in dictionary:
            dictionary[nums[pos]] = pos
            pos += 1
        else:
            return [dictionary[target - nums[pos]], pos]
