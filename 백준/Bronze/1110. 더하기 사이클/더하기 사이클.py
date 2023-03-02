input_num = int(input())
num_new = 0
count = 0

def number_process(num):
  if int(num) < 10:
    num = "0" + str(num)
  else:
    num = str(num)
  return num

while (input_num != num_new):
  if (99 >= input_num >= 0):
    if count == 0:
      num_before = number_process(input_num)
    else:
      num_before = number_process(str(num_new))
    num_before.split()
    num_after = str(int(num_before[0]) + int(num_before[1]))
    num_after = number_process(num_after)
    num_after.split()
    num_new = int(num_before[1]+num_after[1])
    count+=1
if input_num == 0:
  count += 1
print(f"{count}")