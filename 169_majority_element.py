class Solution:
  def majorityElement(self, nums: list[int]) -> int:
    num_counts = {}
    for num in nums:
      if num in num_counts:
        num_counts[num]+=1
      else:
        num_counts[num]=1

    
    return max(num_counts, key=num_counts.get)



nums=[2,2,1,1,1,2,2]

output = Solution().majorityElement(
  nums=nums
)

print(output)
