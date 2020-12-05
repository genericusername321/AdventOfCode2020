with open('day1.in') as f:
    nums = [int(num) for line in f for num in line.split()]

N = len(nums)
for i in range(N):
    for j in range(i+1, N):
        a = nums[i]
        b = nums[j] 
        if a + b == 2020:
            print(a*b)


for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            a = nums[i]
            b = nums[j]
            c = nums[k]
            if a + b + c == 2020:
                print(a*b*c)
