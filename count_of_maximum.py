def mostFrequent(arr):
    counts = {}
    for x in arr:
        counts[x] = counts.get(x, 0) + 1

    max_freq = 0
    result = None

    for key, value in counts.items():
        if value > max_freq:
            max_freq = value
            result = key
        elif value == max_freq and key < result:
            result = key

    return result, max_freq

t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int,input().split()))
    val, freq = mostFrequent(s)
    print(val, freq)