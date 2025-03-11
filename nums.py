def change(nums):
  nums[0] = nums[0] + 1
  nums[1] = nums[1] - 1
  nums = [1, 2, 3]
  print(nums)

def main():
  numbers = [3, 2, 1]
  change(numbers)
  print(numbers)

main()