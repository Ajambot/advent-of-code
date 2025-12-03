with open('3.txt') as f:
    res = 0
    for line in f:
        cur = ["0" for _ in range(12)]
        for i, c in enumerate(line):
            distFromEnd = len(line) - i - 1
            replaced = False
            for j in range(max(0, len(cur)-distFromEnd), len(cur)):
                if replaced:
                    cur[j] = "0"
                    continue
                if c > cur[j]:
                    cur[j] = c
                    replaced = True
        res += int("".join(cur))
    print(res)
