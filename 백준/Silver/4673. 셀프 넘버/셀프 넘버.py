nums = list(range(1,10_001))
remove_list=[]    #생성자 리스트
for num in nums:
    for n in str(num):
        num += int(n)
    if num <= 10_000:
        remove_list.append(num)
        
for remove_num in set(remove_list):
    nums.remove(remove_num)
for self_num in nums:
    print(self_num)
