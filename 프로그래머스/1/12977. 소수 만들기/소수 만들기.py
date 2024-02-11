def solution(nums):
    answer = 0
    tests = []
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                tests.append(nums[i] + nums[j] + nums[k])

    for _, test in enumerate(tests):
        prime = True
        for l in range(2, test):
            if test % l == 0:
                prime = False
        if prime == True:
            answer += 1
    return answer