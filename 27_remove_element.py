def removeElement(nums: list[int], val: int) -> int:
  nums[:] = [num for num in nums if num != val]

  # i = 0
  # k = 0
  # last_index = len(nums) - 1

  
  # while i < len(nums) and last_index != i:
  #   num = nums[i]
  #   if num != val:
  #     nums[i] = num
  #     k+=1
  #   else:
  #     nums[i], nums[last_index] = nums[last_index], nums[i]
  #     last_index-=1

  #   if nums[i] != val:
  #     i+=1

  # nums[:] = nums[:i+1]

  return len(nums)


input=[1]
val=1

num_of_not_equal=removeElement(
  nums=input,
  val=val
)

print(input)
print(num_of_not_equal)