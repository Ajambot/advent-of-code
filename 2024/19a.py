from functools import cache


f = open("19.txt")

patts = f.readline().strip().split(", ")
patts = set(patts)


res = 0
f.readline()
for line in f:
    towel = line.strip()

    @cache
    def dp(i, last):
        if last == len(towel)-1:
            return True
        if i > len(towel)-1:
            return False
        
        if towel[last+1:i+1] in patts:
            return dp(i+1, i) or dp(i+1, last)
        return dp(i+1, last)
    
    res += int(dp(0, -1))
print(res)
