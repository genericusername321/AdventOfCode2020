TARGET = 2020

def sum2(nums, target):
    # Solution to part 1
    N = len(nums)
    for i in range(N):
        for j in range(i+1, N):
            a = nums[i]
            b = nums[j]
            if a + b == target:
                print(a*b)

def sum3(nums, target):
    # Solution to part 2
    N = len(nums)
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                a = nums[i]
                b = nums[j]
                c = nums[k]
                if a + b + c == target:
                    print(a*b*c)

if __name__ == "__main__":
    with open('day1.in') as f:
        nums = [int(num) for line in f for num in line.split()]

    sum2(nums, TARGET)
    sum3(nums, TARGET)
