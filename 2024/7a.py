f = open("7.txt")

target = 0

def findResult(target, nums):
    def dfs(i, sum):
        if i == len(nums) and sum == target:
            return True
        if i >= len(nums) or sum > target:
            return False
        return dfs(i+1, sum * nums[i]) or dfs(i+1, sum + nums[i])
    return dfs(1, nums[0])

res = 0
for line in f:
    target = int(line.split(":")[0])
    nums = line.split(":")[1].strip().split()
    nums = [int(num) for num in nums]
    if findResult(target, nums):
        res += target
print(res)
